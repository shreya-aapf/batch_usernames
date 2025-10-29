import argparse
import os
from pathlib import Path
import re
import sys
import pandas as pd


def excel_col_letter_to_index(letter: str) -> int:
    """
    Convert Excel column letter(s) to zero-based index.
    e.g., 'A' -> 0, 'B' -> 1, ..., 'Z' -> 25, 'AA' -> 26, etc.
    """
    letter = letter.strip().upper()
    if not re.fullmatch(r"[A-Z]+", letter):
        raise ValueError(f"Invalid Excel column letter: {letter}")
    idx = 0
    for ch in letter:
        idx = idx * 26 + (ord(ch) - ord('A') + 1)
    return idx - 1  # zero-based


def resolve_column(series_df: pd.DataFrame, column_arg: str) -> pd.Series:
    """
    Accepts a column spec as:
      - Header name (exact match),
      - Excel letter(s) like 'A', 'B', 'AA',
      - Zero-based numeric index like '0', '1', ...
    Returns the selected Series.
    """
    # Exact header name
    if column_arg in series_df.columns:
        return series_df[column_arg]

    # Try Excel letters
    try:
        col_idx = excel_col_letter_to_index(column_arg)
        return series_df.iloc[:, col_idx]
    except Exception:
        pass

    # Try numeric index
    if column_arg.isdigit():
        col_idx = int(column_arg)
        return series_df.iloc[:, col_idx]

    # If nothing worked: helpful error
    cols = list(map(str, series_df.columns))
    raise ValueError(
        f"Could not resolve column '{column_arg}'. "
        f"Available headers: {cols}. "
        f"You can also pass a column letter like 'A' or a zero-based index like '0'."
    )


def chunk_list(items, chunk_size=50):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]


def main():
    parser = argparse.ArgumentParser(
        description="Read names from an Excel column and write comma-separated batches of 50 to a .txt file."
    )
    parser.add_argument("--excel", required=True, help="Path to the .xlsx file")
    parser.add_argument(
        "--column", required=True,
        help="Column to read (header name, Excel letter like 'A'/'AA', or zero-based index like '0')"
    )
    parser.add_argument(
        "--sheet-index", type=int, default=0,
        help="Zero-based sheet index (Sheet 1 = 0). Default: 0"
    )
    parser.add_argument(
        "--outfile", required=True,
        help="Base output filename (without extension). The file will be saved in your Downloads folder."
    )
    parser.add_argument(
        "--batch-size", type=int, default=50,
        help="Batch size per line. Default: 50"
    )
    args = parser.parse_args()

    excel_path = Path(args.excel)
    if not excel_path.exists():
        print(f"Error: Excel file not found at '{excel_path}'.", file=sys.stderr)
        sys.exit(1)

    try:
        df = pd.read_excel(excel_path, sheet_name=args.sheet_index, engine="openpyxl")
    except Exception as e:
        print(f"Failed to read Excel: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        series = resolve_column(df, args.column)
    except Exception as e:
        print(f"{e}", file=sys.stderr)
        sys.exit(1)

    # Preserve original order, duplicates; do NOT strip spaces; include blanks
    # Convert NaN to empty string so blanks are preserved as empty entries
    values = series.astype(object).where(pd.notna(series), "").tolist()

    # Prepare output path: Windows Downloads folder
    downloads_dir = Path.home() / "Downloads"
    downloads_dir.mkdir(parents=True, exist_ok=True)
    out_path = downloads_dir / f"{args.outfile}.txt"

    # Write batches: each line is up to N comma-separated names
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            for batch in chunk_list(values, chunk_size=args.batch_size):
                # Join as-is (no quotes, no trimming). This may produce consecutive commas for blanks.
                f.write(", ".join(map(str, batch)) + "\n\n")
    except Exception as e:
        print(f"Failed to write output: {e}", file=sys.stderr)
        sys.exit(1)

    print("Done.")
    print(f"Source Excel : {excel_path}")
    print(f"Sheet index  : {args.sheet_index} (Sheet 1)")
    print(f"Column       : {args.column}")
    print(f"Batch size   : {args.batch_size}")
    print(f"Output file  : {out_path}")


if __name__ == "__main__":
    main()

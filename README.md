# Batch Username Processor

A Python utility that reads names/usernames from Excel files and outputs them in comma-separated batches to text files.

## Features

- Read from any column in Excel files (.xlsx format)
- Flexible column specification (by header name, Excel letter like 'A'/'AA', or zero-based index)
- Configurable batch sizes (default: 50 per line)
- Preserves original order and includes blank/empty entries
- Output saved to Downloads folder automatically
- Support for multiple Excel sheets

## Requirements

- Python 3.6+
- pandas
- openpyxl

## Installation

```bash
pip install pandas openpyxl
```

## Usage

```bash
python batch_names_to_text.py --excel path/to/your/file.xlsx --column A --outfile output_filename
```

### Parameters

- `--excel`: Path to the Excel file (.xlsx)
- `--column`: Column to read from (header name, Excel letter like 'A'/'AA', or zero-based index like '0')
- `--outfile`: Base output filename (without extension) - file will be saved in Downloads folder
- `--sheet-index`: Zero-based sheet index (default: 0 for first sheet)
- `--batch-size`: Number of names per batch/line (default: 50)

### Examples

```bash
# Read from column A, output batches of 50
python batch_names_to_text.py --excel data/users.xlsx --column A --outfile user_batches

# Read from column named "Username", batches of 25
python batch_names_to_text.py --excel data/users.xlsx --column Username --batch-size 25 --outfile usernames

# Read from second sheet (index 1), column B
python batch_names_to_text.py --excel data/users.xlsx --column B --sheet-index 1 --outfile sheet2_names
```

## Output Format

The script creates a text file with comma-separated names, with each line containing up to the specified batch size:

```
name1, name2, name3, ..., name50

name51, name52, name53, ..., name100

...
```

## Notes

- Empty/blank cells are preserved as empty strings in the output
- No trimming of whitespace is performed - names are kept as-is
- Output files are automatically saved to your system's Downloads folder
- The script handles duplicate names and maintains original order

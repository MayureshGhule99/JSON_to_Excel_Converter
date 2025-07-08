# JSON to Excel Converter 🧾➡️📊

A powerful Python tool to convert one or **multiple JSON files** into formatted Excel `.xlsx` files. It supports:

- ✅ Drag-and-drop files into a GUI
- ✅ Batch conversion of multiple files
- ✅ Command-line interface (CLI) for automation

---

## 🔧 Features

- 📂 **Drag-and-drop** JSON files directly into the window for instant conversion
- 📁 **Batch processing** — select and convert multiple files at once
- 💻 **CLI support** — run from the terminal for quick operations
- 🎨 Auto-formatted Excel:
  - Adjusted column widths
  - Bold, colored headers with borders
- 💾 Output saved in the same directory as the original JSON file

---

## 🛠️ Requirements

- Python 3.x

Install dependencies:
```bash
pip install pandas xlsxwriter
```
## 🚀 How to Use

### Option 1: GUI (with drag-and-drop)

Run the script:

```bash
python json_to_excel_converter.py
```

A window will appear — drag and drop one or more .json files into it.

Each .json file will be converted to .xlsx and saved in the same folder.

### Option 2: CLI Mode (Headless)

Convert a single JSON file:
```
python json_to_excel_converter.py path/to/file.json
```
Convert multiple files:
```
python json_to_excel_converter.py file1.json file2.json file3.json
```

## 📁 Example

### Input JSON:
[
  {"name": "Alice", "age": 28},
  {"name": "Bob", "age": 34}
]

### Output excel:
| name  | age |
| ----- | --- |
| Alice | 28  |
| Bob   | 34  |

## ⚙️ Output Notes

* File names are retained:
data.json → data.xlsx

* Existing files with the same name will be overwritten

## 📜 License
This project is released under the MIT License. Free to use, modify, and distribute.

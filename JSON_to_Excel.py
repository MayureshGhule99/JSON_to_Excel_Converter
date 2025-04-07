import pandas as pd
import json
import tkinter as tk
from tkinter import filedialog, messagebox

def json_to_excel(json_file, excel_file):
    """
    Converts a JSON file into an Excel file with proper formatting.
    :param json_file: Path to the input JSON file.
    :param excel_file: Path to the output Excel file.
    """
    try:
        # Load JSON data
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Convert JSON data to DataFrame
        df = pd.json_normalize(data)  # Flattens nested structures if present
        
        # Write to Excel with formatting
        with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
            
            # Get the workbook and worksheet
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']
            
            # Auto-adjust column width
            for col_num, value in enumerate(df.columns.values):
                column_width = max(df[value].astype(str).map(len).max(), len(value)) + 2
                worksheet.set_column(col_num, col_num, column_width)
                
            # Add header formatting
            header_format = workbook.add_format({'bold': True, 'bg_color': '#D7E4BC', 'border': 1})
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, header_format)
        
        messagebox.showinfo("Success", f"Excel file '{excel_file}' has been created successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

def select_file():
    """Opens a file dialog to select a JSON file and converts it to Excel."""
    json_file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if json_file:
        excel_file = json_file.replace(".json", ".xlsx")
        json_to_excel(json_file, excel_file)

# Create a simple GUI window
root = tk.Tk()
root.title("JSON to Excel Converter")
root.geometry("300x150")

btn_select = tk.Button(root, text="Select JSON File", command=select_file)
btn_select.pack(pady=20)

root.mainloop()

import pandas as pd

# Load the Excel file into a DataFrame
file_path = '../data/All Kit Fit Male Comments.xlsx'
df = pd.read_excel(file_path, sheet_name='All Male Comments')

# Iterate over each cell in the DataFrame
for index, row in df.iterrows():
    for col in df.columns:
        # Check if the cell contains a text value (string)
        if isinstance(row[col], str):
            print(f"\nOriginal value in ({index}, {col}): {row[col]}")
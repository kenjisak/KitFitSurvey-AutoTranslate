import pandas as pd

# Load the Excel file
file_path = '../data/All Kit Fit Male Comments.xlsx'
df = pd.read_excel(file_path, sheet_name='All Male Comments')

# Display the DataFrame
print(df)
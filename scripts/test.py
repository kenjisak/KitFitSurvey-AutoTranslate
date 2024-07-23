import pandas
import json
import deepl
from autoDetectLang import detect_Language

# # Load the Excel file into a DataFrame
# file_path = '../data/All Kit Fit Male Comments.xlsx'
# df = pandas.read_excel(file_path, sheet_name='All Male Comments')

# # Iterate over each cell in the DataFrame
# for index, row in df.iterrows():
#     for col in df.columns:
#         # Check if the cell contains a text value (string)
#         if isinstance(row[col], str):
#             print(f"\nOriginal value in ({index}, {col}): {row[col]}")

primary_language = "en" # used from spaCy docs for languages listed
target_language = "EN-GB" # used from DeepL docs for languages listed

# init DeepL Translator
auth_key = ""
with open('../data/api_key.json', 'r') as file:
    auth_key = json.load(file)['api-key']

translator = deepl.Translator(auth_key)

# TODO add spaCY to detect language before sending API request to help with rate limiting
# might not need to implement exponential back off
# make another excel sheet and cut french cells into new one
# send one translation request uploading the whole excel file
# then add back the translated version into

def translate_to_english(sourceText):
    if not detect_Language(sourceText) == primary_language: # if any other language than person spoken language then make DeepL API translation request

        result = translator.translate_text(sourceText, target_lang = target_language)
        
        return result.text

if __name__ == "__main__":
    print(translate_to_english("Je porte ma veste tous les jours et c'est très désagréable."))
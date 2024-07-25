import pandas
import json
import deepl
from autoDetectLang import detect_Language, is_majority_english

input_file_path = '../data/All Kit Fit Male Comments.xlsx'
output_file_path = '../data/Translated Kit Fit Male Comments.xlsx'
sheet_name = 'All Male Comments'
# Load the Excel file into a DataFrame
df = pandas.read_excel(input_file_path, sheet_name = sheet_name)

primary_language = "en" # used from spaCy docs for languages listed
target_language = "EN-GB" # used from DeepL docs for languages listed
expected_secondary_language = "fr"
# init DeepL Translator
auth_key = ""
with open('../data/api_key.json', 'r') as file:
    auth_key = json.load(file)['api-key']

translator = deepl.Translator(auth_key)

def translate_excel_sheet():

    # Iterate over each cell in the DataFrame
    for index, row in df.iterrows():
        for col in df.columns:
            # Check if the cell contains a text value (string)
            if isinstance(row[col], str):
                original_text = row[col]
                original_text = original_text.lower()
                
                # detected = detect_Language(original_text) # DEBUGGING
                # if not detected == primary_language:
                #     if not is_majority_english(original_text):
                #         print(detected)
                #         print(f"\nNon Translated Original Text at ({index}, {col}): \n\t{original_text}")

                # translation operation
                translated_text = translate_to_english(original_text)
                if not translated_text == None and not original_text == translated_text:
                        df.at[index, col] = translated_text
                        print(f"Translated Text at ({index}, {col}): \n\tOriginal: {original_text} \n\tTranslated: {translated_text}")

    # Save the modified DataFrame back to an Excel file
    df.to_excel(output_file_path, sheet_name = sheet_name, index=False)

def translate_to_english(sourceText):
    langdetected = detect_Language(sourceText)
    
    if not langdetected == primary_language: # if any other language than person spoken language then make DeepL API translation request
        if not is_majority_english(sourceText):
            print(langdetected)
            result = translator.translate_text(sourceText, target_lang = target_language)
            
            return result.text
    else: return None


if __name__ == "__main__":
    translate_excel_sheet()

# TODO possibly use a different language detection library for better results
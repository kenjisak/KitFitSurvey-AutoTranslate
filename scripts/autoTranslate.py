import spacy
from spacy.language import Language

from spacy_language_detection import LanguageDetector


def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42)  # We use the seed 42


nlp_model = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp_model.add_pipe('language_detector', last=True)

def detect_Language(sourceText): # Sentence level language detection, finds and returns the majority of language detected in the source text
    
    languages_detected = {}  # Use a dictionary to store language: count pairs
    
    doc = nlp_model(sourceText)
    for i, sent in enumerate(doc.sents):
        lang = sent._.language['language']  # Assuming 'language' key exists in the language detection result
        languages_detected[lang] = languages_detected.get(lang, 0) + 1  # Increment language count

    # Find the language with the highest count
    highest_count_language = max(languages_detected, key=languages_detected.get)
    
    return highest_count_language


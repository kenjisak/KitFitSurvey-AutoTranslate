import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector

import nltk
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer

def get_lang_detector(nlp, name):
    return LanguageDetector(seed=0)


nlp_model = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp_model.add_pipe('language_detector', last=True)

def detect_Language(sourceText): # Document level language detection, finds and returns the majority of language detected in the source text depending on word count
    doc = nlp_model(sourceText)
    return doc._.language['language']

def detect_Language_by_sentence_count(sourceText): # Sentence level language detection, finds and returns the majority of language detected in the source text depending on sentence count
    languages_detected = {}  # Use a dictionary to store language: count pairs
    
    doc = nlp_model(sourceText)
    for i, sent in enumerate(doc.sents):
        lang = sent._.language['language']  # Assuming 'language' key exists in the language detection result
        languages_detected[lang] = languages_detected.get(lang, 0) + 1  # Increment language count

    # Find the language with the highest count
    highest_count_language = max(languages_detected, key=languages_detected.get)
    
    return highest_count_language

nltk.download('words') # Ensure you have the necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
english_words = set(words.words()) # List of English words
lemmatizer = WordNetLemmatizer()

def is_majority_english(paragraph, threshold=0.5):
    tokens = nltk.word_tokenize(paragraph)
    lemmatized_tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    english_word_count = sum(1 for word in lemmatized_tokens if word in english_words)
    proportion_english = english_word_count / len(tokens)
    return proportion_english > threshold

if __name__ == "__main__":
    ex_text = "This is English text. Er lebt mit seinen Eltern und seiner Schwester in Berlin. Yo me divierto todos los días en el parque. Je m'appelle Angélica Summer, j'ai 12 ans et je suis canadienne. Je m'appelle Angélica Summer, j'ai 12 ans et je suis canadienne"

    print(detect_Language(ex_text))
    print(is_majority_english(ex_text))
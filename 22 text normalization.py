# TERMINAL INSTALL COMMANDS (run in terminal before using this script)
"""
!pip install unidecode contractions pdfplumber nltk pyspellchecker polyglot pycld2 indexer spellchecker symspellpy wordsegment
"""

# -----------------------------------
# IMPORTS
# -----------------------------------
import time
import sys
import string
import re
import os

from unidecode import unidecode
import contractions
import pdfplumber

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

from spellchecker import SpellChecker
from wordsegment import load, segment
from symspellpy.symspellpy import SymSpell, Verbosity



# DOWNLOAD NLTK RESOURCES

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
load()



# CLASSES

class WordSegmentation:
    def __init__(self):
        self.dictionary = set()

    def segment_text(self, text):
        return ' '.join(segment(text))


class TextNorm:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.spell_checker = SpellChecker()
        self.symspell = self.load_symspell()

    def load_symspell(self):
        symspell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
        dict_path = "frequency_dictionary_en_82_765.txt"
        if os.path.exists(dict_path):
            symspell.load_dictionary(dict_path, 0, 1)
        else:
            print(f"Warning: {dict_path} not found. SymSpell will be disabled.")
        return symspell

    def lowercase(self, text):
        return text.lower()

    def expand_contractions(self, text):
        return contractions.fix(text)

    def replace_slangs(self, text):
        slangs = {
            r'\bu\b': "you",
            r'\br\b': "are",
            r'\bb4\b': "before",
            r'\bgr8\b': "great",
            r"\blil'\b": "little",
            r"\bhe's\b": "he is",
            r"\bshe's\b": "she is",
            r"\bit's\b": "it is",
            r"\bthat's\b": "that is",
            r"\bwhat's\b": "what is",
            r"\bwhere's\b": "where is",
            r"\bhow's\b": "how is",
            r"\bi'm\b": "i am",
            r"\byou're\b": "you are",
            r"\bwe're\b": "we are",
            r"\bthey're\b": "they are",
            r"\bi've\b": "i have",
            r"\byou've\b": "you have",
            r"\bwe've\b": "we have",
            r"\bthey've\b": "they have",
            r"\bi'll\b": "i will",
            r"\byou'll\b": "you will",
            r"\bwe'll\b": "we will",
            r"\bthey'll\b": "they will",
            r"\bi'd\b": "i would",
            r"\byou'd\b": "you would",
            r"\bwe'd\b": "we would",
            r"\bthey'd\b": "they would"
        }
        for slang, replacement in slangs.items():
            text = re.sub(slang, replacement, text)
        return text

    def replace_accents(self, text):
        return unidecode(text)

    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def remove_stop_words(self, text):
        words = word_tokenize(text)
        return ' '.join([word for word in words if word.lower() not in self.stop_words])

    def tokenize(self, text):
        return word_tokenize(text)

    def lemmatize(self, word):
        return self.lemmatizer.lemmatize(word, pos='v')

    def pos_tags(self, tokens):
        return pos_tag(tokens)

    def symspell_correct(self, text):
        if hasattr(self.symspell, "lookup_compound"):
            suggestions = self.symspell.lookup_compound(text, max_edit_distance=2)
            return suggestions[0].term if suggestions else text
        return text

    def correct_spelling(self, text):
        words = text.split()
        corrected_words = [
            self.spell_checker.correction(word) or word for word in words
        ]
        return ' '.join(corrected_words)

    def process_text(self, text):
        sentences = sent_tokenize(text)
        processed_sentences = []

        for sentence in sentences:
            sentence = self.lowercase(sentence)
            sentence = self.expand_contractions(sentence)
            sentence = self.replace_slangs(sentence)
            sentence = self.replace_accents(sentence)
            sentence = self.remove_punctuation(sentence)
            sentence = self.remove_stop_words(sentence)
            sentence = self.symspell_correct(sentence)
            processed_sentences.append(sentence)

        return processed_sentences


def rotating_slash(duration):
    spinner = ['/', '-', '\\', '|']
    end_time = time.time() + duration

    while time.time() < end_time:
        for symbol in spinner:
            sys.stdout.write(f'\r{symbol} Processing...')
            sys.stdout.flush()
            time.sleep(0.1)


def extract_text_from_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"An error occurred: {e}")
    return text



# MAIN EXECUTION

if __name__ == "__main__":
    print("Enter text (multi-line supported). End input with an empty line:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    text = "\n".join(lines).strip()

    if not text:
        print("No text provided.")
    else:
        rotating_slash(3)

        norm = TextNorm()
        word_segmenter = WordSegmentation()

        processed_sentences = norm.process_text(text)
        for i, processed_sentence in enumerate(processed_sentences):
            print(f"\nProcessed Sentence {i + 1}: {processed_sentence}")

            segmented = word_segmenter.segment_text(processed_sentence)
            print(f"Segmented Sentence: {segmented}")

            corrected = norm.correct_spelling(segmented)
            print(f"Corrected Sentence: {corrected}")

            tokens = norm.tokenize(corrected)
            print(f"Tokens: {tokens}")

            lemmatized_words = [norm.lemmatize(word) for word in tokens]
            print(f"Lemmatized Words: {lemmatized_words}")

            tags = norm.pos_tags(lemmatized_words)
            print(f"POS Tags: {tags}")

            print("-" * 80)

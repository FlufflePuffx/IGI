import re
from patterns import *


def amount_of(pattern, text: str) -> int:
    return len(re.findall(pattern, text))


def count_sentences(text) -> int:
    sentences_amount = amount_of(SENTENCES, text)
    abbreviations_amount = amount_of(ABBREVIATIONS, text)
    doubled_abbreviations_amount = amount_of(DOUBLED_ABBREVIATIONS, text) * 2

    return sentences_amount - abbreviations_amount - doubled_abbreviations_amount


def count_non_declarative_sentences(text) -> int:
    return amount_of(NON_DECLARATIVE_SENTENCES, text)


def average_sentence_length(text):
    nums = re.findall(NUMBERS, text)
    words = [word for word in re.findall(WORDS, text) if word not in nums]
    words_len = sum(len(word) for word in words)

    return round(words_len / count_sentences(text), 2) if count_sentences(text) != 0 else 0


def average_word_length(text):
    nums = re.findall(NUMBERS, text)
    words = list(word for word in re.findall(WORDS, text) if word not in nums)
    words_len = sum(len(word) for word in words)
    return round(words_len / len(words), 2) if len(words) != 0 else 0


def top_k_repeated_n_grams(text: str, k=10, n=4):
    words = re.findall(WORDS, text.lower())
    dictionary = {}
    for i in range(len(words) - n + 1):
        n_gram = ' '.join([str(word) for word in words[i:i + n]])
        if n_gram not in dictionary:
            dictionary[n_gram] = 1
        else:
            dictionary[n_gram] += 1
    sorted_ngrams = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_ngrams[0:k]

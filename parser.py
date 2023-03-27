import re
import patterns


def find(pattern, text: str):
    return len(re.findall(pattern, text))


def count_sentences(text):
    sentences_amount = find(patterns.SENTENCES, text)
    abbreviations_amount = find(patterns.ABBREVIATIONS, text)
    doubled_abbreviations_amount = find(patterns.DOUBLED_ABBREVIATIONS, text) * 2

    return sentences_amount - abbreviations_amount - doubled_abbreviations_amount


def count_non_declarative_sentences(text):
    return find(patterns.NON_DECLARATIVE_SENTENCES, text)


def average_sentence_length(text):
    nums = re.findall(patterns.NUMBERS, text)
    words = [word for word in re.findall(patterns.WORDS, text) if word not in nums]
    words_len = sum(len(word) for word in words)

    return round(words_len / count_sentences(text), 2) if count_sentences(text) != 0 else 0


def average_word_length(text):
    nums = re.findall(patterns.NUMBERS, text)
    words = list(word for word in re.findall(patterns.WORDS, text) if word not in nums)
    words_len = sum(len(word) for word in words)
    return round(words_len / len(words), 2) if len(words) != 0 else 0


def top_k_repeated_n_grams(text: str, k=10, n=4):
    words = re.findall(patterns.WORDS, text.lower())
    dictionary = {}
    for i in range(len(words) - n + 1):
        n_gram = ' '.join([str(word) for word in words[i:i + n]])
        if n_gram not in dictionary:
            dictionary[n_gram] = 1
        else:
            dictionary[n_gram] += 1
    sorted_ngrams = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_ngrams[0:k]

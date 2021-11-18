from translitua import translit, UkrainianKMU
import string
import re

abc = string.ascii_lowercase + string.ascii_uppercase
vector_shift = 1 #This shift is required to compensate for differences in counting - 0 is an empty space, while 1 is an "a" symbol.


def vectorizer(text):
    text_transliterized = translit(text, UkrainianKMU)
    sentences = re.split("\.|!|\?", text_transliterized)
    text_vector = []
    for sentence in sentences:
        if sentence != "":
            words = re.split(",|:|;| ", sentence)
            sentence_vector = []
            for word in words:
                if word != "":
                    word_vector = 0 
                    for letter in word:
                        word_vector = word_vector + abc.index(letter) + vector_shift
                    sentence_vector.append(word_vector)
            text_vector.append(sentence_vector) 
    return(text_vector)


text = "Тепер шафа зі спеціями пахне нашою суботою. Батько наш Бандера! Чомусь, але чому? Апостроф, м'який знак, гречка?!"
vectorizer(text)

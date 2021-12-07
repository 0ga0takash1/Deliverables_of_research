from numpy import tile
import document_read as dr
import classify_to_array as cl

import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')

def is_reference_sentence(text):
    keywords = ["別紙", "別添", "参照"]
    for keyword in keywords:
        if keyword in text:
            return True
    return False

def is_specific_syntax(text):
    # reference syntax
    if is_reference_sentence(text): return 1
    
    doc = nlp(text)
    for sent in doc.sents:
        for token in sent:
            # following syntax
            if token.head.text == "以下" \
                and token.dep_ != 'nummod':
                    return 1
    return 0

def is_candidate(text):
    if is_specific_syntax(text):
        return 1
    return 0

def subject_is_system(doc):
    # if doc:
    return True

def correct_root_dep_(dep):
    if dep == 'acl':
        return 1
    return 0

def correct_dep_(dep):
    if dep == 'case' \
        or dep == 'aux' \
        or dep == 'obj' \
        or dep == 'obl' \
        or dep == 'compound':
        return 1
    return 0

def make_root_of_sent(root_text):
    res = ''   
    for sent in root_text:
        if sent[1] == 1:
            res += sent[0]
    return res

def root_of_sent(text):
    root_text = [] # array of [word, is root word]

    doc = nlp(text)
    for sent in doc.sents:
        for token in sent:
            root_text.append([token.text, 0])
            if token.dep_ == 'ROOT':
                root_text[token.i][1] = 1
            if token.head.dep_ == 'ROOT' \
                and correct_root_dep_(token.dep_):
                root_text[token.i][1] = 1
        words_to_add_to_root = 10
        while words_to_add_to_root > 0:
            words_to_add_to_root = 0
            for token in sent:
                if root_text[token.head.i][1] == 1 \
                    and token.dep_ != 'ROOT':
                    if correct_dep_(token.dep_) == 1:
                        if root_text[token.i][1] != 1:
                            root_text[token.i][1] = 1
                            words_to_add_to_root += 1
    return make_root_of_sent(root_text)

# main
def nlp_classify(text, now_chapter_array):
    # text = root_of_sent(text)
    if subject_is_system(text):
        cl.classify(text, now_chapter_array, is_candidate(text))
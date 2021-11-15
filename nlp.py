from numpy import tile
import document_read as dr
import classify_to_array as cl

import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')

def is_specific_syntax(sent):
    for token in sent:
        # following syntax
        if token.head.text == "以下" \
            and token.dep_ != 'nummod':
                return 1
        # reference syntax
        # if token.i:
        #     return 1
    return 0

def is_candidate(doc):
    for sent in doc.sents:
        if is_specific_syntax(sent):
            return 1
    return 0

def subject_is_system(doc):
    # if doc:
    return True
    # return 0

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

def root_of_sent(doc):
    root_text = [] # array of [word, is root word]
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

# 
def nlp_classify(txt, now_chapter_array):
    doc = nlp(txt)
    # # doc = nlp(root_of_sent(doc_ori))
    # for sent in doc.sents:
    if subject_is_system(doc):
        cl.classify(txt, now_chapter_array, is_candidate(doc))
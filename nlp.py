from numpy import tile
import pdf_read
import classify

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
        if token.i:
            return 1
    return 0

def is_candidate(sent):
    if is_specific_syntax(sent):
        return 1
    return 0

def subject_is_human(doc):
    if doc:
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
    root_text = []
    for sent in doc.sents:
        for token in sent:
            root_text.append([token.text, 0])
            if token.dep_ == 'ROOT':
                root_text[token.i][1] = 1
        for token in sent:
            if token.head.dep_ == 'ROOT':
                root_text[token.i][1] = 1
        add_to_root = 10
        while add_to_root > 0:
            add_to_root = 0
            for token in sent:
                if root_text[token.head.i][1] == 1 \
                    and token.dep_ != 'ROOT':
                    if correct_dep_(token.dep_) == 1:
                        if root_text[token.i][1] != 1:
                            root_text[token.i][1] = 1
                            add_to_root += 1
    return make_root_of_sent(root_text)

for txt in pdf_read.text:
    doc_ori = nlp(txt)
    doc = nlp(root_of_sent(doc_ori))
    for sent in doc.sents:
        if subject_is_human(doc) == 0:
            classify.classify_to_txt(txt, sent, is_candidate(sent))
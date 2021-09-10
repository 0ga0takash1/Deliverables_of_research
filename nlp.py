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

def is_candi(sent):
    if is_specific_syntax(sent):
        return 1
    return 0

for txt in pdf_read.text:
    doc = nlp(txt)
    for sent in doc.sents:
        classify.classify_to_txt(txt, sent, is_candi(sent))
from numpy import tile
import pdf_read
import classify

import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')

# doc = nlp(pdf_read.text)
# for sent in doc.sents:
#     print(sent)

# displacy.serve(doc, style='dep', options={'compact':True})

def is_candi(text):
    if text:
        return 1
    else:
        return 0

for txt in pdf_read.text:
    doc = nlp(txt)
    for sent in doc.sents:
        classify.classify_to_txt(sent, is_candi(txt))
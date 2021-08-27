import pdf_read as pdf

import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')

doc = nlp(pdf.text)

for sent in doc.sents:
    print(sent)

# displacy.serve(doc, style='dep', options={'compact':True})
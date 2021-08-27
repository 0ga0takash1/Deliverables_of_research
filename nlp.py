import pdf_read as pdf
# print(pdf.text)

def replace_name_with_placeholder(token):
     if token.ent_iob != 0 and token.ent_type_ == "PERSON":
         return "[REDACTED] "
     else:
         return token.text

def scrub(text):
    doc = nlp(text)
    with doc.retokenize() as retokenizer:
        for ent in doc.ents:
            retokenizer.merge(ent)
    tokens = map(replace_name_with_placeholder, doc)
    return "".join(tokens)

import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')

# doc = nlp(scrub(pdf.text))
doc = nlp(pdf.text)

for sent in doc.sents:
    print(sent)
    # print(sent.replace('\n', ''))


# displacy.serve(doc, style='dep', options={'compact':True})
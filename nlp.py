from numpy import tile
import document_read as dr
import classify_to_array as cl

import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')

def is_reference_sentence(text):
    keywords = ["別紙", "別添", "参照", "従う"]
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
                and token.dep_ != 'case':
                    return 2
    return 0

def is_candidate(text):
    syn = is_specific_syntax(text)
    if syn == 1:
        return 1
    return 0

def subject_is_system(text):
    human_action = [
        "協力",
    ]
    if text in human_action: return False
    return True

def correct_root_dep_(dep):
    tokens = ['acl', 'advcl']
    if dep in tokens: return 1
    return 0

def correct_root_verb_dep_(dep):
    tokens = ['nsubj', 'obj', 'obl']
    if dep in tokens: return 1
    return 0

def correct_dep_(dep):
    tokens = ['case', 'aux', 'obj', 'obl', 'nummod', 'compound', 'nsubj', 'csubj', 'advmod', 'nmod', 'acl']
    if dep in tokens: return 1
    return 0

def make_root_of_sent(root_text):
    res = ''   
    for sent in root_text:
        if sent[1] > 0:
            res += sent[0]
    return res

def root_of_sent(text):
    root_text = [] # array of [word, is root word]

    doc = nlp(text)
    root_text = []
    for sent in doc.sents:
        root_i = len(sent)
        for token in sent: root_text.append([token.text, 0])
        for token in reversed(sent):
            if token.dep_ == 'ROOT':
                root_i = token.i
                if token.text == 'こと':
                    root_text[token.i][1] = 3
                else:
                    if token.pos_ == 'VERB':
                        root_text[token.i][1] = 2
                    else:
                        root_text[token.i][1] = 1
            if root_text[token.head.i][1] == 3:
                if correct_root_dep_(token.dep_):
                    if token.pos_ == 'VERB':
                        root_text[token.i][1] = 2
                    else:
                        root_text[token.i][1] = 3
        
        exist_word_addition = True
        while exist_word_addition:
            exist_word_addition = False
            for token in sent:
                if token.i != root_i and root_text[token.i][1] == 0:
                    if root_text[token.head.i][1] == 1:
                        if correct_dep_(token.dep_) == 1:
                            root_text[token.i][1] = 1
                            exist_word_addition = True
                    elif root_text[token.head.i][1] == 2:
                        if correct_root_verb_dep_(token.dep_) == 1:
                            root_text[token.i][1] = 1
                            exist_word_addition = True
    return make_root_of_sent(root_text)

# main
def nlp_classify(text, now_chapter_array):
    # root_text = root_of_sent(text)
    # if not is_specific_syntax(text) == 2:
    #     if subject_is_system(text):
    #         cl.classify(text, root_text, now_chapter_array, is_candidate(text))
    cl.classify(text, text, now_chapter_array, 0)

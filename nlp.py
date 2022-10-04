########################################################################
# GinZAを使った構文解析と文章の簡略化を行うコード
########################################################################

from numpy import tile
import document_read as dr
import classify_to_array as cl

import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')

# 係り受け解析結果を返す関数
# 引数：
# 出力：
def get_nlp(text):
    return nlp(text)

# 参照構文の判定
# 引数：
# 出力：
def is_reference_sentence(text):
    keywords = ["別紙", "別添", "参照", "従う"]
    for keyword in keywords:
        if keyword in text:
            return True
    return False

# 以下構文の判定
# 引数：
# 出力：
def is_following_syntax(text):
    doc = get_nlp(text)
    memo_dep_ = []
    for sent in doc.sents: 
        for token in sent:
            if token.head.text == "以下": 
                memo_dep_.append(token.dep_)
    if memo_dep_ == ["compound"]: return True
    return False

# 要求候補とするかの判定
# 現状は参照構文と以下構文と判定された文章を要求候補とする
# 引数：
# 出力：
def is_candidate(text):
    if is_reference_sentence(text) or is_following_syntax(text): return 1
    return 0

# 文章が人の行動かどうかを判別するための関数
# 人の行動は、ソフトウェアに対する要求ではないため
# 引数：
# 出力：
def subject_is_human_action(text):
    human_action = [
        "協力",
    ]
    if text in human_action: return True
    return False

# 形態素の性質別に取得する係り受け関係を指定
# # 形態素がROOTの「こと」である場合の係り受け関係を指定
# 引数：
# 出力：
def correct_root_dep_(dep):
    tokens = ['acl', 'advcl', 'advmod']
    if dep in tokens: return 1
    return 0
# # 形態素がROOTで、かつ「こと」以外、または動詞である場合の係り受け関係を指定
# 引数：
# 出力：
def correct_root_verb_dep_(dep):
    tokens = ['nsubj', 'obj', 'obl']
    if dep in tokens: return 1
    return 0
# # 上記で指定した以外の形態素に対しての係り受け関係を指定
# 引数：
# 出力：
def correct_dep_(dep):
    tokens = ['case', 'aux', 'obj', 'obl', 'nummod', 'compound', 'nsubj', 'csubj', 'advmod', 'nmod', 'acl']
    if dep in tokens: return 1
    return 0

# 引数：形態素ごとに取得するか否かが指定されている
# 引数に基づいて、簡略化した文字列を生成する関数
# 引数：
# 出力：
def make_root_of_sent(root_text):
    res = ''   
    for sent in root_text:
        if sent[1] > 0:
            res += sent[0]
    return res

# 文章の簡略化を行う関数
# 引数：
# 出力：
def root_of_sent(text):
    root_text = [] # array of [word, is root word]

    doc = get_nlp(text)
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
# 引数：
# 出力：
def nlp_classify(text, now_chapter_array):
    root_text = root_of_sent(text)
    if is_candidate(text):
        if not subject_is_human_action(text):
            cl.unnlp_classify(text, now_chapter_array, is_candidate(text))
    cl.classify(text, text, now_chapter_array, 0)

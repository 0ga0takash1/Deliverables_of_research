########################################################################
# キーワードに関するコード
# キーワードを管理するテキストファイルに対する処理
########################################################################

import os, re
import arrays as ar

# キーワードを格納するテキストファイルのパスを取得
# 引数：
# 出力：
def get_path(list_num):
    path = os.getcwd()
    path += "/keyword_lists/"
    path += ar.id_list[list_num]
    path += "/_.txt"
    return path

# 引数の単語を、指定した品質特性のキーワードとして追加
# 引数：
# 出力：
def add(keyword, list_num):
    with open(get_path(list_num-1), 'a') as fp:
        fp.write('\n')
        fp.write(keyword)
    print("keyword addition completed!")
    return True
# add("パスワード", 1)
# add("パスワード", 61)

# 引数の単語を指定した品質特性のキーワードから除外
# 引数：
# 出力：
def delete(keyword, list_num):
    with open(get_path(list_num-1), 'r+') as fp:
        new = fp.readlines()
        fp.seek(0)
        for key in new:
            if keyword not in key:
                fp.write(key)
        fp.truncate()
    return True
# delete("キーワード", 1)

# すべてのテキストファイルを検索し、品質特性別のキーワードを格納する配列を生成
# 引数：
# 出力：
def get_keywords():
    res = []
    for i in range(len(ar.id_list)):
        with open(get_path(i)) as fp:
            keywords = []
            for word in fp:
                keywords.append(word.rstrip('\n'))
            match = re.match('^(\[\[)', keyword)
            if match:
                keyword = keyword[2:]
                keyword = keyword.split('++')
            res.append(keywords)
    return res
keywords_list = get_keywords()
########################################################################
# 「format<文書名>.txt」を読み込み、配列に整形するコード

# 整形した配列=["タイトル", <文章or子階層の整形した配列>]
# 例
[
    [
        "1章タイトル", [
            ["1-1節タイトル", ["文章1-1_1", "文章1-1_2", "文章1-1_3"]],
            ["1-2節タイトル", ["文章1-2_1", "文章1-2_2"]],
            "文章1_1",
            "文章1_2",
        ]
    ],[
        "2章タイトル", [
            ["2-1節タイトル", ["文章2-1_1", "文章2-1_2", "文章2-1_3", "文章2-1_4"]],
        ]
    ]
]
########################################################################


import re

# 不自然な改行を解消する関数
# 引数：フォーマット途中の配列
# 出力：不自然な改行による配列分割を解消したフォーマット配列
def fix_break(ar):
    all_text = 1
    for i in ar:
        if isinstance(i, list):
            all_text = 0
            i[1] = fix_break(i[1])
    if all_text and len(ar) > 1:
        ar = (''.join(ar))
        ar = re.findall(".*?。", ar)
    return ar

# デバッグ用出力関数
# 引数：フォーマット配列
# 出力：章タイトルと章内の文章を出力
def out(ar):
    for i in ar:
        if isinstance(i, str):
            print(i)
        elif isinstance(i, list):
            print('\ntitle: ', i[0])
            out(i[1])

# 引数：document_read.pyで生成したテキストファイル
# 出力：フォーマット配列
def main(file_path):
    txt_array_list = [] # テキスト情報を配列に格納する変数
    tmp_sentences = [] # 文章情報を一時的に格納する変数

    front_chapter_idx = -1 # 一つ前の章idxを格納する変数
    front_section_idx = -1 # 一つ前の節idxを格納する変数
    front_paragraph_idx = -1 # 一つ前の段落idxを格納する変数
    front_subparagraph_idx = -1 # 一つ前のサブ段落idxを格納する変数

    # 節、段落、サブ段落かを判定するフラグ
    # 配列の初期化を行うために利用
    section_flag = False        # 節かどうか
    paragraph_flag = False      # 段落かどうか
    subparagraph_flag = False   # サブ段落かどうか

    with open(file_path, encoding="utf-8") as f:
        doc = f.readlines()

        escape_flag = False
        for s_line in doc:
            s_line = s_line.strip()
    
            # エスケープ処理
            if s_line == "/://*--- escape start ---*//:/":
                escape_flag = True
                continue
            elif s_line == "/://*--- escape end ---*//:/":
                escape_flag = False
                continue
            
            if escape_flag == True: continue

            # now_XXX = [title, [sentences]]
            # now_chapter：章, now_section：節, now_paragraph：段落
            # 現状は3階層までしか対応できない
            if front_chapter_idx >= 0: 
                now_chapter = txt_array_list[front_chapter_idx]
                if front_section_idx >= 0: 
                    now_section = now_chapter[1][front_section_idx]
                    if front_paragraph_idx >= 0:
                        now_paragraph = now_section[1][front_paragraph_idx]
                        if front_subparagraph_idx >= 0:
                            now_subparagraph = now_paragraph[1][front_subparagraph_idx]
            
            title = s_line

            # 正規表現を利用して、サブ段落にマッチする場合の処理を行う
            # 注意>>>>>>>正規表現について、再設定をし直す必要あり
            res = re.match('^(\(|（)(ア|イ|ウ|エ|オ|カ|キ|ク|ケ|コ)(\)|）)', s_line)
            if res:
                if not subparagraph_flag:
                    now_paragraph.append([])
                subparagraph_flag = True
                now_paragraph[1].append([title])

                if not front_subparagraph_idx == -1:
                    now_subparagraph.append(tmp_sentences)
                
                tmp_sentences = []
                front_subparagraph_idx += 1
                continue

            # 正規表現を利用して、段落にマッチする場合の処理を行う
            # 注意>>>>>>>正規表現について、再設定をし直す必要あり
            res = re.match('^[①-⑳]', s_line)
            if res:
                if not paragraph_flag:
                    now_section.append([])
                
                if subparagraph_flag == True and not front_subparagraph_idx == -1:
                    now_subparagraph.append(tmp_sentences)
                
                paragraph_flag=True                
                now_section[1].append([title])

                if not front_paragraph_idx == -1:
                    now_paragraph.append(tmp_sentences)
                
                tmp_sentences = []
                front_paragraph_idx += 1
                front_subparagraph_idx = -1
                subparagraph_flag = False
                continue

            # 正規表現を利用して、節にマッチする場合の処理を行う
            # 注意>>>>>>>正規表現について、再設定をし直す必要あり
            res = re.match('^(\(|（)[1-9１-９](\)|）)', s_line)
            if res:
                if not section_flag:
                    now_chapter.append([])
                
                if subparagraph_flag == True and not front_subparagraph_idx == -1:
                    now_subparagraph.append(tmp_sentences)
                elif paragraph_flag == True and not front_paragraph_idx == -1:
                    now_paragraph.append(tmp_sentences)
                            
                section_flag = True
                now_chapter[1].append([title])

                if not front_section_idx == -1:
                    now_section.append(tmp_sentences)

                tmp_sentences = []
                front_section_idx += 1
                front_paragraph_idx = -1
                front_subparagraph_idx = -1
                paragraph_flag = False
                subparagraph_flag = False
                continue

            # 正規表現を利用して、章にマッチする場合の処理を行う
            # 注意>>>>>>>正規表現について、再設定をし直す必要あり
            res = re.match('^[1-9１-９](．|\.)[^0-90-9]', s_line)
            if res:
                txt_array_list.append([title])
                if subparagraph_flag == True and not front_subparagraph_idx == -1:
                    now_subparagraph.append(tmp_sentences)
                elif paragraph_flag == True and not front_paragraph_idx == -1:
                    now_paragraph.append(tmp_sentences)
                elif section_flag == True and not front_section_idx == -1:
                    now_section.append(tmp_sentences)

                if not section_flag == True and not paragraph_flag == True\
                    and not front_chapter_idx == -1:
                    now_chapter.append(tmp_sentences)

                tmp_sentences = []
                front_chapter_idx += 1
                front_section_idx = -1
                front_paragraph_idx = -1
                front_subparagraph_idx = -1
                section_flag = False
                paragraph_flag = False
                subparagraph_flag = False
                continue

            tmp_sentences.append(s_line)

    # 最後の文章の情報を格納するための処理
    if subparagraph_flag == True and not front_subparagraph_idx == -1:
        now_subparagraph.append(tmp_sentences)
    elif paragraph_flag == True and not front_paragraph_idx == -1:
        now_paragraph.append(tmp_sentences)
    elif section_flag == True and not front_section_idx == -1:
        now_section.append(tmp_sentences)
    elif not section_flag == True and not front_chapter_idx == -1:
        now_chapter.append(tmp_sentences)

    txt_array_list = fix_break(txt_array_list)
    # out(txt_array_list)
    return txt_array_list
import re

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

def out(ar):
    for i in ar:
        if isinstance(i, str):
            print(i)
        elif isinstance(i, list):
            print('\ntitle: ', i[0])
            out(i[1])

def main(file_path):
    txt_array_list = []
    tmp_sentences = []

    front_chapter_idx = -1
    front_section_idx = -1
    front_paragraph_idx = -1

    section_flag = False
    paragraph_flag = False

    with open(file_path) as f:
        doc = f.readlines()
        # doc = tbl_escape(doc, tbls)
        tbl_flag = False
        for s_line in doc:
            s_line = s_line.strip()
            if s_line == "/://*--- table start ---*//:/":
                tbl_flag = True
                continue
            elif s_line == "/://*--- table end ---*//:/":
                tbl_flag = False
                continue
            
            if tbl_flag == True: continue

            # now_XXX = [title, [sentences]]
            if front_chapter_idx >= 0: 
                now_chapter = txt_array_list[front_chapter_idx]
                if front_section_idx >= 0: 
                    now_section = now_chapter[1][front_section_idx]
                    if front_paragraph_idx >= 0:
                        now_paragraph = now_section[1][front_paragraph_idx]
            # 第n項
            res = re.match('^[①-⑳]', s_line)
            if res:
                if not paragraph_flag:
                    now_section.append([])
                paragraph_flag=True
                
                title = s_line
                now_section[1].append([title])

                if not front_paragraph_idx == -1:
                    now_paragraph.append(tmp_sentences)
                
                tmp_sentences = []
                front_paragraph_idx += 1
                continue

            # 第n節
            res = re.match('^(\(|（)[1-9１-９](\)|）)', s_line)
            if res:
                if not section_flag:
                    now_chapter.append([])

                if paragraph_flag == True and not front_paragraph_idx == -1:
                    now_paragraph.append(tmp_sentences)
                            
                section_flag = True

                title = s_line
                now_chapter[1].append([title])

                if not front_section_idx == -1:
                    now_section.append(tmp_sentences)

                tmp_sentences = []
                front_section_idx += 1
                front_paragraph_idx = -1
                paragraph_flag = False
                continue

            # 第n章
            res = re.match('^[1-9１-９](．|\.)[^0-90-9]', s_line)
            if res:
                txt_array_list.append([s_line])
                if paragraph_flag == True and not front_paragraph_idx == -1:
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
                section_flag = False
                paragraph_flag = False
                continue

            tmp_sentences.append(s_line)

    if paragraph_flag == True and not paragraph_flag == -1:
        now_paragraph.append(tmp_sentences)
    elif section_flag == True and not front_section_idx == -1:
        now_section.append(tmp_sentences)
    elif not section_flag == True and not front_chapter_idx == -1:
        now_chapter.append(tmp_sentences)

    txt_array_list = fix_break(txt_array_list)
    # out(txt_array_list)
    return txt_array_list
import nlp

def read_formated_table(table):
    return True
    # for i in range(table[0][2][0]):
    #     for j in range(table[0][2][1]):
    #         pass

now_chapter_array = []
def read_and_process(chapter):
    # print("\n", "see: ", chapter, "\n")
    now_chapter_array.append(chapter[0])

    for chap_txt_tbl in chapter[1]:
        if isinstance(chap_txt_tbl, str):
            nlp.nlp_classify(chap_txt_tbl, now_chapter_array)
        elif isinstance(chap_txt_tbl, list):
            if chap_txt_tbl[0][0] == "is table":
                read_formated_table(chap_txt_tbl)
                continue
            read_and_process(chap_txt_tbl)
        
    now_chapter_array.pop()
    return True

def main(formated_array):
    for chapter in formated_array:
        read_and_process(chapter)
    return True
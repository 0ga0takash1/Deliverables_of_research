import format_document_to_array as format_doc
import nlp

now_chapter_array = []
def read_process(formated_array):
    for chapter in formated_array:
        now_chapter_array.append(chapter[0])

        for chapter_or_text in chapter[1]:
            if isinstance(chapter_or_text, str):
                nlp.nlp_classify(chapter_or_text, now_chapter_array)
            elif isinstance(chapter_or_text, list):
                read_process(chapter_or_text)
        
        now_chapter_array.pop()
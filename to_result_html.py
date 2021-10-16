import classify_to_array as cl
import prog_keyword as pk

from bs4 import BeautifulSoup4

def one(chapter_array, other_factors_array, text):
    with open('index.html') as index:
        soup = BeautifulSoup4(index, 'html.parser')
        res = soup.new_tag('li', class_="output")

        p = soup.new_tag('p')

        chapter_tag = soup.new_tag('span', id="chapter")
        chapter = ''
        for i in len(chapter_array):
            chapter.append(chapter_array[i])
            if i is not len(chapter_array)-1:
                chapter.append(' &gt; ')
        chapter_tag.string = chapter
        p.append(chapter)

        p.append(soup.new_tag('br'))

    return res

def push():
    soup = BeautifulSoup4('index.html', 'html.parser')
    # [[requirement], [candidate]]
        # [text, chapter, [other factors]]
    for factor in range(len(cl.result)):
        i = 0
        for req in cl.result[factor]: # req == array of [text, chapter, [other factors]]
            if i == 0:
                print(cl.Require_factors[i])

            else:
                print(cl.Require_factors[i], "候補")
            
            if len(req) == 0:
                print("There is no sentences corresponding to this element.")
                continue
            
            for text in req: # text == [text, chapter, [other factors]]
                # print("Chapter:", text[1])
                # print(text[0])
                # print("Other applicable factors:")
                for num in text[2]:
                    print(cl.Require_factors[num], ".")
            i += 1
    return True

def clear():
    cl.result_clear()
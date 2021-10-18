import classify_to_array as cl
import prog_keyword as pk
import arrays as ar

from bs4 import BeautifulSoup
from xml.sax.saxutils import unescape

def chapter(array):
    res = ''
    for i in range(len(array)):
        res += array[i]
        if i < len(array)-1:
            res += ' &gt; '
    return res

def other_factors(array):
    res = ''
    for i in range(len(array)):
        res += ar.Require_factors[array[i]]
        if i < len(array)-1:
            res += '，'
    res += 'にも該当'
    return res

def one(chapter_array, other_factors_array, sentence):
    soup = BeautifulSoup('', 'html.parser')
    res = soup.new_tag('li', class_="output")

    p = soup.new_tag('p')

    chapter_tag = soup.new_tag('span', class_="chapter")
    chapter_tag.string = unescape(chapter(chapter_array))
    p.append(chapter_tag)

    p.append(soup.new_tag('br'))
    p.append(soup.new_tag('br'))

    other_factors_tag = soup.new_tag('span', class_="other_factors")
    other_factors_tag.string = other_factors(other_factors_array)
    p.append(other_factors_tag)

    res.append(p)

    sentence_tag = soup.new_tag('span', class_="sentence")
    sentence_tag.string = sentence
    res.append(sentence_tag)
    return res

# print(one(['1. aa', '(1) bb', '① cc'], ['機能', '使用性'], 'あああ'))

def clear():
    cl.result_clear()
    with open('index.html') as index:
        soup = BeautifulSoup(index, 'html.parser')
        for i in range(len(cl.result)):
            for j in range(2):
                ID = pk.id_list[i]
                if j != 0:
                    ID += '_candi'
            
                conp = soup.find('ul', attrs={'id':ID})
                conp.clear()
    return True

def push():
    clear()
    # [[requirement], [candidate]]
        # [text, chapter, [other factors]]
    for factor in range(len(cl.result)):
        i = 0
        for req in cl.result[factor]: # req == array of [text, chapter, [other factors]]
            ID = pk.id_list[i]
            if i != 0:
                ID += '_candi'
            
            with open('index.html') as index:
                soup = BeautifulSoup(index, 'html.parser')
                conp = soup.find('ul', attrs={'id':ID})

                if len(req) == 0:
                    conp.string = '該当なし'
                    continue
                
                for text in req: # text == [text, chapter, [other factors]]
                    conp.append(one(text[1], text[2], text[0]))
            i += 1
    return True
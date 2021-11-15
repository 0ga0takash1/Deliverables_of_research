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
    if len(array):
        for i in range(len(array)):
            res += ar.Require_factors[array[i][0]]
            if i < len(array)-1:
                res += '，'
        res += 'にも該当'
    return res

def one(chapter_array, other_factors_array, sentence):
    soup = BeautifulSoup('', 'html.parser')
    res = soup.new_tag('li')
    res.attrs['class'] = "output"

    p = soup.new_tag('p')

    chapter_tag = soup.new_tag('span')
    chapter_tag.attrs['class'] = "chapter"
    chapter_tag.string = unescape(chapter(chapter_array))
    p.append(chapter_tag)

    p.append(soup.new_tag('br'))
    p.append(soup.new_tag('br'))

    other_factors_tag = soup.new_tag('span')
    other_factors_tag.attrs['class'] = "other_factors"
    other_factors_tag.string = other_factors(other_factors_array)
    p.append(other_factors_tag)

    res.append(p)

    sentence_tag = soup.new_tag('span')
    sentence_tag.attrs['class'] = "sentence"
    sentence_tag.string = sentence
    res.append(sentence_tag)
    return res

# print(one(['1. aa', '(1) bb', '① cc'], ['機能', '使用性'], 'あああ'))

def clear():
    with open('index.html') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        for i in range(len(cl.result)):
            for j in range(2):
                ID = ar.id_list[i]
                if j != 0:
                    ID += '_candi'
            
                conp = soup.find('ul', attrs={'id':ID})
                conp.clear()
        out = soup.prettify()
        with open('index.html', 'w') as f:
            f.write(out)
    return True

def clear2():
    with open('sample.html') as f:
        with open('index.html', 'w') as f2:
            f2.write(f.read())
    return True

def push():
    clear2()
    # [[requirement], [candidate]]
        # [text, chapter, [other factors]]
    for i in range(len(cl.result)):
        for j in range(len(cl.result[i])): 
            req = cl.result[i][j] # req == array of [text, chapter, [other factors]]
            ID = ar.id_list[i]
            if j != 0:
                ID += '_candi'
            
            with open('index.html') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

                if len(req) == 0:
                    no_one_tag = soup.new_tag('li')
                    no_one_tag.attrs['class'] = "output"
                    no_one_tag.string = '該当なし'
                    soup.find('ul', attrs={'id':ID}).append(no_one_tag)
                else:
                    for text in req: # text == [text, chapter, [other factors]]
                        soup.find('ul', attrs={'id':ID}).append(one(text[1], text[2], text[0]))
                        soup.find('ul', attrs={'id':ID}).append(soup.new_tag('br'))

                out = soup.prettify()
                with open('index.html', 'w') as f:
                    f.write(out)
    return True
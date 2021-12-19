import classify_to_array as cl
import arrays as ar

from bs4 import BeautifulSoup
import re
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

def replace_keyword_to_tag(text: str, target: str) ->str:
    return re.sub(rf"(?<!<span>)({target})(?!</span>)", r"<span>\1</span>", text)

def one(chapter_array, other_factors_array, text_keyword):
    soup = BeautifulSoup('', 'html.parser')
    res = soup.new_tag('div')
    res.attrs['class'] = "output"

    p = soup.new_tag('p')

    chapter_tag = soup.new_tag('div')
    chapter_tag.attrs['class'] = "chapter"
    chapter_tag.string = unescape(chapter(chapter_array))
    p.append(chapter_tag)

    other_factors_tag = soup.new_tag('div')
    other_factors_tag.attrs['class'] = "other_factors"
    other_factors_tag.string = other_factors(other_factors_array)
    p.append(other_factors_tag)

    res.append(p)

    text = text_keyword[0]
    keyword = text_keyword[1]

    for i in keyword:
        text = replace_keyword_to_tag(text, i)

    text_tag = soup.new_tag('div')
    text_tag.attrs['class'] = "sentence"
    text_tag.string = text
    res.append(text_tag)
    return res

# print(one(['1. aa', '(1) bb', '① cc'], ['機能', '使用性'], 'あああ'))

def clear(result_html):
    with open('sample.html') as f:
        with open(result_html, 'w') as f2:
            f2.write(f.read())
    return True

def fix_escape(result_html):
    with open(result_html) as fp:
        file = fp.read()
        file = file.replace("&lt;span&gt;", r"<span>")
        file = file.replace("&lt;/span&gt;", r"</span>")
        with open(result_html, 'w') as f:
            f.write(file)
    return True

def push(result_html):
    clear(result_html)
    # [[requirement], [candidate]]
        # [[text, keyword], chapter, [other factors]]
    for i in range(len(cl.result)):
        for j in range(len(cl.result[i])): 
            req = cl.result[i][j] # req == array of [[text, keyword], chapter, [other factors]]
            ID = ar.id_list[i]
            if j != 0:
                ID += '_candi'
            
            with open(result_html) as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

                if len(req) == 0:
                    no_one_tag = soup.new_tag('div')
                    no_one_tag.attrs['class'] = "output"
                    inside = soup.new_tag('div')
                    inside.attrs['class'] = "no_one"
                    inside.string = '該当なし'
                    no_one_tag.append(inside)
                    soup.find('div', attrs={'id':ID}).append(no_one_tag)
                else:
                    for text in req: # [[text, keyword], chapter, [other factors]]
                        soup.find('div', attrs={'id':ID}).append(one(text[1], text[2], text[0]))

                out = soup.prettify()
                with open(result_html, 'w') as f:
                    f.write(out)
    fix_escape(result_html)
    return True
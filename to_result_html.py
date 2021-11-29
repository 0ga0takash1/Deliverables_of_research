import classify_to_array as cl
import arrays as ar

from bs4 import BeautifulSoup
import html
import re
# from xml.sax.saxutils import unescape

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

def replace_keyword_to_tag(text: str, target: str) -> str:
    return re.sub(rf"(?<!<span>)({target})(?!</span>)", r"<span>\1</span>", text)

def one(chapter_array, other_factors_array, text_keyword):
    soup = BeautifulSoup('', 'html.parser')
    res = soup.new_tag('div')
    res.attrs['class'] = "output"

    p = soup.new_tag('p')

    chapter_tag = soup.new_tag('div')
    chapter_tag.attrs['class'] = "chapter"
    chapter_tag.string = html.unescape(chapter(chapter_array))
    p.append(chapter_tag)

    other_factors_tag = soup.new_tag('div')
    other_factors_tag.attrs['class'] = "other_factors"
    other_factors_tag.string = other_factors(other_factors_array)
    p.append(other_factors_tag)

    res.append(p)

    text = text_keyword[0]
    keyword = text_keyword[1]
    # for keyword in keywords:
    # keyword_highlight = soup.new_tag('span')
    # keyword_highlight.string = keyword
    # tag = html.unescape(str(keyword_highlight))
    # print(tag)
    # text = text.replace(keyword, tag)

    text = replace_keyword_to_tag(text, keyword)
    print("a: " ,text)

    text_tag = soup.new_tag('div')
    text_tag.attrs['class'] = "sentence"
    text_tag.string = text
    res.append(text_tag)
    return res

# print(one(['1. aa', '(1) bb', '① cc'], ['機能', '使用性'], 'あああ'))

def clear():
    with open('sample.html') as f:
        with open('index.html', 'w') as f2:
            f2.write(f.read())
    return True

def push():
    clear()
    # [[requirement], [candidate]]
        # [[text, keyword], chapter, [other factors]]
    for i in range(len(cl.result)):
        for j in range(len(cl.result[i])): 
            req = cl.result[i][j] # req == array of [[text, keyword], chapter, [other factors]]
            ID = ar.id_list[i]
            if j != 0:
                ID += '_candi'
            
            with open('index.html') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

                if len(req) == 0:
                    no_one_tag = soup.new_tag('div')
                    no_one_tag.attrs['class'] = "output"
                    no_one_tag.string = '該当なし'
                    soup.find('div', attrs={'id':ID}).append(no_one_tag)
                else:
                    for text in req: # [[text, keyword], chapter, [other factors]]
                        # new = replace_keyword_to_tag(new.find('div', attrs={'class':"sentence"}).string, text[0][1])
                        soup.find('div', attrs={'id':ID}).append(one(text[1], text[2], text[0]))

                out = soup.prettify()
                with open('index.html', 'w') as f:
                    f.write(out)
    return True
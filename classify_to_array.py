import re, os
import prog_keyword as pk
import arrays as ar

for_result = []
for i in range(12): for_result.append([[], []])

# [text, chapter array, [factors]]
# factors = [factor num, is candi, keywords]
doc_classify = []

# [[requirement], [candidate]]
    # [[text, keyword], chapter array, [other factors]]
result = for_result[:]

def classify(text, root_text, now_chapter_array, is_candi):
    applicable_factors = [] # [factor num, is candi, keyword]
    for i in range(len(ar.id_list)):
        with open(pk.get_path(i)) as fp:
            keywords = []
            for word in fp:
                keywords.append(word.rstrip('\n'))
            for keyword in keywords:
                match = re.match('^(\[\[)', keyword)
                if match:
                    keyword = keyword[2:]
                    keyword = keyword.split('++')
                    if (keyword[0] in root_text) and (keyword[1] in root_text):
                        applicable_factors.append([i, is_candi, keyword])
                        break
                elif keyword in root_text:
                    if keyword == "ログ" and "プログラム" in root_text:
                        continue
                    applicable_factors.append([i, is_candi, keyword])
                    break
    doc_classify.append([text, now_chapter_array[:], applicable_factors])

def leveling_to_result_array():
    result = for_result[:]
    for sent in doc_classify: # sent == [text, chapter array, [factors]]
        for i in range(len(sent[2])):
            other_factors = sent[2][:]
            see = other_factors.pop(i) # see == [factor num, is candi, keyword]
            if isinstance(see[2], str): see[2] = [see[2]]
            result[see[0]][see[1]].append([[sent[0], see[2]], sent[1], other_factors])
    # for i in range(len(result)):
    #     print(ar.Require_factors[i], len(result[i][0]), len(result[i][1]))

def print_one_result(i):
    for req in result[i]: # req == [[requirement], [candidate]]
        for j in range(2):
            if j == 0:
                print(ar.Require_factors[i])
            else:
                print(ar.Require_factors[i], "候補")

            if len(req[j]) == 0:
                print("There is no sentences corresponding to this element.")
                continue
            
            for text in req: # text == [text, chapter array, [other factors]]
                print("Chapter:", text[1])
                print("Other applicable factors:")
                for num in text[2]:
                    print(ar.Require_factors[num], ".")
                print(text[0])
    return True

def print_all_result():
    for i in range(len(result)):
        print_one_result(i)
    return True

def result_clear():
    doc_classify = []
    result = for_result[:]
    return True
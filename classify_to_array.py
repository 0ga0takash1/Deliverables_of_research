import os
import prog_keyword as pk
import array as ar

for_result = [
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
]

# [text, chapter, [factors]]
# factors = [factor num, is candi]
doc_classify = []

# [[requirement], [candidate]]
    # [text, chapter, [other factors]]
result = for_result

def classify_to_array(text, sent, now_chapter, is_candi):
    applicable_factors = []
    for i in range(len(pk.paths)):
        path = os.getcwd()
        path += pk.paths[i]
        with open(path) as fp:
            keywords = fp.readline()
            for keyword in keywords:
                if keyword == sent:
                    # add(text, i, is_candi)
                    applicable_factors.append([i, is_candi])
                    break
    doc_classify.append([text, now_chapter, applicable_factors])

def leveling_to_result_array():
    for sent in doc_classify: # sent == [text, chapter, [factors]]
        for i in range(sent[2]):
            other_factors = sent[2]
            see = other_factors.pop(i) # see = [factor num, is candi]
            result[see[0]][see[1]].append([sent[0], sent[1], other_factors])

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
            
            for text in req: # text == [text, chapter, [other factors]]
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
    result = for_result
    return True
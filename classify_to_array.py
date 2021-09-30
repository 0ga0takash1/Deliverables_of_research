import os
import prog_keyword as pk

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

Require_factors = [
    "外部とのインタフェース",
    "機能要求",
    "性能要求",
    "論理データベース要求",
    "設計制約",
    "機能適合性",
    "性能効率性",
    "互換性",
    "使用性",
    "信頼性",
    "セキュリティ",
    "保守性",
    "移植性"
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

def print_all_result():
    for factor in range(len(result)):
        i = 0
        for req in result[factor]: # req == array of [text, chapter, [other factors]]
            if i == 0:
                print(Require_factors[i])
            else:
                print(Require_factors[i], "候補")
            
            if len(req) == 0:
                print("There is no sentences corresponding to this element.")
                continue
            
            for text in req: # text == [text, chapter, [other factors]]
                print("Chapter:", text[1])
                print(text[0])
                print("Other applicable factors:")
                for num in text[2]:
                    print(Require_factors[num], ".")
            i += 1
    return True

def print_one_result(i):
    i -= 1
    for req in result[i]: # req == array of [text, chapter, [other factors]]
            if i == 0:
                print(Require_factors[i])
            else:
                print(Require_factors[i], "候補")

            if len(req) == 0:
                print("There is no sentences corresponding to this element.")
                continue
            
            for text in req: # text == [text, chapter, [other factors]]
                print("Chapter:", text[1])
                print(text[0])
                print("Other applicable factors:")
                for num in text[2]:
                    print(Require_factors[num], ".")
    return True

def result_clear():
    return for_result
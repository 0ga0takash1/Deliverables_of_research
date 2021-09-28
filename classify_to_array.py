import os
import prog_keyword as pk

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

# [text, chapter, [elements]]
# elements = [num, candi]
doc_classify = []

# [text, chapter, [other elements]]
result = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

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
    for sent in doc_classify: # [text, chapter, [elements]]
        elements = sent[2]


def print_all_result():
    for i in range(len(paths)):
        print(Require_factors[i])
        path_dir = os.getcwd()
        path_dir += paths[i]

        path = path_dir+"_.txt"
        with open(path) as fp:
            print(fp.readline())

        print(Require_factors[i], "候補")
        path = path_dir+"__.txt"
        with open(path) as fp:
            print(fp.readline())
    return True

def print_one_result(i):
    i -= 1
    print(Require_factors[i])
    path_dir = os.getcwd()
    path_dir += paths[i]

    path = path_dir+"_.txt"
    with open(path) as fp:
        print(fp.readline())

    print(Require_factors[i], "候補")
    path = path_dir+"__.txt"
    with open(path) as fp:
        print(fp.readline())
    return True

def output_files_clear():
    for i in range(len(paths)):
        path_dir = os.getcwd()
        path_dir += paths[i]
 
        path = path_dir+"_.txt"
        with open(path, 'w'):
            pass
 
        path = path_dir+"__.txt"
        with open(path, 'w'):
            pass
        print(Require_factors[i], "Complete clear!")
    return True
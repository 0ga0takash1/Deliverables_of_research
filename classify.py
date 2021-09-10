import os
import prog_keyword as pk

paths = [
    "/output_lists/1_Interface_with_outside/",
    "/output_lists/2_Functional_requirements/",
    "/output_lists/3_Performance_requirements/",
    "/output_lists/4_Logical_database_requirements/",
    "/output_lists/5_Design_constraints/",
    "/output_lists/6_1_Functional_compatibility/",
    "/output_lists/6_2_Performance_efficiency/",
    "/output_lists/6_3_Compatibility/",
    "/output_lists/6_4_Usability/",
    "/output_lists/6_5_Reliability/",
    "/output_lists/6_6_Security/",
    "/output_lists/6_7_Maintainability/",
    "/output_lists/6_8_Portability/"
]

Chapters = [
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

def add(text, list_num, is_candi):
    path_dir = os.getcwd()
    path_dir += paths[list_num]
    if is_candi == 0: 
        path = path_dir+"_.txt"
    else: 
        path = path_dir+"__.txt"
    with open(path, mode='w') as fp:
        fp.write(text)
    # print("Classification succeeded!")
    return True

def classify_to_txt(text, sent, is_candi):
    for i in range(len(pk.paths)):
        path = os.getcwd()
        path += pk.paths[i]
        with open(path) as fp:
            keywords = fp.readline()
            for keyword in keywords:
                if keyword == sent:
                    add(text, i, is_candi)

def print_result():
    for i in range(len(paths)):
        print(Chapters[i])
        path_dir = os.getcwd()
        path_dir += paths[i]

        path = path_dir+"_.txt"
        with open(path) as fp:
            print(fp.readline())

        print(Chapters[i], "候補")
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
        print(Chapters[i], "Complete clear!")
    return True
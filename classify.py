import os

paths = [
    "/output_lists/1_Interface_with_outside/_.txt",
    "/output_lists/2_Functional_requirements/_.txt",
    "/output_lists/3_Performance_requirements/_.txt",
    "/output_lists/4_Logical_database_requirements/_.txt",
    "/output_lists/5_Design_constraints/_.txt",
    "/output_lists/6_1_Functional_compatibility/_.txt",
    "/output_lists/6_2_Performance_efficiency/_.txt",
    "/output_lists/6_3_Compatibility/_.txt",
    "/output_lists/6_4_Usability/_.txt",
    "/output_lists/6_5_Reliability/_.txt",
    "/output_lists/6_6_Security/_.txt",
    "/output_lists/6_7_Maintainability/_.txt",
    "/output_lists/6_8_Portability/_.txt"
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

def add(text, list_num):
    path = os.getcwd()
    path += paths[list_num-1]
    fp = open(path, mode='w')
    fp.write(text)
    fp.close()
    # print("Classification succeeded!")
    return True

def print_result():
    for i in range(len(paths)):
        print(Chapters[i])
        path = os.getcwd()
        path += paths[i]
        fp = open(path)
        print(fp.readline())
        fp.close()
    return True
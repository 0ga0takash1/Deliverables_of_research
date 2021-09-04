import os

paths = [
    "/keyword_lists/1_Interface_with_outside/_.txt",
    "/keyword_lists/2_Functional_requirements/_.txt",
    "/keyword_lists/3_Performance_requirements/_.txt",
    "/keyword_lists/4_Logical_database_requirements/_.txt",
    "/keyword_lists/5_Design_constraints/_.txt",
    "/keyword_lists/6_1_Functional_compatibility/_.txt",
    "/keyword_lists/6_2_Performance_efficiency/_.txt",
    "/keyword_lists/6_3_Compatibility/_.txt",
    "/keyword_lists/6_4_Usability/_.txt",
    "/keyword_lists/6_5_Reliability/_.txt",
    "/keyword_lists/6_6_Security/_.txt",
    "/keyword_lists/6_7_Maintainability/_.txt",
    "/keyword_lists/6_8_Portability/_.txt"
]

def add(keyword, list_num):
    path = os.getcwd()
    if list_num < 5: path += paths[list_num-1]
    # elif list_num > 60: path += paths[5][list_num%10-1]
    fp = open(path, mode='w')
    fp.write(keyword)
    fp.close()
    print("keyword addition completed!")
    return True

# add("パスワード", 1)
# add("パスワード", 61)
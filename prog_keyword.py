import os

paths = [
    "/keyword_lists/1_Interface_with_outside/_.txt",
    "/keyword_lists/2_Functional_requirements/_.txt",
    "/keyword_lists/3_Performance_requirements/_.txt",
    "/keyword_lists/4_Logical_database_requirements/_.txt",
    "/keyword_lists/5_Design_constraints/_.txt",
    "/keyword_lists/6_1_1_Functional_compatibility/_.txt",
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
    path += paths[list_num-1]
    with open(path, 'w') as fp:
        fp.write(keyword)
    print("keyword addition completed!")
    return True

# add("パスワード", 1)
# add("パスワード", 61)

def delete(keyword, list_num):
    path = os.getcwd()
    path += paths[list_num-1]
    with open(path, 'r+') as fp:
        new = fp.readlines()
        fp.seek(0)
        for key in new:
            if keyword not in key:
                fp.write(key)
        fp.truncate()
    return True

# delete("キーワード", 1)
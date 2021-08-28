import os

paths = [
    "/password_lists/1_Interface_with_outside/_.txt",
    "/password_lists/2_Functional_requirements/_.txt",
    "/password_lists/3_Performance_requirements/_.txt",
    "/password_lists/4_Logical_database_requirements/_.txt",
    "/password_lists/5_Design_constraints/_.txt",
    "/password_lists/6_1_Functional_compatibility/_.txt",
    "/password_lists/6_2_Performance_efficiency/_.txt",
    "/password_lists/6_3_Compatibility/_.txt",
    "/password_lists/6_4_Usability/_.txt",
    "/password_lists/6_5_Reliability/_.txt",
    "/password_lists/6_6_Security/_.txt",
    "/password_lists/6_7_Maintainability/_.txt",
    "/password_lists/6_8_Portability/_.txt"
]

def add(password, list_num):
    path = os.getcwd()
    if list_num < 5: path += paths[list_num-1]
    # elif list_num > 60: path += paths[5][list_num%10-1]
    fp = open(path, mode='w')
    fp.write(password)
    fp.close()
    print("Password addition completed!")
    return True

# add("パスワード", 1)
# add("パスワード", 61)
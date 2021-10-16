import os

id_list = [
    "1_Interface_with_outside",
    "2_Functional_requirements",
    "3_Performance_requirements",
    "4_Logical_database_requirements",
    "5_Design_constraints",
    "6_1_1_Time_behaviour",
    "6_1_2_Resource_utilization",
    "6_2_Compatibility",
    "6_3_Usability",
    "6_4_Reliability",
    "6_5_Security",
    "6_6_Maintainability",
    "6_7_Portability"
]

def add(keyword, list_num):
    path = os.getcwd()
    path += "/keyword_lists/"
    path += id_list[list_num-1]
    path += "/_.txt"
    with open(path, 'w') as fp:
        fp.write(keyword)
    print("keyword addition completed!")
    return True

# add("パスワード", 1)
# add("パスワード", 61)

def delete(keyword, list_num):
    path = os.getcwd()
    path += "/keyword_lists/"
    path += id_list[list_num-1]
    path += "/_.txt"
    with open(path, 'r+') as fp:
        new = fp.readlines()
        fp.seek(0)
        for key in new:
            if keyword not in key:
                fp.write(key)
        fp.truncate()
    return True

# delete("キーワード", 1)
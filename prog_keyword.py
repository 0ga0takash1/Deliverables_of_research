import os
import array as ar

def add(keyword, list_num):
    path = os.getcwd()
    path += "/keyword_lists/"
    path += ar.id_list[list_num-1]
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
    path += ar.id_list[list_num-1]
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
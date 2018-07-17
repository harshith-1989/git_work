import os
import time


findings_dict = {}

def search_key_in_all_files_in_entire_folder(key,directory_path):
    occurrance_array = []
    for root,subdirs,files in os.walk(directory_path,topdown=True):
        for file in files:
            with open(f"{root}/{file}",'r',encoding='UTF-8',errors = 'ignore') as file_name:
                i = 0
                for line in file_name:
                     i = i + 1
                     if len(line) == 0: continue  # happens at end of file, then stop loop
                     if key in line:
                        occurrance_array.append({"FILE_NAME" : f"{root}/{file}", "LINE" : line, "LINE_NUMBER" : i})
    return occurrance_array
then = time.time()

keys = ("password", "user", "cert", "card", "password=", "password", "user", "cert", "card", "password=", "password", "user", "cert", "card", "password=", "password", "user", "cert", "card", "password=")
for key in list(set(keys)):
    findings_dict[key] = search_key_in_all_files_in_entire_folder(key,directory_path="output")


now = time.time()
print(findings_dict)
print((now - then))


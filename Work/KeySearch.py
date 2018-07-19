import os
import json

findings_dict = {}

ENCODING = 'UTF-8'
FILE_OPEN_MODE_READ = 'r'
STARTING_LINE = 1

#### changing to json as no additional data manipulation/transformation is required while reading for other languages, the result file name should be in format <app_name_sensititve_strings.json>
RESULT_JSON_FILE_LOCATION = "/tmp/tmp1.json"
#### Test data - this array will have to be a regex expression to match only the certain patterns of occurrances
keys = ("password", "user", "cert", "card", "password=", "password", "user", "cert", "card", "password=", "password", "user", "cert", "card", "password=", "password", "user", "cert", "card", "password=")


def search_key_in_all_files_in_entire_folder(key,directory_path):
    occurrance_array = []
    for root,subdirs,files in os.walk(directory_path,topdown=True):
        for file in files:
            with open(f"{root}/{file}",FILE_OPEN_MODE_READ,encoding=ENCODING,errors = 'ignore') as file_name:
                for line_number, line in enumerate(file_name, STARTING_LINE):
                     if len(line) == 0: continue  # happens at end of file, then stop loop
                     if key in line:
                        occurrance_array.append({"FILE_NAME" : f"{root}/{file}", "LINE" : line, "LINE_NUMBER" : line_number})
    return occurrance_array


def write_results_to_json(finding_results_json_file, dict):
    try:
        with open(finding_results_json_file, 'w') as results_file:
            json.dump(dict, results_file)
    except Exception as e:
        print("Error : {}".format(str(e)))


#Test usage :
for key in list(set(keys)):
    findings_dict[key] = search_key_in_all_files_in_entire_folder(key,directory_path="output")
    
#Test usage :
write_results_to_json(RESULT_JSON_FILE_LOCATION, findings_dict)


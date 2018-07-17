import threading
from queue import Queue
import time
import os

print_lock = threading.Lock()


#########################
#########################
#########################
#########################
def search_key_in_all_files_in_entire_folder(key,directory_path):
    global i
    for root,subdirs,files in os.walk(directory_path,topdown=True):
        for file in files:
            with open(f"{root}/{file}",'r',encoding='UTF-8',errors = 'ignore') as file_name:
                 for line in file_name:
                     if len(line) == 0: continue  # happens at end of file, then stop loop
                     if key in line:
                        i = i+1
                        print(f"{root}/{file} has {key}")
    print(f"{i} counts of {key}")

#########################
#########################
#########################
#########################
def process_queue():
    while True:
        key = search_key_queue.get() # at this point the get() function will not
                                      # return anything as the url_queue variable is empty, but waits for a fixed time-out period
                                      # for some value to be input to the url_queue.
                                      # beyond this time out period "queue empty" exception is raised'''
        search_key_in_all_files_in_entire_folder(key, directory_path="output")
        search_key_queue.task_done() # for every queue.get() method, a task_done()
                              # method must be called to indicate the completion of the task or in this case a thread

#########################
#########################
#########################
#########################
# create a queue-array object
search_key_queue = Queue()
keys = ("password", "user", "cert", "card", "password=", "password", "user", "cert", "card", "password=", "password", "user", "cert", "card", "password=", "password", "user", "cert", "card", "password=")

# iterate over the array
for i in range(len(keys)):
    thread = threading.Thread(target=process_queue)
    thread.daemon = True # the thread is background and exits as soon as the program exits if stuck at some point
    thread.start()

# after start all the above initialized threads are waiting in the process_queue function at url_queue.get()

for key in keys:
    search_key_queue.put(key) # as soon as the elements get input to the queue,
                               # the get() function in process_queue is called in all the threads as the iteration proceeds


start = time.time()
'''for url in url_list:
    get_url(url)'''


search_key_queue.join() # do not proceed till task_done from all the items in the queue is obtained
print("Execution time = {0:.5f}".format(time.time() - start))


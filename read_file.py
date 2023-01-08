#function read_file
#work read file 
#par no parymater
#return array of (time and task)
def read_file():
     saved_tasks=open("Tasks.txt","r")
     saved_tasks.close()
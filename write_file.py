#function write_file
#work to write data in file 
#return void 
#par (array time,array task)
# i am workin on this file
def write_file(date,data):
     d=[]
     i=len(d)
     d.insert(i,date)
     add_Task=open("Tasks.txt","a")
     add_Task.write(str(d[i]))
     add_Task.write("\t\t\t\t")
     add_Task.write(data)
     add_Task.write("\n")
     i=i+1
     if(i==7):
          i=0
     add_Task.close()      
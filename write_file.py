#function write_file
#work to write data in file 
#return void 
#par (array time,array task)
# i am workin on this file
def write_file(date,data):
     add_Task=open("Tasks.txt","a")
     add_Task.write("2023/")
     add_Task.write(str(date[1]))
     add_Task.write("/")
     add_Task.write(str(date[0]))
     add_Task.write("\t\t\t\t")
     add_Task.write(data)
     add_Task.write("\n")
     add_Task.close()
     
write_file([16,12],"study")
write_file([3,5],"meeting with company")
write_file([22,7],"sport")
#function input_time
#work input time and task from user
#return 1=>if ok do that ,0=>time is exsit ask them to befor edite it 
#par no parymater
#function use check_time,read_file,write_file .....I work in this
#function use check_time,read_file,write_file
import write_file
import check_time
def input_time():
     print("TIME : \n")
     time=input()
     if(check_time(int(time))==1):
         print("THE TIME IS EXIST ....please edit time ")
         return 0
     else:    
         print("YOUR TASK : \n")
         task=input()
         write_file(time,task)
         return 1

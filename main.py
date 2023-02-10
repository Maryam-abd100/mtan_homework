# this file is main file and all file is include and import here
# work:
# 1- load file
# 2- ask user if he need to show data or add data (if he want to show data show them and return to 2)
# 3- to add data make hime input time and data and check if time is exsit(if exsit ask him befor to edite them )
# 4- sort data by time 
# 5- edit file and return to 2 or 1
import read_file
import write_file
import show_file
import input_time
import check_time
def main ():
       mode=input("you need to : \n 1-show data \n 2-add data\n")
       if (mode=="1") :
             print("1")
             main()

       elif (mode=="2") :
             n=input_time.input_time()
             while (n==0):
                   n=input_time.input_time()   
             main()

       else :
             print("PLEASE ! ENTER \"1\" OR \"2\"")
             main()
main()             
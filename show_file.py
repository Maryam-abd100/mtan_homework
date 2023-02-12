#function show_file
#work to print file in nice way to user
#return void 
#par no parymater
#function use read_file


#************************************* 
# khalile is work in this file
#*************************************

import read_file
def show_file():
     e=[]
     e=read_file.read_file()
     for n in range (len(e)):
         print(e[n])
         if(n%2==0):
             print("\t\t")    

#*************************
# this edite without pull 
#*************************

#function check_time
#work to ckeck time if exsit befor or not 
#return 1=>if exit ,0=>if not
#par (time)=>time to ceck if exit
#function use read_file
import read_file
def check_time(time):
     e=[]    
     e=read_file()
     g=[]
     i=len(g)
     for n in range(len(e)) :
         if(n%2==0):
             g.insert(i,int(e[n]))
         i=i+1
     if(g.count(time)==0):
         return 0
     else :
         return 1

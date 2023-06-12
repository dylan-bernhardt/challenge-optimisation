import read_file
import algo_naif
import algo_max
import os
import sys
'''
for file in os.listdir("../instances/"):
    
    room = read_file.Room("../instances/"+file)
    instance = file[2:file.find(".")]
    l = algo_max.algo_max(room)
    print(f"{file} : {len(l)}")
    
    f = open("../res/res-"+file, "w")
    f.write("EQUIPE 22\n")
    f.write("INSTANCE " + instance + "\n")
    for surv in l :
        f.write(f"{surv[0]} {surv[1]}\n")
    f.close()
'''  

room = read_file.Room("../instances/gr6.txt")
instance = 6
l=algo_max.algo_max(room)
print(len(l))
f= open("../res/res-gr6.txt","w")
f.write("EQUIPE 22\n")
f.write("INSTANCE 6\n")
for surv in l :
    f.write(f"{surv[0]} {surv[1]}\n")
f.close()
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

room = read_file.Room("../instances/gr15.txt")
instance = 15
l = algo_max.algo_max(room)
print(f"{len(l)}")
f= open("../res/res-gr15.txt","w")
f.write("EQUIPE 22\n")
f.write("INSTANCE 15\n")
for surv in l :
    f.write(f"{surv[0]} {surv[1]}\n")
f.close()
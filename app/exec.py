import read_file
import algo_naif
import algo_max
import os

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
    
import algo_naif
import read_file



def algo_max(Room : read_file.Room) -> list :
    list_chercheurs = []
    nb_of_cible = room.get_nb_of_cible()
    while(nb_of_cible!=0):
        d = best_placement(Room)
        for case in d["cible"] :
            Room.cases[case.i][case.j].marked = 1
            nb_of_cible-=1
        list_chercheurs.append([d["x"], d["y"]])
    return list_chercheurs


def best_placement(Room : read_file.Room)->dict :
    d = {"x" : 0, "y": 0, "cible" : []}
    for i in range(Room.lignes) :
        for j in range(Room.colonnes) :
            l = algo_naif.couvre(Room, i, j)
            if len(l)>len(d["cible"]) :
                d["x"],d["y"],d["cible"] = i,j, l
    return d

room  = read_file.Room("../instances/gr1.txt")
print(algo_max(room))
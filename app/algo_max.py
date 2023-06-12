import algo_naif
import read_file



def algo_max(Room : read_file.Room) -> list :
    list_chercheurs = []
    nb_of_cible = Room.get_nb_of_cible()
    while(nb_of_cible!=0):
        d = best_placement(Room)
        for case in d["cible"] :
            Room.cases[case.i][case.j].marked = 1
            nb_of_cible-=1
        list_chercheurs.append([d["i"], d["j"]])
    return list_chercheurs


def best_placement(Room : read_file.Room)->dict :
    d = {"i" : 0, "j": 0, "cible" : []}
    for i in range(Room.lignes) :
        for j in range(Room.colonnes) :
            if Room.cases[i][j].type != "OBSTACLE" :
                l = algo_naif.couvre(Room, i, j)
                if len(l)>len(d["cible"]) :
                    d["i"],d["j"],d["cible"] = i,j, l
    return d



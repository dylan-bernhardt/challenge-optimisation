import read_file
import os

def algo_naif(Room : read_file.Room) -> list :
    list_chercheurs =[]
    for i in range(Room.lignes) :
        for j in range(Room.colonnes) :
            if Room.cases[i][j].type != "OBSTACLE":
                l = couvre(Room, i, j)
                if l :
                    for case in l:
                        Room.cases[case.i][case.j].marked = 1
                    list_chercheurs.append((i,j))
    return list_chercheurs


def couvre(Room : read_file.Room, i:int, j:int)->list :
    l = []
    jj=j
    ii = i
    while jj>= 0 and jj < Room.colonnes and Room.cases[ii][jj].type != "OBSTACLE":
        if Room.cases[ii][jj].type == "CIBLE" and Room.cases[ii][jj].marked == 0:
            l.append(Room.cases[ii][jj])
        jj-=1
    ii=i
    jj=j+1
    while jj>=0 and jj < Room.colonnes and Room.cases[ii][jj].type != "OBSTACLE" :
        if Room.cases[ii][jj].type == "CIBLE" and Room.cases[ii][jj].marked == 0:
            l.append(Room.cases[ii][jj])
        jj+=1
    ii=i+1
    jj=j
    while  ii>=0 and ii < Room.lignes and Room.cases[ii][jj].type != "OBSTACLE":
        if Room.cases[ii][jj].type == "CIBLE" and Room.cases[ii][jj].marked == 0:
            l.append(Room.cases[ii][jj])
        ii+=1
    ii=i-1
    jj=j
    while ii>=0 and ii < Room.lignes and Room.cases[ii][jj].type != "OBSTACLE" :
        if Room.cases[ii][jj].type == "CIBLE" and Room.cases[ii][jj].marked == 0:
            l.append(Room.cases[ii][jj])
        ii-=1
    return l

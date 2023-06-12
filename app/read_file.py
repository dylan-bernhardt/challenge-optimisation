class Case :
    def __init__(self, type_arg: str, x: int, y: int) -> None :
        self.x = x
        self.y = y
        self.marked = 0
        self.type=type_arg

class Room :
    def __init__(self, path :str)-> None:
        f = open(path)
        lines=f.readlines()
        self.lignes = int(lines[0].split()[1])
        self.colonnes = int(lines[1].split()[1])
        lines.pop(0)
        lines.pop(0)
        lines.pop(0)
        self.cases = [[Case("NORMAL", i, j) for j in range(self.colonnes)] for i in range(self.lignes)]
        for line in lines :
            _type, x, y = line.split()[0],int(line.split()[1]),int(line.split()[2])
            self.cases[x][y].type = _type
    def print_room(self)->None:
        for i in range(self.lignes) :
            print("\n")
            for j in range(self.colonnes): 
                print(self.cases[i][j].type, end=" ")
room = Room("../instances/gr1.txt")
room.print_room()

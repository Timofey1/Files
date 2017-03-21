class students:
    weight=0
    height=0
    name=""
    def __init__(self,w, h, n):
        self.name=n
        self.height=h
        self.weight=w


    def ChangrName(self,NewName):
        self.name=NewName

    def SwapStudents(stud1, stud2):
        stud1.name, stud2.name = stud2.name, stud1.name
        stud1.height, stud2.height = stud2.height, stud1.height
        stud1.weight, stud2.weight = stud2.weight, stud1.weight

    def StudInfa(self):
        print(self.name, self.height, self.weight)

        

m=students(1,1,"m")
t=students(2,2,"t")

dix = {m.name: m, t.name: t}
name=input()
dix[name].StudInfa()
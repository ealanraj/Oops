class parent:
    def __init__(self,father="surya",mother="jothika"):
        self.father=father
        self.mother=mother
    def __str__(self):
        return f"Father's name : {self.father}\nMother's name : {self.mother}"

family_1 = parent()
print(family_1)

class child(parent):
    def __init__(self,name,father="surya",mother="jothika"):
        super().__init__(father,mother)
        self.name=name
    def __str__(self):
        return f"Father of {self.name} is {self.father}\nMother of {self.name} is {self.mother}"

son = child("Dev")
print(son.name)
daughter = child("Diya")
print(daughter.name)
print(daughter)
print(son)

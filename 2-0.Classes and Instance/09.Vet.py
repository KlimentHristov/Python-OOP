class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if len(Vet.animals) == Vet.space:
            return "Not enough space"

        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        return f"{animal_name} registered in the clinic"


    def unregister_animal(self, animal_name):
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"


        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)

        return f"{animal_name} unregistered successfully"

    def info(self):
        animals_count = len(self.animals)
        space_left_in_clinic = Vet.space - len(Vet.animals)
        return f"{self.name} has {animals_count} animals. {space_left_in_clinic} space left in clinic"

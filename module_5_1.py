# Задача 'Developer - не только разработчик'

class House:
    def __init__(self, name_house, num_of_floors):
        self.name = name_house
        self.number_of_floors = int(num_of_floors)

    def go_to(self, new_floor):
        if new_floor not in range(1, self.number_of_floors + 1):
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
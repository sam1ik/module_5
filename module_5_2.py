# Задача 'Магические здания'

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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# h1.go_to(5)
# h2.go_to(10)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

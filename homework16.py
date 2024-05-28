class Buiding:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


Home = Buiding(45, "Хата")
other_home = Buiding(30, "Дом")
if Home == other_home:
    print('Одинаковые')
else:
    print('Разные')

Home = Buiding(45, "Хата")
other_home = Buiding(45, "Хата")
if Home == other_home:
    print('Одинаковые')
else:
    print('Разные')

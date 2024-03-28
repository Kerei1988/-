class Building:
    numberOfFloors = 0
    buildingType = ' '

    def __init__(self, floors: int, construction):
        self.numberOfFloors += floors
        self.buildingType += construction

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfloors, self.buildingType == other.buildingType


my_building = Building(10, 'Hotel')
son_building = Building(8, 'Otel')
print(my_building.numberOfFloors == son_building.numberOfFloors)
print(my_building.buildingType != son_building.buildingType)

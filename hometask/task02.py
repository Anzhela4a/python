class Road:
    _length: int
    _width: int
    weight = 25

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self, thickness):
        calc_mass = self._length*self._width*Road.weight*thickness
        print(f'{self._length}м * {self._width}м * {Road.weight}кг * {thickness}см = {calc_mass/1000}т')

road = Road(1020, 300)
road.mass(7)

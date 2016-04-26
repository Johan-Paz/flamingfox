from firefox.speeder import Speeder, SpeederClass
from firefox.component import Component, ComponentClass


if __name__ == "__main__":
    engines = ComponentClass('Engine', weight_func=lambda e: e.speed*e.acceleration, speed=int, acceleration=int)
    engine = Component('Fastest', engines, speed=23, acceleration=34)
    kind = SpeederClass('Klase Trash', 600, parts=[engine])
    speeder = Speeder('Cometa Rojo', kind)


    print speeder
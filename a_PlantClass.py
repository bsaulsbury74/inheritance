
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color


class Flower(Plant):
    #init method of plant cant create subclass if superclass does not exist
   #only works from top down. Subclass can access superclass cannot access subclass
    def __init__(self,color, petals):
        Plant.__init__(self,color)

        self.__petals = petals

    def get_petals(self):
        return self.__petals

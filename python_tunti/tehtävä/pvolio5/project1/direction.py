# import random
# from enum import Enum

# class Direction(Enum):
#     '''These constants represent the main directions that can be used to move on a map.'''
    #   #directions were thought as clock  
#     UP = 00
#     UP_RIGHT = 1
#     RIGHT = 3
#     DOWN_RIGHT = 4
#     DOWN = 6
#     DOWN_LEFT = 7
#     LEFT = 9
#     UP_LEFT = 10

#     @property
#     def x(self) -> int:
#         '''Returns x component of the direction as int.'''
#         x_pos = [self.DOWN_RIGHT,self.DOWN, self.DOWN_LEFT]
#         x_zero = []
#         x_neg = [self.UP_RIGHT,self.RIGHT,self.UP,self.UP_LEFT]

#         pass
    
#     @property
#     def y(self) -> int:
#         '''Returns y component of the direction as int.'''
#         pass

#     # @classmethod
#     # def get_values(cls) -> list['Direction']:
#     #     '''Returns a list of directions in a clockwise direction starting from up.'''
#     #     pass

#     @classmethod
#     def get_random(cls) -> 'Direction':
#         '''Return a random direction (not diagonals!).'''
#         pass


# ABOVE MY THINKING 

import random
from enum import Enum

class Direction(Enum):
    '''These constants represent the main directions that can be used to move on a map.'''
    UP = (0,-1)
    UP_RIGHT = (1,-1)
    RIGHT = (1, 0)
    DOWN_RIGHT = (1,1)
    DOWN = (0,1)
    DOWN_LEFT = (-1,1)
    LEFT = (-1,0)
    UP_LEFT = (-1-1)

    @property
    def x(self) -> int:
        '''Returns x component of the direction as int.'''
        return self.value[0]
    
    @property
    def y(self) -> int:
        '''Returns y component of the direction as int.'''
        return self.value[1]

    # @classmethod
    # def get_values(cls) -> list['Direction']:
    #     '''Returns a list of directions in a clockwise direction starting from up.'''
    #     pass

    @classmethod
    def get_random(cls) -> 'Direction':
        '''Return a random direction (not diagonals!).'''
        return random.choice((cls.UP, cls.RIGHT, cls.DOWN, cls.LEFT))

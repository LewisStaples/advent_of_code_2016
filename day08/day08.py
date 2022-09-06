import itertools
import copy

class Keypad:
    def __init__(self, width, length):
        self.pixel_set = set()
        self.WIDTH = width
        self.LENGTH = length
        
    def rect(self, x, y):
        the_points = itertools.product(list(range(1, x+1)), list(range(1, y+1)))
        for point in the_points:
            self.pixel_set.add((point[0],point[1]))
        
    def display(self):
        for b in range(1, self.LENGTH + 1):
            for a in range(1, self.WIDTH + 1):
                if (a,b) in self.pixel_set:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print()



def test_partA():
    test_keypad = Keypad(7, 3)
    test_keypad.display()
    test_keypad.rect(3,2)
    test_keypad.display()

test_partA()

            

    


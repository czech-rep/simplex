import numpy as np

class Interact():
    def __init__(self, num_dims):
        self.num_dims = num_dims

    def array_from_user(length):
        '''
        function agets element by element from user
        '''
        array = np.empty(length)
        i = 0
        while i < length:
            # try:
            x = input()
            array[i] = float(x)
            i += 1
            # except:
            #     print('incorrect input. try again')
        
        print(array)
        return array

if __name__ == "__main__":
    I = Interact(3)
    Interact.array_from_user(5)
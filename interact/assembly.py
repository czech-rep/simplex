import numpy as np

def assemble_matrix(case):
    '''
    accepts a np.array
    we insert ones matrix into, like this
    [a, b] -> [a, I, b]
    '''
    case = np.array(case)
    h, w = case.shape
    resources = np.expand_dims(case[:,-1], 1) # get last column

    result = np.concatenate( (case[:,:-1], np.diag(np.ones(h)), resources), 1)
    return result

# todo: sprawdzić czy wektory są liniowo niezależne


if __name__ == "__main__":
    a = np.array([[1, 2, 3, 5],
        [0, 5, 5, 5],
        [1, 9, 9, 8]
    ])
    b = [
        [8, 3, -5, 1, 4],
        [3, 1, -2, -1, 1],
    ]
    # print(a.shape)
    a = assemble_matrix(a)
    print(a)
    b = assemble_matrix(b)
    print(b)
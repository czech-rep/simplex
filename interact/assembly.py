import numpy as np

def assemble_matrix(case):
    '''
    accepts a np.array
    '''
    h, w = case.shape
    assert h == w - 1 
    resources = np.expand_dims(case[:,-1], 1)
    # print(resources, resources.shape)

    result = np.concatenate( (case[:,:-1], np.diag(np.ones(h)), resources), 1)
    print(result)

# sprawdzić czy wektory są liniowo niezależne


if __name__ == "__main__":
    a = np.array([[1, 2, 3, 5],
        [0, 5, 5, 5],
        [1, 9, 9, 8]
    ])
    # print(a.shape)
    assemble_matrix(a)
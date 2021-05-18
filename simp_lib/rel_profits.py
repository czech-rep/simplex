# given a matrix, lets calculate the relative profits:
import numpy as np

a = np.array([
    [1, 1, 1, 0]
    ,[2, 1, 0, 1]
])

objective = np.array([1, 1, 0, 0])
base_variables = [2, 3]
coeficients_in_objective = [ objective[index] for index in base_variables ]
# print(coeficients_in_objective)divider
resource = np.array([8, 10])

def get_rel_profits(array, coefs, objective):
    '''
    returns vector of relative profits:
    Z_objective - [ x_i * coef_objective ]
    '''
    # res = np.array([])
    # for i in range(len(a[0])):
    #     res = np.append(res, np.matmul(a[:,i], coefs) )
    res = [ np.matmul(a[:,i], coefs) for i in range(a.shape[1]) ]

    return objective - res

def compare(profits):
    '''
    choose index of the largest element
    if all are equal or less than zero, end operation
    '''
    return max(profits) if max(profits) > 0 else None

def current_maximum(coeficients_in_objective, resource):
    '''
    get current function maximum, based on current coefs 
    '''
    return np.matmul(coeficients_in_objective, resource)

def based_to_replace(resource, x_chosen):
    '''
    returns index of row
    which variable from base will be replaced
    decide by index of minimum positive coef: [resource] / [x_chosen]
    '''
    arr = np.divide( resource, x_chosen )
    return np.nanargmin(np.where(arr > 0, arr, np.nan))

def rebuild_matrix(a, i, j):
    '''
    so, we want to insert new variable to base
    we know index of variable and its place
    we will have to normalize row where variable is incoming with value from crossing
    and substract it from other rows to zero the column of incoming
    i - row, j - column
    '''
    crossing = a[i,j]
    a[i] = a[i] / crossing      # normalize row, now theres one in crossing

    for row in list(range(0, i)) + list( range(i+1, a.shape[0] )):
        multiplier = a[row][j]
        a[row] = a[row] - a[i] * multiplier  # substract row from others -> zeros in whole column

    return a

def test_rebuild_matrix():
    
    a = np.array([
        [1, 2, 3, 4, 5],
        [4, 3, 2, 4, 5],
        [1, .5, 1, -1, 2]
    ])
    print(rebuild_matrix(a, 1, 1))

def test_rebuild_matrix_2():
    
    a = np.array([
        [1, 2, 1, 1, 0, 0, 5],
        [1, 1, 1, 0, 1, 0, 4],
        [0, 1, 2, 0, 0, 1, 1]
    ])
    print(rebuild_matrix(a, 2, 1))

def test_profits_1():
    res = get_rel_profits(a, [1, 10], np.array([10, 1, 1, 1]) )
    assert (res == np.array([90, -1, -1, 0]))
    # print()


if __name__ == "__main__":
    # res = get_rel_profits(a, coeficients_in_objective, objective)
    
    a = np.array([
        [0, 0, 0, 1]
        ,[10, 0, 0, 0]
    ])
    # res = get_rel_profits(a, np.array([-1, -1]), np.array([0,0,0,0]) )
    # print(res)
    # print(np.transpose(resource))
    # print(compare([0,-1,5]))
    # print(compare([0,-1,0]))
    # print(current_maximum(coeficients_in_objective, resource))
    # print(based_to_replace([0, -1, 5], [1, 1, 2]))
    
    # test_rebuild_matrix()
    test_rebuild_matrix_2()
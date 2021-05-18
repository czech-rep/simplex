from simp_class import Simp
import numpy as np

def test_zeszyt():
    matrix = np.array([
        [1, 1, 0, 1, 8],
        [2, 1, 1, 0, 10]
    ])
    expr = [1, 1]

    problem = Simp(matrix, expr)
    res, val = problem.optimize(True)
    print(res, val)

    assert val == 8
    assert res == [2, 6]

def test_butchery():
    matrix = np.array([
        [1, 2, 1, 1, 0, 0, 5],
        [1, 1, 1, 0, 1, 0, 4],
        [0, 1, 2, 0, 0, 1, 1]
    ])
    expr = [1, 3, 2]

    problem = Simp(matrix, expr)
    res, val = problem.optimize()

    assert res == [3, 1, 0]
    assert val == 6
    
def test_sunelect():
    matrix = np.array([
        [2, 1, 1, 0, 0, 1000],
        [3, 3, 0, 1, 0, 2400],
        [1.5, 0, 0, 0, 1, 600]
    ])
    expr = [30, 20]

    problem = Simp(matrix, expr)
    res, val = problem.optimize()

    assert res == [200, 600]
    assert val == 18000

# def test_minimize():
#     matrix = np.array([
#         [1, 1, -1, 0, 3],
#         [1, 2, 0, -1, 4],
#     ])
#     expr = [2, 1]

#     problem = Simp(matrix, expr)
#     res, val = problem.optimize(True)

#     # assert res == [200, 600]
#     # assert val == 18000

def test_mimuw():
    matrix = np.array([
        [1, 2, -3, 1, 0, 0, 3],
        [2, 5, -5, 0, 1, 0, 7],
        [2, -3, -7, 0, 0, 1, 8]
    ])
    expr = [2, 6, -3]

    problem = Simp(matrix, expr)
    res, val = problem.optimize(True)
    # has no solution

    # assert res == [200, 600]
    # assert val == 18000

def test_mimuw_two_phrase():
    matrix = np.array([
        [8, 3, -5, 1, 1, 0, 4],
        [3, 1, -2, -1, 0, 1, 1],
    ])
    expr = [7, 2, -3, -1]

    problem = Simp(matrix, expr)
    res, val = problem.optimize(True)

    # assert res == [3, 0, 4, 0]
    # assert val == 9

if __name__ == "__main__":
    # test_zeszyt()
    # test_minimize()
    # test_mimuw()
    test_mimuw_two_phrase()
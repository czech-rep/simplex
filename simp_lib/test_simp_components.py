from simp_class import Simp
import numpy as np

def test_get_result():
    matrix = np.array([ [1], [2], [8], [10] ])
    num_vars = 4
    base = [4, 5, 0, 3]

    case = Simp(matrix, base, [], num_vars)
    res = case.get_result()
    print(res)

    assert res.tolist() == [8, 0, 0, 10]


if __name__ == "__main__":
    test_get_result()
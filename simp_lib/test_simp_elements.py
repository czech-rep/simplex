from simp_class import Simp
import numpy as np


def test_rebuild():
    matrix = np.array([
        [1, 2, 1, 1, 0, 0, 5],
        [1, 1, 1, 0, 1, 0, 4],
        [0, 1, 2, 0, 0, 1, 1]
    ])

    case = Simp(matrix, 0, 0, 0)
    case.rebuild_matrix(1, 1)

    print(case.a)



if __name__ == "__main__":
    test_rebuild()
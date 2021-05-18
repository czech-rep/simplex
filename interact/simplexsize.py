import sys
sys.path.append('D:\programming\zad3')                  # ważne

from read_file import extract_data
from assembly import assemble_matrix
from simp_lib.simp_class import Simp

def solve(case: dict):
    simplex_matrix = assemble_matrix(case['case'])
    expression = case['expr']

    simp = Simp(simplex_matrix, expression)
    res, val = simp.optimize(True)


if __name__ == "__main__":
    filename = input('give case data file. default: interact/case.json')
    case = extract_data(filename if filename else "interact/case.json")
    solve(case)
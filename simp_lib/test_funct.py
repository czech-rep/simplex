from rel_profits import *

a = np.array([
    [1, 0,0,10],
    [0,5,0,0]
])

def test_profits_1():
    res = get_rel_profits(a, np.array([-1, -1]), np.array([0,0,0,0]) )
    print(res)
    q = np.equal(res, np.array([1, 5, 0, 10]))
    print(q)
    assert np.all(q)
    # print()

def test_compare():
    a = [2, 998, 0, 999, -1]
    assert compare(a) == 999
    a = [0, -1, -999, -10, -1]
    assert compare(a) == None

def test_maximum():
    a, b = [1, 10], [1, 10]
    assert current_maximum(a, b) == 101
    a, b = [999, 0], [0, 500]
    assert current_maximum(a, b) == 0

def test_to_replace():
    res = based_to_replace([1, 50, -1], [1, 25, 1])
    assert res == 0
    res = based_to_replace([0, 8, 2], [2, 2, 2])
    assert res == 2
    
def test_rebuild():
    a = np.array([
        [2, 2, 2, 2],
        [1, 1, 1, 1],
        [10, 5, -8, 1]
    ])
    res = rebuild_matrix(a, 0, 0)
    assert 1 == res[0,0]
    assert 0 == res[1,0] == res[2,0]
    assert 1 == res[0,2]
    assert -5 == res[2,1]



if __name__ == "__main__":
    test_profits_1()
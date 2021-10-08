"""
Zac Foteff
10-5-2021
V.1

Test driven dev walkthrough -- Test file
Given an array A of integers, and an integer target k. Find all pairs x,y such that A[x] + A[y] == k, x != y
"""

import numpy as np
from numpy.core.fromnumeric import sort
from num_pairs import *
from random import randint

PAIRS_DATA = [
    {'test_array': np.array([]), 'test_target': 42, "test_result": 0},
    {'test_array': np.array([1]), 'test_target':42, "test_result": 0}, 
    {'test_array': np.array([1,2]), 'test_target': 3, "test_result": 1},
    {'test_array': np.array([2,2]), 'test_target': 4, "test_result": 1},
    {'test_array': np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2]), 'test_target': 7, 'test_result': 3},
    {'test_array': np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2]), 'test_target': 4, 'test_result': 3},
    {'test_array': np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2]), 'test_target': 0, 'test_result': 3},
    {'test_array': np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2]), 'test_target': -2, 'test_result': 1},
    {'test_array': np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2]), 'test_target': 47, 'test_result': 0}
]

BS_DATA = [
    {'test_array':  np.array([]), 'test_target': 42, 'test_result': 0},
    {'test_array':  np.array([0]), 'test_target': 42, 'test_result': 0},
    {'test_array':  np.array([0, 1]), 'test_target': 1, 'test_result': 1},
    {'test_array':  np.array([0, 1]), 'test_target': 2, 'test_result': 0},
    {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': 3, 'test_result': 1},
    {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': 4, 'test_result': 1},
    {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': -2, 'test_result': 2},
    {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': 1, 'test_result': 3},
    {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': 6, 'test_result': 0},
    {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': 0, 'test_result': 0}
]

LARGE_ARRAY_SIZE = 1000
RAND_INT_MIN = -100
RAND_INT_MAX = 100

def test_brute_search():
    #   Initialize log file
    brute_test_log = log_setup('brutetest', LOG_DIR+"brutetest.log")
    brute_test_log.info("Start brute search test\t|"+"-"*45)

    #   Initialize test results
    test_results = []
    return_results = []
    return_comps = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        brute_test_log.debug(f"Inside brute test suite\t| Test Arr: {test['test_array']} Target: {test['test_target']} Result: {test['test_result']}")
        num_pairs, num_comps = brute_search(test['test_array'], test['test_target'])
        brute_test_log.debug(f"Completed brute search\t| Num pairs: {num_pairs} Num comps: {num_comps}")
        return_results.append(num_pairs)
        return_comps.append(num_comps)
        test_results.append(test['test_result'])
    
    #   Log results and assert that the results are the same as the expected results
    brute_test_log.debug(f'Return Results: {return_results} Test results: {test_results} Comps: {return_comps}')
    brute_test_log.info("End brute force test\t|"+"-"*45)
    assert return_results == test_results
    

def test_binary_search():
    #   Initialize log file
    bs_test_log = log_setup('binarytest', LOG_DIR+"binarytest.log")
    bs_test_log.info("Start binary search test\t|"+"-"*45)

    #   Initialize test results
    test_results = []
    return_results = []
    return_comps = []

    for test in BS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        working_arr = sort(test['test_array'])
        bs_test_log.debug(f'Inside binarytest\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        bs_pairs, bs_comps = binary_search(working_arr, test['test_target'], 0, len(working_arr)-1)
        bs_test_log.debug(f'Number of pairs: {bs_pairs} Number of comps: {bs_comps}')
        return_results.append(bs_pairs)
        return_comps.append(bs_comps)
        test_results.append(test['test_result'])
    
    #   Log results and assert that the results are the same as the expected results
    bs_test_log.debug(f'Return Results: {return_results} Test results: {test_results} Comps: {return_comps}')
    bs_test_log.info("End binary search test\t|"+"-"*45)
    assert return_results == test_results


def test_sorted_search():
    #   Initialize log file
    sorted_test_log = log_setup('sortedtest', LOG_DIR+"sortedtest.log")
    sorted_test_log.info("Start sorted search test\t|"+"-"*45)

    #   Initialize test results
    test_results = []
    return_results = []
    return_comps = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        working_arr = sort(test['test_array'])
        sorted_test_log.debug(f'Inside Sorted search test\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        res_pairs, res_comps = sorted_search(working_arr, test['test_target'])
        return_results.append(res_pairs)
        return_comps.append(res_comps)
        test_results.append(test['test_result'])
    
    #   Log results and assert that the results are the same as the expected results
    sorted_test_log.debug(f'Return Results: {return_results} Test results: {test_results} Comps: {return_comps}')
    sorted_test_log.info("End Sorted search test\t|"+"-"*45)
    assert return_results == test_results


def test_large_numbers():
    #   Uncomment tests to increase scope. Can take up to 10 minutes to complete sorting with all algorithms
    large_test_logger = log_setup('largetest', LOG_DIR+"largetest.log")
    working_array = np.random.randint(RAND_INT_MIN, RAND_INT_MAX, LARGE_ARRAY_SIZE)
    target = randint(RAND_INT_MIN, RAND_INT_MAX)
    large_test_logger.debug(f'Large array test. Test array: {working_array}. Target: {target} ')
    brute_pairs, brute_comps = brute_search(working_array, target)
    sorted_pairs, sorted_comps = sorted_search(working_array, target)
    #pointer_pairs, pointer_comps = pointers_search(working_array, target)
    #hash_pairs, hash_comps = hash_search(working_array, target)
    large_test_logger.debug(f'Large test results\t| Brute: {brute_pairs} Sorted: {sorted_pairs}')
    assert brute_pairs == sorted_pairs# == pointer_pairs == hash_pairs
    assert brute_comps > sorted_comps# > pointer_comps > hash_comps


def test_pointers_search():
    #   Initialize log file
    pointer_test_log = log_setup('pointertest', LOG_DIR+"pointertest.log")
    pointer_test_log.info("Start Pointer search test\t|"+"-"*45)

    #   Initialize test results
    test_results = []
    return_results = []
    return_comps = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        working_arr = sort(test['test_array'])
        pointer_test_log.debug(f'Inside Pointer sort test\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        pnt_pairs, pnt_comps = pointers_search(working_arr, test['test_target'])
        return_results.append(pnt_pairs)
        return_comps.append(pnt_comps)
        test_results.append(test['test_result'])

    #   Log results and assert that the results are the same as the expected results
    pointer_test_log.debug(f'Return Results:\t\t\t| Algorithm Results: {return_results} Test results: {test_results} Comps: {return_comps}')
    pointer_test_log.info("End Pointer search test\t|"+"-"*45)
    assert return_results == test_results


def test_hash_search():
    #   Initialize log file
    hash_test_log = log_setup(f'hashtest', LOG_DIR+"hashtest.log")
    hash_test_log.info(f"Entering hashtest\t|"+"-"*45)

    #   Initialize test results
    test_results = []
    return_results = []
    return_comps = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        hash_test_log.debug(f'Inside Hash sort test\t| Test array: {test["test_array"]} Target: {test["test_target"]} Result: {test["test_result"]}')
        hash_pairs, hash_comps = pointers_search(test['test_array'], test['test_target'])
        return_results.append(hash_pairs)
        return_comps.append(hash_comps)
        test_results.append(test['test_result'])

    #   Log results and assert that the results are the same as the expected results
    hash_test_log.debug(f'Return Results:\t\t\t| Algorithm Results: {return_results} Test results: {test_results} Comps: {return_comps}')
    hash_test_log.info(f"End Hash search test\t|"+"-"*45)
    assert return_results == test_results
    

def test_brute_and_sorted():
    #   Initialize log file
    brutesorted_test_log = log_setup('brutesortedtest', LOG_DIR+"brutesortedtest.log")
    brutesorted_test_log.info("Entering brutesorted\t|"+"-"*45)

    #   Initialize test results
    brute_results = []
    sorted_results = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        bs_arr = sort(test['test_array'])
        brutesorted_test_log.debug(f'Inside brutesorted\t| Test array: {bs_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        brute_pairs, x = brute_search(test['test_array'], test['test_target'])
        brute_results.append(brute_pairs)
        bs_pairs, y = sorted_search(bs_arr, test['test_target'])
        sorted_results.append(bs_pairs)

    #   Sort results so that the order of the pairs is the same
    brute_results = sort(brute_results)
    sorted_results = sort(sorted_results)
    #   Log results and assert that the results are the same as the expected results
    brutesorted_test_log.debug(f'Brutesorted results| Brute: {sort(brute_results)} Sorted Search: {sort(sorted_results)}')
    assert brute_results.all() == sorted_results.all()
    brutesorted_test_log.info("End brutesorted\t|"+"-"*45)


def test_brute_and_pointers():
    #   Initialize log file
    brutepointers_test_log = log_setup('brutepointerstest', LOG_DIR+"brutepointerstest.log")
    brutepointers_test_log.info("Entering brutepointers\t|"+"-"*45)

    #   Initialize test results
    brute_results = []
    pnt_results = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        working_arr = sort(test['test_array'])
        brutepointers_test_log.debug(f'Inside brutepointers\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        
        brute_pairs, x = brute_search(test['test_array'], test['test_target'])
        brute_results.append(brute_pairs)
        pnt_pairs, y = pointers_search(working_arr, test['test_target'])
        pnt_results.append(pnt_pairs)

    #   Sort results so that the order of the pairs is the same
    brute_results = sort(brute_results)
    pnt_results = sort(pnt_results)
    #   Log results and assert that the algorithms output the same results
    brutepointers_test_log.debug(f'Brutepointers results| Brute: {sort(brute_results)} Pointers: {sort(pnt_results)}')
    assert brute_results.all() == pnt_results.all()
    brutepointers_test_log.info("End brutepointers\t|"+"-"*45)


def test_brute_and_hash():
    #   Initialize log file
    brutehash_test_log = log_setup('brutehashtest', LOG_DIR+"brutehashtest.log")
    brutehash_test_log.info("Entering brutehash\t|"+"-"*45)

    #   Initialize test results
    brute_results = []
    hash_results = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        working_arr = sort(test['test_array'])
        brutehash_test_log.debug(f'Inside brutehash\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        
        brute_pairs, x = brute_search(test['test_array'], test['test_target'])
        brute_results.append(brute_pairs)
        hash_pairs, y = pointers_search(working_arr, test['test_target'])
        hash_results.append(hash_pairs)

    #   Sort results so that the order of the pairs is the same
    brute_results = sort(brute_results)
    hash_results = sort(hash_results)
    #   Log results and assert that the algorithms output the same results
    brutehash_test_log.debug(f'Brutehash results| Brute: {sort(brute_results)} Hash: {sort(hash_results)}')
    assert brute_results.all() == hash_results.all()
    brutehash_test_log.info("End brutehash\t|"+"-"*45)


def test_sorted_and_pointers():
    #   Initialize log file
    sortedpointers_test_log = log_setup('sortedpointerstest', LOG_DIR+"sortedpointertest.log")
    sortedpointers_test_log.info("Entering sortedpointers\t|"+"-"*45)

    #   Initialize test results
    sorted_results = []
    pnt_results = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        working_arr = sort(test['test_array'])
        sortedpointers_test_log.debug(f'Inside sortedpointers\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        
        sorted_pairs, x = sorted_search(working_arr, test['test_target'])
        sorted_results.append(sorted_pairs)
        pnt_pairs, y = pointers_search(working_arr, test['test_target'])
        pnt_results.append(pnt_pairs)

    #   Sort results so that the order of the pairs is the same
    sorted_results = sort(sorted_results)
    pnt_results = sort(pnt_results)
    #   Log results and assert that the algorithms output the same results
    sortedpointers_test_log.debug(f'Sortedpointers results| Sorted: {sort(sorted_results)} Pointer: {sort(pnt_results)}')
    assert sorted_results.all() == pnt_results.all()
    sortedpointers_test_log.info("End sortedpointers\t|"+"-"*45)


def test_sorted_and_hash():
    #   Initialize log file
    sortedhash_test_log = log_setup('sortedhashtest', LOG_DIR+"sortedhashtest.log")
    sortedhash_test_log.info("Entering sortedhash\t|"+"-"*45)

    #   Initialize test results
    sorted_results = []
    hash_results = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        working_arr = sort(test['test_array'])
        sortedhash_test_log.debug(f'Inside sortedhash\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        sorted_pairs, x = sorted_search(working_arr, test['test_target'])
        sorted_results.append(sorted_pairs)
        hash_pairs, y = hash_search(working_arr, test['test_target'])
        hash_results.append(hash_pairs)

    #   Sort results so that the order of the pairs is the same
    sorted_results = sort(sorted_results)
    hash_results = sort(hash_results)
    #   Log results and assert that the algorithms output the same results
    sortedhash_test_log.debug(f'Sortedhash results| Sorted: {sort(sorted_results)} Hash: {sort(hash_results)}')
    assert sorted_results.all() == hash_results.all()
    sortedhash_test_log.info("End sortedhash\t|"+"-"*45)


def test_pointers_and_hash():
    #   Initialize log file
    pointerhash_test_log = log_setup('pointerhashtest', LOG_DIR+"pointerhashtest.log")
    pointerhash_test_log.info("Entering pointerhash\t|"+"-"*45)

    #   Initialize test results
    pointer_results = []
    hash_results = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        working_arr = sort(test['test_array'])
        pointerhash_test_log.debug(f'Inside sortedhash\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        sorted_pairs, x = sorted_search(working_arr, test['test_target'])
        pointer_results.append(sorted_pairs)
        hash_pairs, y = hash_search(working_arr, test['test_target'])
        hash_results.append(hash_pairs)

    #   Sort results so that the order of the pairs is the same
    pointer_results = sort(pointer_results)
    hash_results = sort(hash_results)
    #   Log results and assert that the algorithms output the same results
    pointerhash_test_log.debug(f'Sortedhash results| Pointer: {sort(pointer_results)} Hash: {sort(hash_results)}')
    assert pointer_results.all() == hash_results.all()
    pointerhash_test_log.info("End sortedhash\t|"+"-"*45)


def test_brute_sorted_and_pointers():
    #   Initialize log file
    tri_test1_log = log_setup('tritest', LOG_DIR+"tritest1.log")
    tri_test1_log.info("Entering Comprehensive Test 1\t|"+"-"*45)

    #   Initialize test results
    brute_results = []
    sorted_results = []
    pointer_results = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        working_arr = sort(test['test_array'])
        tri_test1_log.debug(f'Inside tritest\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]} ')

        brute_pairs, x = brute_search(test['test_array'], test["test_target"])
        sorted_pairs, y = sorted_search(working_arr, test["test_target"])
        pointer_pairs, z = pointers_search(working_arr, test['test_target'])
        brute_results.append(brute_pairs)
        sorted_results.append(sorted_pairs)
        pointer_results.append(pointer_pairs)

    #   Sort results so that the order of the pairs is the same
    brute_results = sort(brute_results)
    sorted_results = sort(sorted_results)
    pointer_results = sort(pointer_results)
    #   Log results and assert that the algorithms output the same results
    tri_test1_log.debug(f'Tritest1 results\t| Brute: {brute_results} Sorted: {sorted_results} Pointer: {pointer_results}')
    assert brute_results.all() == sorted_results.all() == pointer_results.all()


def test_sorted_pointers_and_hash():
    #   Initialize log file
    tri_test2_log = log_setup('tritest', LOG_DIR+"tritest2.log")
    tri_test2_log.info("Entering Comprehensive Test 2\t|"+"-"*45)

    #   Initialize test results
    hash_results = []
    sorted_results = []
    pointer_results = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        working_arr = sort(test['test_array'])
        tri_test2_log.debug(f'Inside tritest\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]} ')

        hash_pairs, x = hash_search(test['test_array'], test["test_target"])
        sorted_pairs, y = sorted_search(working_arr, test["test_target"])
        pointer_pairs, z = pointers_search(working_arr, test['test_target'])
        hash_results.append(hash_pairs)
        sorted_results.append(sorted_pairs)
        pointer_results.append(pointer_pairs)

    #   Sort results so that the order of the pairs is the same
    hash_results = sort(hash_results)
    sorted_results = sort(sorted_results)
    pointer_results = sort(pointer_results)
    #   Log results and assert that the algorithms output the same results
    tri_test2_log.debug(f'Tritest2 results\t| Hash: {hash_results} Sorted: {sorted_results} Pointer: {pointer_results}')
    assert hash_results.all() == sorted_results.all() == pointer_results.all()


def test_brute_sorted_pointers_and_hash():
    #   Initialize log file
    quad_test_log = log_setup('quadtest', LOG_DIR+"quadtest.log")
    quad_test_log.info("Entering Comprehensive Test\t|"+"-"*45)

    #   Initialize test results
    brute_results = []
    sorted_results = []
    pointer_results = []
    hash_results = []

    for test in PAIRS_DATA:
    #   Test each dataset with the algorithm and record the results
        #   Sort incoming test array
        working_arr = sort(test['test_array'])
        quad_test_log.debug(f'Inside tritest\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]} ')

        brute_pairs, x = brute_search(test['test_array'], test["test_target"])
        sorted_pairs, y = sorted_search(working_arr, test["test_target"])
        pointer_pairs, z = pointers_search(working_arr, test['test_target'])
        hash_pairs, a = hash_search(working_arr, test['test_target'])
        brute_results.append(brute_pairs)
        sorted_results.append(sorted_pairs)
        pointer_results.append(pointer_pairs)
        hash_results.append(hash_pairs)

    #   Sort results so that the order of the pairs is the same
    brute_results = sort(brute_results)
    sorted_results = sort(sorted_results)
    pointer_results = sort(pointer_results)
    hash_results = sort(hash_results)
    #   Log results and assert that the algorithms output the same results
    quad_test_log.debug(f'Tritest results\t| Brute: {brute_results} Sorted: {sorted_results} Pointer: {pointer_results} Hash: {hash_results}')
    assert brute_results.all() == sorted_results.all() == pointer_results.all() == hash_results.all()
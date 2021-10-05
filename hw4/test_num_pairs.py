import numpy as np
from numpy.core.fromnumeric import sort
from dan_solutions.tnum_pairs import BS_TEST_DATA
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
    {'test_array': np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2]), 'test_target': 47000, 'test_result': 0}
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

LARGE_ARR_SIZE = 1000
RAND_INT_MIN = -100000
RAND_INT_MAX = 100000

def test_brute_search():
    brute_test_log = log_setup('brutetest', LOG_DIR+"brute_test.log")
    brute_test_log.info("Entering brute force test\t|"+"-"*45)

    test_results = []
    return_results = []
    return_comps = []

    for test in PAIRS_DATA:
        brute_test_log.debug(f"Inside brute test suite\t| Test Arr: {test['test_array']} Target: {test['test_target']} Result: {test['test_result']}")
        num_pairs, num_comps = brute_search(test['test_array'], test['test_target'])
        brute_test_log.debug(f"Completed brute search\t| Num pairs: {num_pairs} Num comps: {num_comps}")
        return_results.append(num_pairs)
        return_comps.append(num_comps)
        test_results.append(test['test_result'])
    
    brute_test_log.debug(f'Return Results: {return_results} Test results: {test_results} Comps: {return_comps}')
    assert return_results == test_results
    brute_test_log.info("Leaving brute force test\t|"+"-"*45)
    

def test_bin_search():
    bs_test_log = log_setup('binarytest', LOG_DIR+"binarytest.log")
    bs_test_log.info("Entering binary sort test\t|"+"-"*45)

    test_results = []
    return_results = []
    return_comps = []

    for test in BS_DATA:
        working_arr = sort(test['test_array'])
        bs_test_log.debug(f'Inside binarytest\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        bs_pairs, bs_comps = binary_search(working_arr, test['test_target'])
        bs_test_log.debug(f'Number of pairs: {bs_pairs} Number of comps: {bs_comps}')
        return_results.append(bs_pairs)
        return_comps.append(bs_comps)
        test_results.append(test['test_result'])
    
    bs_test_log.debug(f'Return Results: {return_results} Test results: {test_results} Comps: {return_comps}')
    assert return_results == test_results
    bs_test_log.info("Leaving binary search test\t|"+"-"*45)

def test_pointers():
    pointer_test_log = log_setup('logtest', LOG_DIR+"combotest.log")
    pointer_test_log.info("Entering Pointer sort test\t|"+"-"*45)

    test_results = []
    return_results = []
    return_comps = []

    for test in PAIRS_DATA:
        working_arr = sort(test['test_array'])
        pointer_test_log.debug(f'Inside Pointer sort test\t| Test array: {working_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        pnt_pairs, pnt_comps = pointers_search(working_arr, test['test_target'])
        return_results.append(pnt_pairs)
        return_comps.append(pnt_comps)
        test_results.append(test['test_result'])

    pointer_test_log.debug(f'Return Results: {return_results} Test results: {test_results} Comps: {return_comps}')
    assert return_results == test_results
    pointer_test_log.info("Leaving Pointer search test\t|"+"-"*45)

#   Not working
def test_brute_and_bin():
    combo_test_log = log_setup('combotest', LOG_DIR+"combotest.log")
    combo_test_log.info("Entering combo test\t|"+"-"*45)

    brute_results = []
    bs_results = []

    for test in PAIRS_DATA:
        bs_arr = sort(test['test_array'])
        combo_test_log.debug(f'Inside combotest\t| Test array: {bs_arr} Target: {test["test_target"]} Result: {test["test_result"]}')
        
        brute_pairs, brute_comps = brute_search(test['test_array'], test['test_target'])
        brute_results.append(brute_pairs)
        bs_pairs, bs_comps = binary_search(bs_arr, test['test_target'])
        bs_results.append(bs_pairs)

    combo_test_log.debug(f'Combo test results\t| Brute: {brute_results} Bin. Search: {bs_results}')
    assert brute_results.sort() == bs_results.sort()
    combo_test_log.info("Leaving combo test\t|"+"-"*45)

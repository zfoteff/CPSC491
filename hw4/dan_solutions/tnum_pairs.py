import logging
import numpy as np
from numpy.core.fromnumeric import sort
import num_pairs
import math
from random import randint

PAIRS_TEST_DATA = [{'test_array':  np.array([1,2]), 'test_target': 3, 'test_result': 1},
                    {'test_array':  np.array([2,2]), 'test_target': 4, 'test_result': 1},
             {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2]), 'test_target': 7, 'test_result': 3},
             {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2]), 'test_target': 4, 'test_result': 3},
             {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2]), 'test_target': 0, 'test_result': 3},
             {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2]), 'test_target': -2, 'test_result': 1},
            ]

BS_TEST_DATA = [{'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': 3, 'test_result': 1},
                {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': 4, 'test_result': 1},
                {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': -2, 'test_result': 2},
                {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': 1, 'test_result': 3},
                {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': 6, 'test_result': 0},
                {'test_array':  np.array([-2, 3, 1, 5, -3, -1, 7, 4, 8, 2, 1, 5, -1, 1, 9, -2]), 'test_target': 0, 'test_result': 0},
               ]


TEST_3_ARRAY = np.array([-2, 0, -5, 12, 7, 3, 1, 2, -1, 4])
TEST_3_TARGET = 4
TEST_3_RESULT = 2
LARGE_ARRAY_SIZE = 1000
RAND_INT_LOW = -1000000
RAND_INT_HIGH =  1000000

def test_brute():
    brute_test_log = num_pairs.log_setup('brutetest', 'C:\\Users\\eshner\\OneDrive\\Gonzaga\\code\\logs\\brutetest.log', 'w')
    brute_test_log.info('Entering brute force test...')
    test_results = []
    return_results = []
    return_comps = []
    for test in PAIRS_TEST_DATA:        
        brute_test_log.debug(f'Inside test_brute. Test array: {test["test_array"]}. Target: {test["test_target"]} and Result: {test["test_result"]} ')
        res_pairs, num_comps = num_pairs.brute_search(test['test_array'], test['test_target'])
        brute_test_log.debug(f'Number of pairs: {res_pairs}, number of comps: {num_comps}')
        return_results.append(res_pairs)
        test_results.append(test['test_result'])
        return_comps.append(num_comps)
#        assert res_pairs == test['test_result']
    brute_test_log.info('Leaving brute force test...')
    assert return_results == test_results

def test_pointers():
    pointer_test_log = num_pairs.log_setup('pointertest', 'C:\\Users\\eshner\\OneDrive\\Gonzaga\\code\\logs\\pointertest.log', 'w')
    pointer_test_log.info('Entering pointers test...')
    test_results = []
    return_results = []
    return_comps = []
    for test in PAIRS_TEST_DATA:        
        working_array = np.sort(test['test_array'])
        pointer_test_log.debug(f'Inside test_pointer. Test array: {working_array} Target: {test["test_target"]} and Result: {test["test_result"]} ')
        res_pairs, num_comps = num_pairs.pointers_search(working_array, test['test_target'])
        pointer_test_log.debug(f'Number of pairs: {res_pairs}, number of comps: {num_comps}')
        return_results.append(res_pairs)
        test_results.append(test['test_result'])
        return_comps.append(num_comps)
#        assert res_pairs == test['test_result']
    pointer_test_log.info(f'Leaving pointer test. Num pairs is {res_pairs} num comps is {num_comps}')
    assert return_results == test_results

def test_sort():
    sorted_test_log = num_pairs.log_setup('sortedtest', 'C:\\Users\\eshner\\OneDrive\\Gonzaga\\code\\logs\\sortedtest.log', 'w')
    sorted_test_log.info('Entering sorted test...')
    test_results = []
    return_results = []
    return_comps = []
    for test in PAIRS_TEST_DATA:   
        working_array = np.sort(test['test_array'])     
        sorted_test_log.debug(f'Inside test_sorted. Test array: {test["test_array"]}. Target: {test["test_target"]} and Result: {test["test_result"]} ')
        res_pairs, num_comps = num_pairs.sorted_search(working_array, test['test_target'])
        sorted_test_log.debug(f'Inside test_sorted. Number of pairs: {res_pairs}, number of comps: {num_comps}')
        return_results.append(res_pairs)
        test_results.append(test['test_result'])
        return_comps.append(num_comps)
#        assert res_pairs == test['test_target']
#        assert num_comps < len(working_array) * math.log(len(working_array), 2)
    assert return_results == test_results
    sorted_test_log.debug(f'Return results: {return_results}. Test results: {test_results}. Comps: {return_comps}')
    sorted_test_log.info('Leaving sorted test...')

def test_large_array():
    working_array = np.random.randint(RAND_INT_LOW, RAND_INT_HIGH, LARGE_ARRAY_SIZE)
    target = randint(RAND_INT_LOW, RAND_INT_HIGH)
    large_test_logger = num_pairs.log_setup('largetest', 'C:\\Users\\eshner\\OneDrive\\Gonzaga\\code\\logs\\largetest.log', 'w')
    large_test_logger.debug(f'Inside large array test. Test array: {working_array}. Target: {target} ')
    brute_pairs, brute_comps = num_pairs.brute_search(working_array, target)
    sorted_pairs, sorted_comps = num_pairs.pointers_search(working_array, target)
    large_test_logger.debug(f'Inside large array test. Number of pairs: brute_pairs:{brute_pairs}, sorted_pairs:{sorted_pairs} brute comps: {brute_comps} sorted comps:{sorted_comps}')
    assert brute_pairs == sorted_pairs
    assert brute_comps > sorted_comps
    large_test_logger.info('Leaving large test...')

def test_binary():
    bs_test_log = num_pairs.log_setup('binarytest', 'C:\\Users\\eshner\\OneDrive\\Gonzaga\\code\\logs\\binarytest.log', 'w')
    bs_test_log.info('Entering binary search test...')
    test_results = []
    return_results = []
    return_comps = []
    for test in BS_TEST_DATA:
        working_array = np.sort(test['test_array'])
        bs_test_log.debug(f'Inside test_binary. Test array: {working_array}. Target: {test["test_target"]} and Result: {test["test_result"]} ')
        BS_pairs, BS_comps = num_pairs.binary_search(working_array, test['test_target'])
        bs_test_log.debug(f'Number of pairs: {BS_pairs}, number of comps: {BS_comps}')
        return_results.append(BS_pairs)
        test_results.append(test['test_result'])
        return_comps.append(BS_comps)
#        assert int(BS_pairs) == test['test_result']
#        assert BS_comps <= int(math.log(len(working_array), 2)) + 1
    bs_test_log.debug(f'Return results: {return_results}. Test results: {test_results}. Comps: {return_comps}')
    bs_test_log.info('Leaving brute force test...')
    assert return_results == test_results

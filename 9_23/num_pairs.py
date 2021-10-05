"""
Test driven dev walkthrough 
Given an array A of integers, and an integer target k. Find all pairs x,y such that A[x] + A[y] == k, x != y
"""

import numpy as np
import logging as log

LOG_DIR = "/home/csuser/Documents/cpsc491/hw4/logs/"

def log_setup(logger_name, log_file, mode='w'):
    """
    Logging setup and initialization
    """
    new_log = log.getLogger(logger_name)
    formatter = log.Formatter("%(asctime)s : %(message)s")
    file_handler = log.FileHandler(log_file, mode=mode)
    file_handler.setFormatter(formatter)
    stream_handler = log.StreamHandler()

    new_log.setLevel(log.DEBUG)
    new_log.addHandler(file_handler)
    new_log.addHandler(stream_handler)
    return new_log

def brute_search(src_arr, target) -> int:
    """
    Arrow give a expected return type for debugger
    Linear search: O(n^2) 
    """

    brute_log = log_setup('brute_force', LOG_DIR+"brute.log")
    brute_log.info(f'Entering Brute Search Function\t| Array is {src_arr} target is {target}')

    num_pairs = 0
    num_comps = 0
    outer_idx = 0
    arr_len = len(src_arr)
    
    while outer_idx < arr_len:
        inner_idx = outer_idx + 1
        while inner_idx < arr_len:
            num_comps += 1
            if src_arr[outer_idx] + src_arr[inner_idx] == target:
                num_pairs += 1
            inner_idx += 1
        outer_idx += 1
    brute_log.info(f'Terminating Brute Search Function\t| Array is {src_arr} target is {target}')
    return num_pairs, num_comps


"""

"""
def bin_sort_rec(src_arr, target) -> int:
    if len(src_arr) == 0:
        return -1
    
    mid = len(src_arr/2) - 1
    if src_arr[mid] == target:
        return target
    elif src_arr[mid] > target:
        bin_sort(src_arr[mid+1:-1], target) 
    elif src_arr[mid] < target:
        bin_sort(src_arr[0:mid], target)
    
    return -1


def sorted_rec_search(src_arr, target) -> int:
    """
    Binary search recursive
    """
    num_pairs = 0
    sorted_src = src_arr.sort()
    for each in src_arr:
        num_to_search = target - each
        r1 = np.searchsorted(src_arr, num_to_search, 'left')
        r2 = np.searchsorted(src_arr, num_to_search, 'right')
        print (str(r1) + str(r2))
        if each < r1 < r2:
            num_pairs += 1

    return num_pairs

def bin_sort(src_arr, target) -> int:
    """
    Binary search iterative
    """
    num_comps = 0
    num_pairs = 0
    start_idx = 0
    end_idx = len(src_arr)-1
    mid_idx = end_idx/2

    while ():
        mid_idx = start_idx + math.floor((end_idx-start_idx + 1)/2)
        bin_logger.info()

        if src_arr[mid_idx] == target:
            while src_arr[mid_idx -1] == target:
                mid_idx -= 1
            while mid_idx <= len(src_arr)-1 and min_idx >= 0 and src_arr[mid_idx] == target:
                num_pairs += 1
                mid_idx += 1
            break
        elif start_idx == end_idx:
            break
        elif src_arr[mid_idx] > target:
            end_idx = mid_idx - 1
        else:
            start_idx = mid_idx
    return num_pairs, num_comps
        
def pointers_search(src_arr, target):
    log_setup('pointers', '~/Documents/cpsc491/9_30')
    pointer_logger = logging.getLogger('pointers')
    working_arr = np.sort(src_arr)
    beg_ptr = 0
    end_ptr = len(working_arr) - 1
    num_pairs = 0
    num_comps = 0

    while beg_ptr > end_ptr:
        num_comps += 1
        if working_arr[beg_ptr] + working_arr[end_ptr] < target:
            beg_ptr += 1
        elif working_arr[beg_ptr] + working_arr[end_ptr] > target:
            end_ptr -= 1
        else:
            num_beg_dups = 1
            num_end_dups = 1
            while working_arr[beg_ptr+1] == working_arr[beg_ptr]:
                beg_ptr += 1
                num_beg_dups += 1
            while working_arr[end_ptr-1] == working_arr[end_ptr]:
                end_ptr -= 1
                num_dups += 1

            num_pairs += num_beg_dups * num_end_dups
            num_comps += num_end_dups + num_beg_dups
    return num_pairs
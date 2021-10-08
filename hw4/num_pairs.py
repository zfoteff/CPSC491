"""
Zac Foteff
10-5-2021
V.1

Test driven dev walkthrough -- Implementation file
Given an array A of integers, and an integer target k. Find all pairs x,y such that A[x] + A[y] == k, x != y
"""

import numpy as np
import logging as log
import math
import platform

_LOG_DIR_WIN = "C:/Users/Zac/GitHub/CPSC491/hw4/logs/"
_LOG_DIR_LIX = "/home/csuser/Documents/cpsc491/hw4/logs/"
LOG_DIR = _LOG_DIR_WIN

if platform.system() == 'Linux':
    LOG_DIR = _LOG_DIR_LIX

def log_setup(logger_name, log_file, mode='w'):
    """
    Logging setup and initialization
    """
    #   Initialize handlers
    new_log = log.getLogger(logger_name)
    formatter = log.Formatter("%(asctime)s : %(message)s")
    file_handler = log.FileHandler(log_file, mode=mode)
    file_handler.setFormatter(formatter)
    stream_handler = log.StreamHandler()

    #   create logging object with handlers
    new_log.setLevel(log.DEBUG)
    new_log.addHandler(file_handler)
    new_log.addHandler(stream_handler)
    return new_log


def brute_search(src_arr, target) -> int:
    """
    Brute force linear search: O(n^2) 
    Parameters:
        src_arr (np.Array()): An array of integers
        target (int): Target number combination to search for 
    Returns:
        num_pairs (int): Number of pairs that satisfy target number combination
        num_comps (int): Number of comparisons made over the course of the algorithm 
    """
    brute_log = log_setup('brute_force', LOG_DIR+"brute.log")
    brute_log.info(f"\tStart Brute Search Function\t| Array:{src_arr} Target:{str(target)} ")
    num_pairs = 0
    num_comps = 0
    outer_idx = 0
    arr_len = len(src_arr)
    
    while outer_idx < arr_len:
        inner_idx = outer_idx + 1
        brute_log.info(f"\tBrute search iter.\t| OI = {outer_idx} II = {inner_idx} SRC: {src_arr} ")
        while inner_idx < arr_len:
            num_comps += 1
            if src_arr[outer_idx] + src_arr[inner_idx] == target:
                num_pairs += 1
            inner_idx += 1
        outer_idx += 1

    brute_log.info(f"\tEnd Brute Search Function\t\t\t| Array: {src_arr} Target:{str(target)} ")
    return num_pairs, num_comps


def binary_search(src_arr, target, p_start, p_end) -> int:
    """
    Binary search implementation:
    Parameters:
        src_arr (np.Array()): An array of integers
        target (int): Target number combination to search for
        p_start (int): Start index
        p_end (int): End index
    Returns:
        num_pairs (int): Number of pairs that satisfy target number combination
        num_comps (int): Number of comparisons made over the course of the algorithm 
    """
    binary_log = log_setup('binary', LOG_DIR+"binary.log")
    binary_log.info(f"\tStart Binary Search Function\t| Array: {src_arr} Target:{str(target)} ")
    num_pairs = 0
    num_comps = 0
    begin_idx = p_start
    end_idx = p_end

    while begin_idx <= end_idx:
        mid_idx = begin_idx + math.floor((end_idx-begin_idx+1) / 2)
        binary_log.info(f"\tBinary search iter.\t| BI = {begin_idx} EI = {end_idx} MI = {mid_idx} src[MI]: {src_arr[mid_idx]} ")
        num_comps += 1
        if src_arr[mid_idx] == target:
            while mid_idx > begin_idx and src_arr[mid_idx-1] == target:
                #   Iterate through dups
                mid_idx -= 1
            while mid_idx <= len(src_arr) - 1 and mid_idx >= 0 and src_arr[mid_idx] == target:
                num_pairs += 1
                mid_idx += 1
            break
        elif begin_idx == end_idx:
            break
        elif src_arr[mid_idx] > target:
            end_idx = mid_idx - 1
        else:
            begin_idx = mid_idx
            
    binary_log.info(f'\tEnd Binary Search Function\t\t\t| Array: {src_arr} Target:{str(target)} ')
    return num_pairs, num_comps


def sorted_search(src_arr, target) -> int:
    """
    Sorted binary search implementation:
    Parameters:
        src_arr (np.Array()): An array of integers
        target (int): Target number combination to search for
    Returns:
        num_pairs (int): Number of pairs that satisfy target number combination
        num_comps (int): Number of comparisons made over the course of the algorithm 
    """
    sorted_log = log_setup('sorted', LOG_DIR+"sorted.log")
    working_arr = np.sort(src_arr)
    num_pairs = 0
    num_comps = 0
    size = len(working_arr)

    sorted_log.info(f"Start sorted search\t|")
    for cur_idx in range(0, size):
        cur_num = working_arr[cur_idx]
        sorted_log.info(f'Sorted search iter.\t| Array: {working_arr} Target: {target} Num: {cur_num} Goal: {target-cur_num}')
        #   Search for the number that would complete the target pair
        bin_res, bin_comps = binary_search(working_arr, target-cur_num, cur_idx+1, size-1)
        sorted_log.info(f"Result of search\t| Result: {bin_res} Comps: {bin_comps}")
        #   Tally results
        num_pairs += bin_res
        num_comps += bin_comps

    sorted_log.info(f"End sorted search\t| Num pairs: {num_pairs} Num comps: {num_comps}")
    return num_pairs, num_comps


def pointers_search(src_arr, target):
    """
    Pointer chasing search implementation:
    Parameters:
        src_arr (np.Array()): An array of integers
        target (int): Target number combination to search for
    Returns:
        num_pairs (int): Number of pairs that satisfy target number combination
        num_comps (int): Number of comparisons made over the course of the algorithm 
    """
    pointer_log = log_setup('pointers', LOG_DIR+"pointers.log")
    working_arr = np.sort(src_arr)
    beg_ptr = 0
    end_ptr = len(working_arr) - 1
    num_pairs = 0
    num_comps = 0

    pointer_log.info(f'\tStart pointers search\t| Array: {working_arr} Target:{str(target)} ')
    while beg_ptr < end_ptr:
        pointer_log.info(f"\tPointer search iter.\t| BP = {beg_ptr} EP = {end_ptr} SRC: {working_arr} ")
        num_comps += 1
        if working_arr[beg_ptr] + working_arr[end_ptr] < target:
            #   Move beginning ptr forward if the combination is less that target
            beg_ptr += 1
        elif working_arr[beg_ptr] + working_arr[end_ptr] > target:
            #   Move end ptr backward if the combination is less that target
            end_ptr -= 1
        else:
            beg_dups = 1
            end_dups = 1
            while beg_ptr < end_ptr-1 and working_arr[beg_ptr+1] == working_arr[beg_ptr]:
                #   Move beginning ptr forward if a duplicate exists ahead of it
                beg_ptr += 1
                beg_dups += 1
            while end_ptr > beg_ptr + 1 and working_arr[end_ptr-1] == working_arr[end_ptr]:
                #   Move end ptr backwards if a duplicate exists behind of it
                end_ptr -= 1
                end_dups += 1

            #   Tally results and move pointers
            num_pairs += beg_dups * end_dups
            num_comps += beg_dups + end_dups
            beg_ptr += 1
            end_ptr -= 1
    
    pointer_log.info(f'\tEnd pointers search\t\t\t| Num pairs: {num_pairs} Comps: {num_comps} ')
    return num_pairs, num_comps


def hash_search(src_arr, target):
    """
    Hash search implementation:
    Parameters:
        src_arr (np.Array()): An array of integers
        target (int): Target number combination to search for
    Returns:
        num_pairs (int): Number of pairs that satisfy target number combination
        num_comps (int): Number of comparisons made over the course of the algorithm 
    """
    hash_log = log_setup('hash', LOG_DIR+"hash.log")
    hash_log.info(f"Start hash search\t|")
    hash = {}
    num_pairs = 0
    num_comps = 0

    for each in src_arr:
    #   Hash each element in the source and the # of dups into a dictionary
        if each not in hash:
            hash[each] = 1
        else:
            hash[each] = hash[each] + 1

    for each in hash:
    #   Examine each hash, if the expected pair exists, multiply the # of dups in num1 & the # of dups in num2
        hash_log.info(f"\tHash search iter.\t| SRC: {src_arr} Target: {target} ")
        new_target = target-each
        if new_target in hash:
            num_pairs += hash[new_target] * hash[each]
        num_comps += 1

    hash_log.info(f'\tEnd hash search\t\t\t| Num pairs: {num_pairs} Comps: {num_comps} ')
    return num_pairs, num_comps
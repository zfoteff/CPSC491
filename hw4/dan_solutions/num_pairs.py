from numpy import inner
import numpy as np
import numpy.ma as ma
import math
import logging

def log_setup(logger_name, log_file, mode='w'):
    new_log = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    file_handler = logging.FileHandler(log_file, mode=mode)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    new_log.setLevel(logging.DEBUG)
    new_log.addHandler(file_handler)
    new_log.addHandler(stream_handler)
    return new_log

def brute_search(src_array, target):
    brute_log = log_setup('brute', 'C:\\Users\\eshner\\OneDrive\\Gonzaga\\code\\logs\\brute.log', 'w')
    brute_log.info(f'Entering brute search function. Array is {src_array}, target is {target}')
    num_pairs = 0
    outer_index = 0
    num_comps = 0
    array_len = len(src_array)
    while outer_index < array_len:
        inner_index = outer_index + 1
        while inner_index < array_len:
            num_comps += 1
            if src_array[outer_index] + src_array[inner_index] == target:
                num_pairs += 1
            inner_index += 1
        outer_index += 1
    brute_log.info(f'Leaving brute search function. num pairs is {num_pairs}, num comps is {num_comps}')
    return num_pairs, num_comps

def binary_search(src_array, target, p_begin_index, p_end_index):
    binary_logger = log_setup('binary', 'C:\\Users\\eshner\\OneDrive\\Gonzaga\\code\\logs\\binary.log', 'w')
    binary_logger.info(f'inside binary search, array is: {src_array}, target is {target}, beg_index is {p_begin_index} end index is {p_end_index}')
    begin_index = p_begin_index
    end_index = p_end_index
    num_comps = 0
    num_found = 0
    while begin_index <= end_index:
        mid_index = begin_index + math.floor((end_index - begin_index + 1) / 2)
        binary_logger.info(f'inside binary search, BI = {begin_index}, EI = {end_index}, MI = {mid_index}, src[MI]: {src_array[mid_index]}')   
        num_comps += 1
        if src_array[mid_index] == target:
            while mid_index > begin_index and src_array[mid_index - 1] == target:
                mid_index -= 1
            while mid_index <= len(src_array) - 1 and mid_index >= 0 and src_array[mid_index] == target :
                num_found += 1
                mid_index += 1
            break
        elif begin_index == end_index:
            break
        elif src_array[mid_index] > target:
            end_index = mid_index - 1
        else:
            begin_index = mid_index
    binary_logger.info(f'Leaving binary search, num found is: {num_found}, num comps is {num_comps}')
    return num_found, num_comps

def sorted_search(src_array, target):
    sorted_logger = log_setup('sorted', 'C:\\Users\\eshner\\OneDrive\\Gonzaga\\code\\logs\\sorted.log', 'w')
    working_array = np.sort(src_array)
    sorted_logger.info(f'inside sorted search, sorted array is: {working_array}, target is {target}')   
    num_pairs = 0
    num_comps = 0
    array_size = len(working_array)
    for cur_index in range(0, array_size):
        cur_num = working_array[cur_index]
        sorted_logger.info(f'inside sorted pairs func, src array is {working_array} target is {target} num is {cur_num}, searching for {target - cur_num}, num_pairs is {num_pairs}')
        binary_res, search_comps = binary_search(working_array, target - cur_num, cur_index + 1, array_size - 1)
        sorted_logger.info(f'inside sorted pairs, search result is {binary_res} and number of comps is {num_comps}')
        num_pairs += binary_res
        num_comps += search_comps
    sorted_logger.info(f'Leaving sorted search, num pairs is {num_pairs}, num comps is {num_comps}')   
    return num_pairs, num_comps

def pointers_search(src_array, target):
    pointers_logger = log_setup('pointers', 'C:\\Users\\eshner\\OneDrive\\Gonzaga\\code\\logs\\pointers.log', 'w')
    working_array = np.sort(src_array)
    pointers_logger.info(f'inside pointers search, sorted array is: {working_array}, target is {target}')   
    num_pairs = 0
    num_comps = 0
    beg_ptr = 0
    end_ptr = len(working_array) - 1
    while beg_ptr < end_ptr:
        num_comps += 1
        if working_array[beg_ptr] + working_array[end_ptr] < target:
            beg_ptr += 1
        elif working_array[beg_ptr] + working_array[end_ptr] > target:
            end_ptr -= 1
        else:
            beg_dups = 1
            end_dups = 1
            while beg_ptr < end_ptr - 1 and working_array[beg_ptr + 1] == working_array[beg_ptr]:
                beg_ptr += 1
                beg_dups += 1
            while end_ptr > beg_ptr + 1 and working_array[end_ptr - 1] == working_array[end_ptr]:
                end_ptr -= 1
                end_dups += 1
            num_pairs += beg_dups * end_dups
            num_comps += beg_dups + end_dups
            beg_ptr += 1
            end_ptr -= 1
    pointers_logger.info(f'Leaving pointers search, num pairs is: {num_pairs}, num comps is {num_comps}')   
    return num_pairs, num_comps

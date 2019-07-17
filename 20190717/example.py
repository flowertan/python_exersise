# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/7/17 23:36
# @file    : example.py
# @desc    : 多进程与非多进程运行时间比较
#

import time
from multiprocessing import Process, Queue


def not_process():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time.time()
    for number in number_list:
        total += number
    print(total)
    end = time.time()
    print('not process Execution time: %.3fs' % (end - start))


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total = number + total

    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 分成8个进程取计算，不考虑列表切片时间，单从计算时间上进行比较
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    start = time.time()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time.time()
    print('Execution time: ', (end - start), 's', sep='')
    not_process()


if __name__ == '__main__':
    main()

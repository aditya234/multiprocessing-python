# import multiprocessing
#
# score = multiprocessing.Value('i', 0)
#
# if __name__ == '__main__':
#     result = multiprocessing.Array('i', 4)
#     mylist = [1, 2, 3, 4]
#     p1 = multiprocessing.Process(target=square_list, args=(mylist, result))
#     p1.start()
#     p1.join()
#     print(f"Result in parent {square_sum.value}")

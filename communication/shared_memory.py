import multiprocessing


def square_list(mylist, result, square_sum):
    for idx, num in enumerate(mylist):
        result[idx] = num * num
    square_sum.value = sum(result)
    print(f"RESULT LIST HERE - {square_sum.value}")


if __name__ == '__main__':
    result = multiprocessing.Array('i', 4)
    square_sum = multiprocessing.Value('i')
    mylist = [1, 2, 3, 4]
    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))
    p1.start()
    p1.join()
    print(f"Result in parent {square_sum.value}")

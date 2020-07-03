import multiprocessing


def square_list(mylist, q):
    for num in mylist:
        q.put(num * num)


def print_list(q):
    while not q.empty():
        print(q.get())


if __name__ == '__main__':
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=square_list, args=([1, 2, 3, 4], q))
    p2 = multiprocessing.Process(target=print_list, args=(q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

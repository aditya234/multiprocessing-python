import multiprocessing


def withdraw(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


def deposite(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def perform_transactions():
    balance = multiprocessing.Value('i', 100)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=withdraw, args=(balance, lock))
    p2 = multiprocessing.Process(target=deposite, args=(balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Final balance {balance.value}")


if __name__ == '__main__':
    for _ in range(10):
        perform_transactions()

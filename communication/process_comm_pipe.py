import multiprocessing
import time

msgs = ["Hey", "Hello", "How r u?", "END"]


def send_msgs(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        time.sleep(2)
    conn.close()


def recieve_msgs(conn):
    while 1:
        msg = conn.recv()
        if (msg == "END"):
            break
        print(msg)


if __name__ == '__main__':
    conn_one, conn_two = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=send_msgs, args=(conn_one, msgs))
    p2 = multiprocessing.Process(target=recieve_msgs, args=(conn_two,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

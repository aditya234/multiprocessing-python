import multiprocessing


def print_records(records):
    for record in records:
        print(f"Name: {record[0]} and Score: {record[1]}")


def insert_record(record, records):
    records.append(record)
    print("New record added!")


if __name__ == '__main__':
    # server process
    with multiprocessing.Manager() as manager:
        records = manager.list([('Sam', 10), ('Adam', 11), ('Cris', 9)])
        record = ('New', 5)

        p1 = multiprocessing.Process(target=insert_record, args=(record, records))
        p2 = multiprocessing.Process(target=print_records, args=(records,))

        p1.start()
        p1.join()

        p2.start()
        p2.join()

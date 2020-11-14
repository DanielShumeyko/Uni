import multiprocessing as mp
import time 

to_replace = 'az'
replace_with = '{[]}'


def customer_wait(lock, start_time, seats_open, id, waiting_list):
    lock.acquire()
    print(f'Customer {id} is waiting outside.')
    lock.release()

    while True:
        lock.acquire()
        if seats_open.value >= 1:
            with seats_open.get_lock():
                seats_open.value -= 1
            waiting_list.insert(0, id)
            lock.release()
            break
        lock.release()
        #time.sleep(1)
    lock.acquire()
    print(f'Customer {id} is now waiting inside.There are {seats_open.value} open seats. Waiting list: {waiting_list}')
    lock.release()

def barber(lock, start_time, seats_open, customers_left, waiting_list, speed):
    print(f'Barber started his shift. {customers_left.value} customers to serve.')
    while customers_left.value > 0:
        lock.acquire()
        if len(waiting_list) > 0:
            serve_id = waiting_list[-1]
            print(f'Serving customer {serve_id}')
            waiting_list.pop()
            seats_open.value += 1
            customers_left.value -=1
            lock.release()
            time.sleep(speed)
            lock.acquire()
            print(f'Finished serving customer {serve_id}.')
            lock.release()
        else:
            print('Barber waiting for customer.')
            lock.release()
    print('BARBER HAS FINISHED WORKING')


def main():
    start = time.perf_counter()
    OPEN_SEATS = 5
    BARBER_SPEED = 0.2
    NUMBER_OF_CUSTOMERS = 100
    processes = []

    lock = mp.Lock()
    manager = mp.Manager()
    seats_open = mp.Value("i", OPEN_SEATS)
    customers_left = manager.Value("i", NUMBER_OF_CUSTOMERS)
    waiting_list = manager.list()

    p = mp.Process(target=barber, args = [lock, time.time(), seats_open, customers_left, waiting_list, BARBER_SPEED])
    p.start()
    processes.append(p)

    for i in range(1, NUMBER_OF_CUSTOMERS+1):
        p = mp.Process(target=customer_wait, args = [lock, time.time(), seats_open, i, waiting_list])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 4)} second(s)')

if __name__ == "__main__":
    main()
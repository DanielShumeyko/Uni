import threading
import time 

start = time.perf_counter()
txtsmpl = open('C:\\dev\\OS\\dummy.txt', 'r').read()
threads_num = 5
to_replace = 'ap'
replace_with = '{[]}'
lock = threading.Semaphore(value=1)

def process_txt(start_time, inp_text):
    txt = list(inp_text)
    for i, letter in enumerate(txt):
        if letter in to_replace:
            txt[i] = replace_with
    txt = ''.join(txt)
    lock.acquire()
    print(txt + '\n')
    print('Ran for ' + str(round(time.time() - start_time, 4)) + ' second(s)...\n')
    lock.release()


threads = []
for _ in range(threads_num):
    t = threading.Thread(target=process_txt, args = [time.time(), txtsmpl])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()



finish = time.perf_counter()
print(f'Finished in {round(finish-start, 4)} second(s)')
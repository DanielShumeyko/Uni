import threading
import time 
import sys

start = time.perf_counter()
txtsmpl = open('C:\\dev\\OS\\lab2\\dummy.txt', 'r').read()
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    threads_num = int(sys.argv[1])        
else:
    threads_num = 5

to_replace = 'ap'
replace_with = '{[]}'
lock = threading.Semaphore(value=1)

def process_txt(start_time, inp_text, i):
    txt = list(inp_text)
    for k, letter in enumerate(txt):
        if letter in to_replace:
            txt[k] = replace_with
    txt = ''.join(txt)
    lock.acquire()
    filename = 'file_' + str(i+1) + '.txt'
    with open(filename, 'w') as f:
        f.write(txt + '\n')
        f.write(f'Ran for {round(time.time() - start_time, 4)} second(S)... \n')
        f.close()
    lock.release()


threads = []
for i in range(threads_num):
    t = threading.Thread(target=process_txt, args = [time.time(), txtsmpl, i])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()



finish = time.perf_counter()
print(f'Finished in {round(finish-start, 4)} second(s)')
import multiprocessing as mp
import time 
import sys

to_replace = 'az'
replace_with = '{[]}'


def process_txt(start_time, inp_text, i, lock):
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

def main():
    start = time.perf_counter()
    txtsmpl = open('C:\\dev\\OS\\lab2\\dummy.txt', 'r').read()
    lock = mp.Lock()
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        processes_num = int(sys.argv[1])        
    else:
        processes_num = 5
    processes = []
    for i in range(processes_num):
        p = mp.Process(target=process_txt, args = [time.time(), txtsmpl, i, lock])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 4)} second(s)')

if __name__ == "__main__":
    main()
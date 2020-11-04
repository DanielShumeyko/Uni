import multiprocessing as mp
import time 

to_replace = 'az'
replace_with = '{[]}'


def process_txt(start_time, inp_text):
    txt = list(inp_text)
    for i, letter in enumerate(txt):
        if letter in to_replace:
            txt[i] = replace_with
    txt = ''.join(txt)
    print(txt + '\n')
    print('Ran for ' + str(round(time.time() - start_time, 4)) + ' second(s)...\n')

def main():
    start = time.perf_counter()
    txtsmpl = open('C:\\dev\\OS\\dummy.txt', 'r').read()
    processes_num = 5
    processes = []
    for _ in range(processes_num):
        p = mp.Process(target=process_txt, args = [time.time(), txtsmpl])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 4)} second(s)')

if __name__ == "__main__":
    main()
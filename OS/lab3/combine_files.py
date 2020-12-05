import sys

r1 = int(sys.argv[1])
r2 = int(sys.argv[2])
t1 = int(sys.argv[3])
t2 = int(sys.argv[4])
N1 = int(sys.argv[5])
N2 = int(sys.argv[6])

basedir = 'C:\dev\OS\lab3\VirtualDisk' 
input1 = basedir
input2 = basedir
output1 = basedir
output2 = basedir
print(type(input1))
print(input1)
print(r1)
print(type(r1))
print(f'\{r1}')
print(type(f'\{r1}'))

#getting input locations for both processes and threads (1 and 2)
for i in range(1,r1+1):
    input1 += f'\{i}'
input1 += '\\'

for i in range(1,r2+1):
    input2 += f'\{i}'
input2 += '\\'

# getting locations of each file to combine, for both processes and threads (1 and 2)
filenames1 = []
filenames2 = []

for i in range(1, N1+1):
    filenames1.append(input1 + f'file_{i}.txt')

for i in range(1, N2+1):
    filenames2.append(input2 + f'file_{i}.txt')


#getting output locations for both processes and threads (1 and 2)
for i in range(1,r1+t1+1):
    output1 += f'\{i}'
output1 += '\\'

for i in range(1,r2+t2+1):
    output2 += f'\{i}'
output2 += '\\'

with open(output1 + 'processes_joined.txt', 'w') as outp:
    for filename in filenames1:
        with open(filename) as f:
            for line in f:
                outp.write(line)


with open(output2 + 'threads_joined.txt', 'w') as outp:
    for filename in filenames2:
        with open(filename) as f:
            for line in f:
                outp.write(line)

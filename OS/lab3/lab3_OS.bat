 @ECHO ON
set /A R = 15
set /A N1 = 53
set /A N2 = 54
set /A r1 = 13
set /A r2 = 15
set /A a1 = 12
set /A a2 = 14
set /A a3 = 8
set /A a4 = 9 
set /A t1 = - 12
set /A t2 = - 11


MD C:\dev\OS\lab3\VirtualDisk
CD C:\dev\OS\lab3\VirtualDisk

ECHO "CREATING FOLDERS "
for /l %%i in (1, 1, %R%) DO (
    MD "%%~i"
    CD "%%~i"
)

ECHO "RUNNING LAB 2 PROCESSES AT LEVEL r1"
set /A levels1 = %R% - %r1%
for /l %%i in (1, 1, %levels1%) do (
    CD ".."
)
C:\Users\Daniel\Anaconda3\python.exe C:\dev\OS\lab2\lab2_processes.py %N1%

set "r1_loc=%cd%"


ECHO "RUNNING LAB 2 THREADS AT LEVEL r2"
CD C:\dev\OS\lab3\VirtualDisk
for /l %%i in (1, 1, %r2%) DO (
    CD "%%~i"
)

C:\Users\Daniel\Anaconda3\python.exe C:\dev\OS\lab2\lab2_threads.py %N2%

set "r2_loc=%cd%"

ECHO "ARCHIVING PROCESS FILES INTO ARCHIVE AT LEVEL a1"
CD C:\dev\OS\lab3\VirtualDisk
for /l %%i in (1, 1, %a1%) DO (
    CD "%%~i"
)
set "a1_loc=%cd%\proc.rar"
CD %r1_loc%
"C:\Program Files\WinRAR\Rar.exe" a  %a1_loc% *.txt

ECHO "ARCHIVING THREAD FILES INTO ARCHIVE AT LEVEL a2"
CD C:\dev\OS\lab3\VirtualDisk
for /l %%i in (1, 1, %a2%) DO (
    CD "%%~i"
)
set "a2_loc=%cd%\thrd.rar"
CD %r2_loc%
"C:\Program Files\WinRAR\Rar.exe" a %a2_loc% *.txt


ECHO "COMBINING TEXT FILES FOR PROCESSES\THREADS INTO 1 AND SORTING"
C:\Users\Daniel\Anaconda3\python.exe C:\dev\OS\lab3\combine_files.py %r1% %r2% %t1% %t2% %N1% %N2%

CD C:\dev\OS\lab3\VirtualDisk
set /A levels2 = %r1% + %t1%
for /l %%i in (1, 1, %levels2%) DO (
    CD "%%~i"
)
sort processes_joined.txt /o sorted_processes.txt
del /f processes_joined.txt
set "sorted_loc_proc=%cd%"

CD C:\dev\OS\lab3\VirtualDisk
set /A levels3 = %r2% + %t2%
for /l %%i in (1, 1, %levels3%) DO (
    CD "%%~i"
)
sort threads_joined.txt /o sorted_threads.txt
del /f threads_joined.txt
set "sorted_loc_thrd=%cd%"

ECHO "ADDING SORTED PROCESS FILE TO ARCHIVE"
CD %sorted_loc_proc%
"C:\Program Files\WinRAR\Rar.exe" a %a1_loc% "sorted_processes.txt"

ECHO "ADDING SORTED THREAD FILE TO ARCHIVE"
CD %sorted_loc_thrd%
"C:\Program Files\WinRAR\Rar.exe" a %a2_loc% "sorted_threads.txt"

ECHO "UNPACKING PROCESS ARCHIVE AT a3"
CD C:\dev\OS\lab3\VirtualDisk
for /l %%i in (1, 1, %a3%) DO (
    CD "%%~i"
)
"C:\Program Files\WinRAR\UnRAR.exe" e %a1_loc%

ECHO "UNPACKING THREAD ARCHIVE AT a4"
CD C:\dev\OS\lab3\VirtualDisk
for /l %%i in (1, 1, %a4%) DO (
    CD "%%~i"
)
"C:\Program Files\WinRAR\UnRAR.exe" e %a2_loc%
pause
EXIT
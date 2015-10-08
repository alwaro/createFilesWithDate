CreateFileWithDate

This little script allows create the number of files you want with a concrete access and modification date.
Really is a bulk file generator, but has a main goal... create the files with the modif date you want

    Use:

    createFilesWithDate num dd/mm/yyyy path

    num --> Is the number of files you want to create
    dd/mm/yyyy --> The date to use as modification and access date in the new files
    path --> The path where to save the files

The created files will have a name formatted with a combination of fixed and dinamic parts.

The fixed part in the name will be: "file_" at the begining of the name.
The next part is the numer of the file. This number will have the same number of figures in
every file, so if you are listing files ordering by name, you will see them in the right way.
Obviously, to fill the number of figures i use zeros at the left of the number :)
Finally, the last part of the file name is a timestamp with the real date, not is the date you
are passing as argument. This date (the real name) only appears in the name of the file.

This is sample of a bunch of files created with the script:

    $ ls -lrt
    total 48
    -rw-rw-r-- 1 alwaro alwaro 67 feb  1  1990 file_12_20151008082641.txt
    -rw-rw-r-- 1 alwaro alwaro 67 feb  1  1990 file_11_20151008082641.txt
    -rw-rw-r-- 1 alwaro alwaro 67 feb  1  1990 file_10_20151008082641.txt
    -rw-rw-r-- 1 alwaro alwaro 66 feb  1  1990 file_09_20151008082641.txt
    -rw-rw-r-- 1 alwaro alwaro 66 feb  1  1990 file_08_20151008082641.txt
    -rw-rw-r-- 1 alwaro alwaro 66 feb  1  1990 file_07_20151008082641.txt
    -rw-rw-r-- 1 alwaro alwaro 66 feb  1  1990 file_06_20151008082641.txt
    -rw-rw-r-- 1 alwaro alwaro 66 feb  1  1990 file_05_20151008082641.txt
    -rw-rw-r-- 1 alwaro alwaro 66 feb  1  1990 file_04_20151008082641.txt
    -rw-rw-r-- 1 alwaro alwaro 66 feb  1  1990 file_03_20151008082641.txt
    -rw-rw-r-- 1 alwaro alwaro 66 feb  1  1990 file_02_20151008082641.txt
    -rw-rw-r-- 1 alwaro alwaro 66 feb  1  1990 file_01_20151008082641.txt


The created files are not empty. The content is simply a two lines content.

The first line is like a counter showing the number of file and the total.

The 2nd and last file is itself name.

    $ cat sample/file_07_20151008073616.txt

    File number 7 from 12
    Name....: sample/file_07_20151008073616.txt


A lot of times is neccesary to have X number of files with concrete date to test log rotates,
scripts, complex commands with a filtered 'find' from date...etc quite a few projects in which
i have to work with touch command, but always it takes me more time than i want.
With this little tool, is possible to create several blocks of files, assigning the desired dates in a couple of seconds

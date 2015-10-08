#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import datetime
import sys
import os


def main():
    """ The core of the program """

    # Lets check de args (simple way, without module for it)
    checkTheArgs(sys.argv)
    fechaIn = sys.argv[2]       # dd/mm/yyyy"
    numFiles = int(sys.argv[1])      # interger
    workDir = sys.argv[3]

    # Composing the part with the date
    tmpString = "%Y%m%d%H%M%S.txt"
    filenameFull = time.strftime(tmpString)

    for x in xrange(1, numFiles+1):     # limit is numFiles+1 becouse is not starting in 0


        # Putting X zeros at the left of value based in the higest value (numFiles)
        # This let see in a right way the sorted by name listing
        totalFigures = len(str(numFiles))
        numFigures = len(str(x))

        if totalFigures == numFigures:
            # Same number of figures as numFiles so is not neccesary write any zero
            number = str(x)
        else:
            numZeros = totalFigures - numFigures
            fileNumber = '0'*numZeros
            number = fileNumber + str(x)


        filename = "file_"+str(number)+"_"+filenameFull

        #filename = "file_"+str(x)+filenameFull

        # Now lets create the file
        initFile = os.path.join(workDir, filename)
        f = open(initFile, 'w')
        content = "File number " +str(x)+ " from " + str(numFiles) + "\n"\
            "Name....: " + str(initFile) + "\n"
        f.write(content)
        f.close()

        # Now lets change its dates (modif and access)
        fechaUnix = time.mktime(datetime.datetime.strptime(fechaIn, "%d/%m/%Y").timetuple())
        #os.utime(initFile,(1330712280, 1330712292))
        os.utime(initFile,(fechaUnix, fechaUnix))

    print "\nIt's done!!\n"


def checkTheArgs(arguments):
    """ Little function to check the args in a simply way """
    if len(sys.argv) != 4:
        helpAndErrors("Wrong num of arguments")

    if not os.path.isdir(sys.argv[3]):
        helpAndErrors("the path not exists or cannot be accesed!!")

    if not fechaOk(sys.argv[2]):
        helpAndErrors("Date argument with wrong format!!")

    try:
        isNum = int(sys.argv[1])

    except:
        helpAndErrors("El primer arg no parece un numero entero!")


def helpAndErrors(msg):
    """ Another function to show help and errors if these exists """
    # Check if there are some error messages
    if len(msg) > 1:
        print "\nERROR:\n    " + str(msg) + "\n"

    command = os.path.basename(sys.argv[0])
    print "'"+str(command) + "'' is a little tool for create files with a concrete date in the path"
    print "       you pass from command line as an argument. The name of each file will be the mix of"
    print "       a fixed part called 'file_' plus number of file and the timestamp (creation moment)."
    print "       the year must be between the years 1970 and 2500, i think is quite well, isn't it?"
    print "       The last arguent is the path where the files will be created and must exists."
    print "       (Please note that the date in the file name is not the date you are passing from "
    print "       is only a good way to avoid use the same name to several files, which is imposible!)"
    print ""
    print ""
    print "Use:"
    print "    " + str(command) + " num dd/mm/yyyy path"
    print "\nExamples:"
    print "    " + str(command) + " 4 22/12/2004 /tmp/sample"
    print "        This will create 4 files with modif and access date to 22/12/2004 in /tmp/sample\n"
    print "    " + str(command) + " 20 30/01/1999 $HOME/files"
    print "        This will create 20 files with modif and access date to 30/01/1999 in /home/user/files\n"
    print "\n\nwww.ArchivosLog.es   Creative commons License :)\n"
    sys.exit(1)


def fechaOk(date2Check):
    """ Function to check the date passed as argument format """
    toCheck = str(date2Check)

    if toCheck[2:3] == "/" and toCheck[5:6]== "/"  and len(toCheck) == 10:

        if int(toCheck[-4:]) >= 1970 and int(toCheck[-4:]) <= 2500:
            result = True
        else:
            helpAndErrors("The year MUST be between 1970 y 2500!")

    else:
        result = False

    return result


if __name__=='__main__':
    main()

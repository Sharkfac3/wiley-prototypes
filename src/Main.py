'''
Created on Nov 21, 2017

@author: sharkface
'''
from _collections import deque
from wiley.threads.commandinput import CommandInput
from wiley.threads.commandoutput import CommandOuput
import os

def testCommandSending():
    #print('tits dood, tits')
    commandQueue = deque()
    #create
    inputThread = CommandInput(commandQueue)
    outputThread = CommandOuput(commandQueue)
    #start
    inputThread.start()
    outputThread.start()
    #finish
    inputThread.join()
    outputThread.join()

def testDiskSpaceCheck():
    disk = os.statvfs("/")
    print ("preferred file system block size: " + str(disk.f_bsize))
    print ("fundamental file system block size: " + str(disk.f_frsize))
    print ("total number of blocks in filesystem: " + str(disk.f_blocks))
    print ("total number of free blocks: " + str(disk.f_bfree))
    print ("free blocks available to non-super user: " + str(disk.f_bavail))
    print ("total number of file nodes: " + str(disk.f_files))
    print ("total number of free file nodes: " + str(disk.f_ffree))
    print ("free nodes available to non-super user: " + str(disk.f_favail))
    print ("flags: " + str(disk.f_flag))
    print ("miximum file name length: " + str(disk.f_namemax))
    print ("~~~~~~~~~~calculation of disk usage:~~~~~~~~~~")
    totalBytes = float(disk.f_bsize*disk.f_blocks)
    print ("total space: %d Bytes = %.2f KBytes = %.2f MBytes = %.2f GBytes" % (totalBytes, totalBytes/1024, totalBytes/1024/1024, totalBytes/1024/1024/1024))
    totalUsedSpace = float(disk.f_bsize*(disk.f_blocks-disk.f_bfree))
    print ("used space: %d Bytes = %.2f KBytes = %.2f MBytes = %.2f GBytes" % (totalUsedSpace, totalUsedSpace/1024, totalUsedSpace/1024/1024, totalUsedSpace/1024/1024/1024))
    totalAvailSpace = float(disk.f_bsize*disk.f_bfree)
    print ("available space: %d Bytes = %.2f KBytes = %.2f MBytes = %.2f GBytes" % (totalAvailSpace, totalAvailSpace/1024, totalAvailSpace/1024/1024, totalAvailSpace/1024/1024/1024))
    totalAvailSpaceNonRoot = float(disk.f_bsize*disk.f_bavail)
    print ("available space for non-super user: %d Bytes = %.2f KBytes = %.2f MBytes = %.2f GBytes " % (totalAvailSpaceNonRoot, totalAvailSpaceNonRoot/1024, totalAvailSpaceNonRoot/1024/1024, totalAvailSpaceNonRoot/1024/1024/1024) )


def testWebSocketServer():
    pass

if __name__ == '__main__':
    testCommandSending()
    #testDiskSpaceCheck()






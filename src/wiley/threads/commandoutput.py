'''
Created on Nov 23, 2017

@author: sharkface
'''

import threading
import time

class CommandOuput(threading.Thread):
    '''
    this is the class which will handle actually working with the commands that get input into the system. 
    '''


    def __init__(self, processQueue):
        '''
        take in the queue that will handle commands from various inputs
        yeah prototypeeeeeeee
        '''
        threading.Thread.__init__(self)
        self.queueToProcess = processQueue
        #just a test variable here yo
        self.keepRunning = True
    
    def run(self):
        while self.keepRunning:
            time.sleep(5)
            try:
                command = self.queueToProcess.pop()
                print('the command was: ')
                print(command)
                if command == 10:
                    self.keepRunning = False
            except IndexError:
                #print('no command found here boss man')
                pass
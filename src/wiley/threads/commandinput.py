'''
Created on Nov 23, 2017

@author: sharkface
'''

import threading
#from src.wiley.commands.voice.basic import DiskSpace
import speech_recognition as sr

class CommandInput(threading.Thread):
    '''
    this class is for creating the thread that will handle taking in commands for wiley
    later we will likely have to rename this "voice command input"
    as later we will have more than just voice commands.... but this is prototype repo
    '''

    def __init__(self, workerQueue):
        '''
        will likely want to take in the dequeue here that we send off to the thread that actually handles the commands
        '''
        threading.Thread.__init__(self)
        self.queueForOutputProcess = workerQueue
    
    def run(self):
        print("hello")
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        '''
        for x in range(0, 13):
            time.sleep(10)
            print('going to send the command of: ')
            print(x)
            if(x == 3):
                diskCommand = DiskSpace()
                self.queueForOutputProcess.append(diskCommand)
            else:
                self.queueForOutputProcess.append(x)
            time.sleep(1)
        '''
'''
Created on Dec 15, 2017

@author: sharkface
'''

class Sender(object):
    '''
    the sender basically takes care of actually sending some manner of voice message
    '''


    def __init__(self, voiceToTextString = None):
        '''
        not sure what to put here yet
        
        something something strip out "wiley bot"
        probably will have issues with the way we gather the VTT
        '''
        self.voiceToTextString = voiceToTextString
    def getVoiceTextString(self):
        '''
        dont include "wiley bot" when returning this...
        '''
        return self.voiceToTextString
    
'''
Created on 10/08/2019

@author: Lee5
'''

class target:

    def __init__(self, text = ''):
        self._text = text
        
    def get_text(self):
        return self._text
    
    def set_text(self, text = ''):
        self._text = text
    
    def __str__(self):
        return self.get_text()
    

'''
Created on 10/08/2019

@author: Lee5
'''
import unittest
from logger import Logger
from Target import target



class Test(unittest.TestCase):

    def test_info(self):
        #Arrange
        t = target()
        log = Logger(t.set_text)
    
        #Act
        log.info("my unique string")
        
        #Assert
        self.assertEqual(t.get_text(), "[INFO] my unique string")
        


    def test_error(self):
        #Arrange
        t = target()
        log = Logger(t.set_text)
        
        #Act
        log.error("msg")
        
        #Assert
        self.assertEqual(t.get_text(), "[WARNING] msg")
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
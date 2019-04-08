'''
Created on Apr 8, 2019

@author: Anisha
'''
import ConfigParser
import StringIO
import os 

class propReaderClass(): 
    
    def read_propertyFile(self,file_path):
        with open(file_path) as f:
            config = StringIO.StringIO()
            config.write('[WebElementsValue]\n')
            config.write(f.read())
            config.seek(0, os.SEEK_SET)
    
            cp = ConfigParser.SafeConfigParser()
            cp.readfp(config)
            
            return dict(cp.items('WebElementsValue'))
        
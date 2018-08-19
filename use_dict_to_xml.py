
"""
import dicttoxml
xml = dicttoxml.dicttoxml("C:/Users/bethge-adm/Documents/GitHub/IGComp/IGComp/testfiles/simple.xml")
#C:/Users/bethge-adm/Documents/GitHub/IGComp/IGComp/testfiles/tsk_file.xctsk
"""
import urllib
import json
import dicttoxml
import os



xml = ""
dir_path = os.path.dirname(os.path.realpath(__file__))          #use os to get this file directory  #string
file_path = dir_path + "//task_files/task_2018-08-16.json"      #put in here the .xctsk file from xctrack and rename it into *.json



with open(file_path, 'r') as f:
    content = f.read()
    print(content)


    obj = json.loads(content)
    xml = dicttoxml.dicttoxml(obj)

print(xml)   


#TODO: make rel path
file_path_out = "C:/Users/bethge-adm/Documents/GitHub//IGComp/outputfiles/taskout.xml"

with open(file_path_out, 'w') as f:
    f.write(xml)


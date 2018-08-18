
"""
import dicttoxml
xml = dicttoxml.dicttoxml("C:/Users/bethge-adm/Documents/GitHub/IGComp/IGComp/testfiles/simple.xml")
#C:/Users/bethge-adm/Documents/GitHub/IGComp/IGComp/testfiles/tsk_file.xctsk
"""
import urllib
import json
import dicttoxml
xml = ""
file_path = "C:/Users/bethge-adm/Documents/GitHub/IGComp/IGComp/testfiles/tsk_file.xctsk"
with open(file_path, 'r') as f:
    content = f.read()
    print(content)


    obj = json.loads(content)
    xml = dicttoxml.dicttoxml(obj)

 
    


#TODO: make rel path
file_path_out = "C:/Users/bethge-adm/Documents/GitHub/IGComp/IGComp/testfiles/taskout.xml"

with open(file_path_out, 'w') as f:
    f.write(xml)
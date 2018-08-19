import os
from xml.etree import ElementTree


dir_path = os.path.dirname(os.path.realpath(__file__))          #use os to get this file directory  #string
task_file = dir_path + "\\outputfiles\\taskout.xml"


print(task_file)

dom = ElementTree.parse(task_file)
print (dom)
turnpoints = dom.findall('dict')

for c in turnpoints:
    coord = c.find('SSS')


    
print(turnpoints)
import os
from xml.etree import ElementTree

file_name = 'simple.xml'
#file_name = 'C:/Users/bethge-adm/Documents/GitHub/IGComp/IGComp/lxml-master/samples/simple.xml'
full_file = os.path.abspath(os.path.join( 'IGComp/testfiles' , file_name))
print(full_file)

dom = ElementTree.parse(full_file)
print (dom)
waypoints = dom.findall('waypoint')

for c in waypoints:
    coord = c.find('coord').text
    time = c.find('time').text

    print(coord, time)

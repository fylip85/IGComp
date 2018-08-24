import lxml.builder as lb
from lxml import etree

nstext = "new stesting"
story = lb.E.xml(
  lb.E.lktask(type="Race"),
  lb.E.options(
    lb.E.timegate(number="S11190 Brigels"),
    lb.E.rules(
      lb.E.finish(faiheight="false"),
      lb.E.start(maxheight="0"),
    )
  ),
  lb.E.taskpoints(
    lb.E.point(radius="19500", a="Name1", test="something"),
    lb.E.point(idx="Name1", a="1500"),
    lb.E.point(idx="Name1", radius="2000"),
  ),
  lb.E.waypoints(
    lb.E.point(name="B05225 SEDRUN STREM", latitude="46.699500", longitude="8.780333", altitude="2250.000000", flags="2", code="B05", format="1", country="FR", style="1"),
    lb.E.point(name="B05225 SEDRUN STREM", latitude="46.699500", longitude="8.780333", altitude="2250.000000", flags="2", code="B05", format="1", country="FR", style="1"),
    lb.E.point(name="B05225 SEDRUN STREM", latitude="46.699500", longitude="8.780333", altitude="2250.000000", flags="2", code="B05", format="1", country="FR", style="1"),
  ),
  
  )





  

print 'story:\n', etree.tostring(story, pretty_print=True)


with open('newxmlfile.xml', 'w') as f:
    f.write(etree.tostring(story, pretty_print=True))

"""

<?xml version="1.0" encoding="UTF-8"?>
<lk-task type="Race">
	<options auto-advance="Auto">


    """

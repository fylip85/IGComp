import lxml.builder as lb
from lxml import etree

nstext = "new stesting"
story = lb.E.Peter(
  lb.E.taskpoints(
    lb.E.point(name="S11190 Brigels", act="19500.000"),
    lb.E.point(name="S1224543 Flims", act="19500.000"),
  name="S11190 Brigels", act="19500.000"),
  lb.E.waypoints(nstext, name="Name1", act="set2"),

  lb.E.Relation(lb.E.Asset(idref="Scope:700"),
            name="Scope", act="set")
  )

print 'story:\n', etree.tostring(story, pretty_print=True)


"""

<?xml version="1.0" encoding="UTF-8"?>
<lk-task type="Race">
	<options auto-advance="Auto">


    """

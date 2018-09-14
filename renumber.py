from lxml import etree
import sys

tree = etree.parse(sys.argv[1])

mapping = {}
max_id = 0

for node in tree.iter("*"):
    if 'id' in node.attrib:
        print 'found id:', node.attrib["id"]
        id = int(node.attrib["id"])
        if id > max_id:
            max_id = id
        if id not in mapping:
            mapping[id] = id
        else:
            max_id += 1
            mapping[id] = max_id
            node.attrib["id"] = str(max_id)
            print 'Remapped {0} to {1}'.format(id, max_id)

            attributes = ['basePoint', 'firstPoint', 'secondPoint', 'center', 'point1', 'point4']
            for i in attributes:
                if i in node.attrib:
                    node.attrib[i] = str(mapping[int(node.attrib[i])])

print etree.tostring(tree)

#import xmltools
from collections import defaultdict
import xml.dom.minidom
from xml.dom.minidom import parseString

D = defaultdict(list)

def parseXMLFile():
	file = open("dict.xml")
	data = file.read()
	file.close()
	dom = parseString(data)
	wordTag  = dom.getElementsByTagName('word')
	#print wordTag
	#print wordTag[0].childNodes[0].data
	#print wordTag[0].data

	newWord = ""
	for word in wordTag:
		for node in word.childNodes:
			if node.nodeType != node.TEXT_NODE and node.tagName == 'name':
				newWord = node.childNodes[0].nodeValue
				#print node.childNodes[0].nodeValue
			if node.nodeType != node.TEXT_NODE and node.tagName == 'translate':
				D[newWord].append(node.childNodes[0].nodeValue)
	

#def openFile(filename)

def test1():
	md = defaultdict(list)
	md[1].append('a')
	md[1].append('b')
	md[2].append('c')

	print md[1]

def main():
	print "Hellow"

#main()
#test1()
parseXMLFile()
for w in D:
	print "%s " % w,
	for t in D[w]:
		print t,
	print
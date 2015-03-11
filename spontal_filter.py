#!/usr/bin/env python
#Remy Wang
import sys
import xml.etree.ElementTree as ET


def main(argv):
	tree = ET.parse(argv[1])
	root = tree.getroot()
	
	for child in root.findall('POINT'):
		a = float(child.find('BOTTOM_HZ').text)
		b = float(child.find('TOP_HZ').text)
		c = float(child.find('F0_END').text)
		d = float(child.find('F0_START').text)
		if c < a or d > b or c > b or d < a:
			root.remove(child)
		
	
	tree.write(argv[2])
	

	
	
main(sys.argv)	
	
	
	
	
	


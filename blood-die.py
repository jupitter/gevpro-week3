#!/usr/bin/python3
# Remy Wang


import sys
import json
from collections import namedtuple



def main(argv):
	inputbestand= open(argv[1],'r')
	outputbestand= open('blood-die_outputbestand.json','w')
	CountryInfo =namedtuple('Countryinfo', 'countrylanguage, classification, blood, dying')
	jsonFile = json.load(inputbestand)
	for line in jsonFile:
		country = CountryInfo(line[0],line[1],line[2], line[3])
		bloodWords = country.blood.split()
		dyingWords = country.dying.split()
		[json.dump(country, outputbestand) for blood in bloodWords if blood in dyingWords]
	inputbestand.close()
	outputbestand.close()

if __name__ == "__main__":
	main(sys.argv)

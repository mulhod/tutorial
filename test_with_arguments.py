#!/usr/bin/python -tt
import sys

def main():
	if len(sys.argv) != 2:
		sys.stderr.write("ERROR: You either did not enter an argument or entered too many! Try again.\n")
		sys.exit(1)
	
	file = sys.argv[1]
	
	f = open(file, 'r')
	text = f.read()
	print text


if __name__ == '__main__':
	main()
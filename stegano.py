#!/usr/bin/env python
import sys, getopt
import homoglyphs
			
def print_help():
	print("Usage:")
	print("Encode: stegano.py [-e | --encode] <msg>,<secret>")
	print("Decode: stegano.py [-d | --decode] <msg>")
	print("Help: stegano.py [-h | --help]")

def main(argv):
	if len(argv) > 1:
		try:
			opts, args = getopt.getopt(argv, "hd:e:", ["help", "decode=", "encode="])
		except getopt.GetoptError:
			print_help()
			sys.exit(1)
		for opt, arg in opts:
			if opt in ('-h', '--help'):
				print_help()
			else:
				homoglyphs.update_dico()
				if opt in ('-d', '--decode'):
					homoglyphs.decode(arg)
				elif opt in ('-e', '--encode'):
					msgs = arg.split(',')
					if len(msgs) > 1:
						homoglyphs.encode(msgs[0], msgs[1])		
	else:
		print_help()

if __name__ == '__main__':
	main(sys.argv[1:])

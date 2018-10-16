homoglyphs = {
		"!":["FF01"],
		'"':["FF02"],
		"$":["FF04"],
		"%":["FF05"],
		"&":["FF06"],
		"'":["FF07"],
		"(":["FF08"],
		")":["FF09"],
		"*":["FF0A"],
		"+":["FF0B"],
		",":["FF0C"],
		"-":["FF0D"],
		".":["FF0E"],
		"/":["FF0F"],
		"0":["FF10"],
		"1":["FF11"],
		"2":["FF12"],
		"3":["FF13"],
		"4":["FF14"],
		"5":["FF15"],
		"6":["FF16"],
		"7":["FF17"],
		"8":["FF18"],
		"9":["FF19"],
		":":["FF1A"],
		";":["FF1B"],
		"<":["FF1C"],
		"=":["FF1D"],
		">":["FF1E"],
		"?":["FF1F"],
		"@":["FF20"],
		"A":["FF21","0391","0410"],
		"B":["FF22","0392","0412"],
		"C":["FF23","03F9","216D","0421"],
		"D":["FF24","216E"],
		"E":["FF25","0395","0415"],
		"F":["FF26","03DC"],
		"G":["FF27"],
		"H":["FF28","0397","041D"],
		"I":["FF29","0399","0406","2160"],
		"J":["FF2A","0408"],
		"K":["FF2B","039A","041A","216F"],
		"L":["FF2C","216C"],
		"M":["FF2D","039C","041C"],
		"N":["FF2E","039D"],
		"O":["FF2F","039F","041E"],
		"P":["FF30","03A1","0420"],
		"Q":["FF31"],
		"R":["FF32"],
		"S":["FF33","0405"],
		"T":["FF34","03A4","0422"],
		"U":["FF35"],
		"V":["FF36","0474","2164"],
		"W":["FF37"],
		"X":["FF38","03A7","2169","0425"],
		"Y":["FF39","03A5","04AE"],
		"Z":["FF3A","0396"],
		"[":["FF3B"],
		"\\":["FF3C"],
		"]":["FF3D"],
		"^":["FF3E"],
		"_":["FF3F"],
		"`":["FF40"],
		"a":["FF41","0430"],
		"b":["FF42","042C"],
		"c":["FF43","03F2","0441","217D"],
		"d":["FF44","217E"],
		"e":["FF45","0435"],
		"f":["FF46"],
		"g":["FF47"],
		"h":["FF48","04BB"],
		"i":["FF49","0456","2170"],
		"j":["FF4A","0458"],
		"k":["FF4B"],
		"l":["FF4C","217C"],
		"m":["FF4D","217F"],
		"n":["FF4E"],
		"o":["FF4F","03BF","043E"],
		"p":["FF50","0440"],
		"q":["FF51"],
		"r":["FF52"],
		"s":["FF53","0455"],
		"t":["FF54"],
		"u":["FF55"],
		"v":["FF56","03BD","0475","2174"],
		"w":["FF57","0461"],
		"x":["FF58","0445","2179"],
		"y":["FF59","0443"],
		"z":["FF5A"],
		"{":["FF5B"],
		"|":["FF5C"],
		"}":["FF5D"],
		"~":["FF5E"],
		" ":["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","200A","2028","2029","202F","205F"]
}
alphabet_chars = list(" abcdefghijklmnopqrstuvwxyz123456789'0.:/\\%-_?&;")
alphabet_chars_bitlength = len("{0:b}".format(len(alphabet_chars)))
homoglyphs_lookup = {}

def encode(message, secret):
	secret = secret.lower() + " "
	secret_bin = ""
	for i in range(0, len(secret)):
		character = secret[i]
		index_char = alphabet_chars.index(character)
		if index_char >= 0:
			char_bin = padding("{0:b}".format(index_char), alphabet_chars_bitlength)
			if len(char_bin) != alphabet_chars_bitlength:
				print("ERROR: binary representation of character too big!" + "{0:b}".format(index_char) + " zeropadded to " + padding("{0:b}".format(index_char), alphabet_chars_bitlength))
			secret_bin += char_bin
		else:
			print("ERROR: secret contains invalid character '" + character + "' Ignored.")
	secret_bin = check_bit_length(secret_bin)
	result = ''
	for i in range(0, len(message)):
		character = message[i]
		if character in homoglyphs:
			homoglyph_options = homoglyphs[character][0:]
			homoglyph_options_bitlength = len("{0:b}".format(len(homoglyph_options) + 1)) - 1
			if len(secret_bin) > 0:
				bin_to_encode = secret_bin[:homoglyph_options_bitlength]
				secret_bin = secret_bin[homoglyph_options_bitlength:]	
				encode_bin_dec = int(bin_to_encode, 2)
				if encode_bin_dec > 0:
					character = chr(int(homoglyph_options[encode_bin_dec - 1], 16))
		result += character
	if len(secret_bin) > 0:
		print("The message is too small. Please add spaces or remove some characters in the secret")
	else:
		print("Result (with quotes):\n'" + result + "'")


def check_bit_length(secret_binary):
	if int(secret_binary, 2) % alphabet_chars_bitlength > 0:
		secret_binary += padding("0", alphabet_chars_bitlength - (int(secret_binary, 2) % alphabet_chars_bitlength))
	return str(secret_binary)

def decode(message):
	secret_binary = ""
	result = ''
	for i in range(0, len(message)):
		character = message[i : i+1]
		if character in homoglyphs_lookup:
			secret_binary += homoglyphs_lookup[character]
	secret_binary = check_bit_length(secret_binary)
	while len(secret_binary) > 0:
		bin_char = secret_binary[:alphabet_chars_bitlength]
		if len(bin_char) > 0:
			bin_char = padding(bin_char, alphabet_chars_bitlength);
			if len(bin_char) != alphabet_chars_bitlength:
				print("ERROR: Unable to extract 5 characters (paddingded) from string " + secret_binary[i : alphabet_chars_bitlength] + padding(secret_binary[i : alphabet_chars_bitlength], alphabet_chars_bitlength))
			dec_char = int(bin_char, 2);
			if dec_char >=  0 and dec_char < len(alphabet_chars):
				result += alphabet_chars[dec_char]
			else:
				print("ERROR: Unable to find alphabet character at position" + str(dec_char))
		secret_binary = secret_binary[alphabet_chars_bitlength:]
	print(result)
	
def padding(value, length):
	res_str = ''
	for i in range(0, length - 1):
		res_str += "0"
	res_str += value
	return res_str[len(res_str)-length:]
	
def update_dico():
	for key in homoglyphs:
		bit_length = len("{0:b}".format(len(homoglyphs[key]) + 1)) - 1
		homoglyphs_lookup[key] = padding('0', bit_length)
		for i in range(0, len(homoglyphs[key])):
			homoglyphs_lookup[chr(int(homoglyphs[key][i], 16))] = padding("{0:b}".format(i + 1), bit_length)

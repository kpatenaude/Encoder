#!/usr/bin/python
# Generic Caeser cipher encoder
# Only uses capital letters


fi = raw_input('Type user 1st initial: ')
si = raw_input('Type user 2nd initial: ')
li = raw_input('Type user 3rd initial: ')


map = {
	'A': 23,
	'a': 23,
	'B': 24,
	'b': 24,
	'C': 25,
	'c': 25,
	'D': 26,
	'd': 26,
	'E': 27,
	'e': 27,
	'F': 28,
	'G': 29,
	'H': 30,
	'I': 31,
	'J': 32,
	'K': 33,
	'L': 34,
	'M': 35,
	'N': 10,
	'O': 11,
	'P': 12,
	'Q': 13,
	'R': 14,
	'S': 15,
	'T': 16,
	'V': 17,
	'W': 18,
	'X': 19,
	'Y': 20,
	'Z': 21
}

pwa = (map[fi])
pwb = (map[si])
pwc = (map[li])

dcpwa = str(pwa)
dcpwb = str(pwb)
dcpwc = str(pwc)

print "kp"+"".join([dcpwa,dcpwb,dcpwc])

# print "password is kp%s." %(kppw)

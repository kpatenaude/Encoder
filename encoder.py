#!/usr/bin/python
# Generic Caeser cipher encoder

ui = raw_input('Type user initials: ').upper()

fi = ui[0]
si = ui[1]
li = ui[2]

#fi = raw_input('Type user 1st initial: ').upper()
#si = raw_input('Type user 2nd initial: ').upper()
#li = raw_input('Type user 3rd initial: ').upper()

#fi.upper()
#si.upper()
#li.upper()

map = {
	'A': 23,
	'B': 24,
	'C': 25,
	'D': 26,
	'E': 27,
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

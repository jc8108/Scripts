#!/usr/bin/python
# Simple script to create combinations of user names for brute forcing
# Have caution running this multiple times, as the username-combo list is written in APPEND mode
# Therefore if you run it, then run it again in the same directory, you will have duplicates

import sys

print("Usage: ADNames.py <listofnames.txt>\nNames must be in format of: First Last\n")

name_file = (sys.argv[1])

with open(name_file, 'r') as names:
	for x in names.readlines():
		name_list = (x.split())
		new_list = []
		lower_list = []
		upper_list = []
		# just making easier to read variables from the split first / last names
		first = name_list[0]
		last = name_list[1]
		# creating variations of the first and last name as is
		# if you want to add more variations, add them here
		new_list.append(first[0] + "." + last)
		new_list.append(first[0] + last)
		new_list.append(first[:3] + last)
		new_list.append(first + "." + last)
		new_list.append(first + last)
		# creating lists with combos as all caps and all lowercase from the new_list
		for l in new_list:
			lower_list.append(l.lower())
		for u in new_list:
			upper_list.append(u.upper())
		with open("username-combos.txt", "a+") as userlist:
			for p in new_list:
				userlist.write("\n")
				userlist.write(p)
			for w in lower_list:
				userlist.write("\n")
				userlist.write(w)
			for n in upper_list:
				userlist.write("\n")
				userlist.write(n)
print("username-combos.txt ready in current directory.")
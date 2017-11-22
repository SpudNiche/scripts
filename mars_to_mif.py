#!/usr/bin/python3
# Author: Nicholas LaJoie
# File: mars_to_mif.py
# Date: November 22, 2017
# Description: Converts a .txt file dumped in hex format from MARS into a .mif file. Created for all my pals in ECE 473.
# Usage: $python mars_to_mif.py [input.txt] (optional)[output]

# Packages
import sys

# Variables
temp = """% File generated by 'mars_to_mif.py' by SpudNiche' %
% www.github.com/SpudNiche %

DEPTH = 64;			\t\t% Memory depth and width are required     %
WIDTH = 32;			\t\t% Enter a decimal number                  %
ADDRESS_RADIX = HEX;		% Address and value radixes are optional  %
DATA_RADIX = HEX;		\t% Enter BIN, DEC, HEX, or OCT; unless     %
% otherwise specified, radixes = HEX      %
-- Specify initial data values for memory, format is address : data
CONTENT BEGIN
[00..3F]	: 00000000;	% Range - Every address from 00 to 3F = 00000000 %
-- Initialize data\n"""

# Get command line arguments
if len(sys.argv) < 2:
	print "ERROR: Please format as >> [script] [input.txt] (optional)[output]"
	exit()

# Open MARS hex file dump (.txt) as read-only
txt = sys.argv[1]
if txt.endswith('.txt'):
	f1 = open(sys.argv[1],'r')
else:
	print "ERROR: Improper input type. Must be .txt"
	exit()

# Use command line output file name if provided
if len(sys.argv) == 3:
	f_out = sys.argv[2] + '.mif'
else:
	f_out = 'out.mif'

# Create .mif file to write to
f2 = open(f_out, 'w+')

# Get instructions in hex from text file
h = f1.readlines()

# Write file header
f2.write(temp)

# Fill .mif file with provided instructions
for i, h in enumerate(h):
	f2.write("{0:0{1}X}".format(i,2) + ' : ' + h.strip() + ';\n')

# Pad the remainder of the .mif file with 0's (NOPs)
f2.write("[" + "{0:0{1}X}".format(i+1,2) + "..3F] : 00000000; % nop %\nEND;")

# Close it out
f1.close()
f2.close()

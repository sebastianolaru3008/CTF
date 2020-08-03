#######################
# Powershell XOR 2 Files
# xor.py
# Jul 2016
# Website: http://www.Megabeets.net
# Use: ./xor.py file1 file2 outputFile
# Example: ./xor.py C:\a.txt C:\b.txt C:\result.txt
#######################

import sys

# Read two files as byte arrays
file1_b = bytearray(open(sys.argv[1], 'rb').read())
# file2_b = bytearray(open(sys.argv[2], 'rb').read())
stringXOR = bytearray(b'ar')
 
num = int(sys.argv[3])

# Set the length to be the smaller one
size = len(file1_b)

xord_byte_array = bytearray(size)

# XOR between the files
for i in range(size):
	xord_byte_array[i] = file1_b[i] ^ stringXOR[i%num]

# Write the XORd bytes to the output file	
open(sys.argv[2], 'wb').write(xord_byte_array)

print "[*] %s XOR %s\n[*] Saved to \033[1;33m%s\033[1;m."%(sys.argv[1], stringXOR, sys.argv[2])
# Created by Joshua Curry
# The purpose of this program is to be utilized in a bash script,
# to automate hashing a downloaded file and checking against the supplied hash.

import hashlib
import sys

filename = (sys.argv[1])  # the name of the file you want to hash

print('File: ' + filename + '\n')


with open(filename, 'rb') as file:  # opening the file and hashing
    file_as_bytes = file.read()
    h256 = hashlib.sha256(file_as_bytes).hexdigest()
    hmd5 = hashlib.md5(file_as_bytes).hexdigest()
    print(f'SHA256: {h256}\n')
    print(f'MD5: {hmd5}\n')


compared_hash = input('Enter hash to compare or press enter to skip: \n>>>')

if compared_hash == h256:  # comparing hash
    print('\nValid SHA256 hash.\n')
elif compared_hash == hmd5:
    print('\nValid MD5 hash.\n')
elif compared_hash == '':
    sys.exit()
else:
    print('\nInvalid hash.\n')

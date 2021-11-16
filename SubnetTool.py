# Created by Joshua Curry
# A tool to calculate subnet info from an IP
# You must know either your CIDR notation or subnet address

print('Enter an IPv4 address:\n'
      'If you do not know your CIDR you will be asked for your subnet address.\n'
      'Good examples: 192.168.5.0/24 or 192.168.5.0')
aip = input()

# take the IP address string and split it into a list

octets = aip.split('.')


# check the 4th octet for the CIDR notation and create a variable from that
# fix the 4th octet that has the /x add-on
# if no CIDR notation program skips this step


def check_cidr(oct_list):
    global octets
    c = oct_list[3].split('/')
    octets[3] = c[0]
    return int(c[1])


# converts a list of integers into an 8 digit binary number

def list_to_binary(ip_list):
    b = []
    for y in range(len(ip_list)):
        ip_list[y] = int(ip_list[y])
        b.append(format(ip_list[y], '08b'))
    return b


# takes the 4 octets of 8 digit binary numbers and joins them together into one string
# counts all the leading 1s and that number becomes the CIDR
# this is for when a subnet address is supplied but not the CIDR

def cidr_from_submask(s):
    for z in range(len(s)):
        s[z] = str(s[z])
    smstring = "".join(s)
    lead_ones = 0
    for c in smstring:
        if c == '1':
            lead_ones += 1
    return lead_ones


# check if the CIDR was supplied and if so run the CIDR function
# set need_mask to True so that later we can check this to run a different function

# if no CIDR supplied ask the user for the subnet address
# then split it, convert it, join and count the 1s to get the CIDR
# for that scenario we would set need_mask to False to skip that step later


if '/' in octets[3]:
    cidr = check_cidr(octets)
    need_mask = True
else:
    need_mask = False
    smask = input('Enter subnet mask: \n')
    sm = smask.split('.')
    sbin = list_to_binary(sm)
    cidr = cidr_from_submask(sbin)

# take the IP address and convert it to an integer and then into binary
# we need it to be an 8 character binary so that we can match it 1 for 1 later

ip_binary = list_to_binary(octets)


# create a binary representation from its CIDR
# the CIDR represents however many leading 1s there are
# but we need 32 bits for the full address so we fill with 0s
# every 8 bits represents 1 octet

def submask_from_cidr(cdr):
    subnet_binary = '1' * cdr
    subnet_binary = subnet_binary.ljust(32, '0')
    mask = [0, 0, 0, 0]
    mask[0] = int(subnet_binary[0:8], 2)
    mask[1] = int(subnet_binary[8:16], 2)
    mask[2] = int(subnet_binary[16:24], 2)
    mask[3] = int(subnet_binary[24:32], 2)
    return mask


if need_mask:
    submask = submask_from_cidr(cidr)
else:
    submask = sm

# create the network address by bitwise ANDing the submask and the ip address

network_add = [0, 0, 0, 0]
for x in range(0, 4):
    network_add[x] = int(submask[x]) & int(octets[x])


# create an inverted version of the subnet mask from the CIDR notation
# basically the opposite as what we did earlier
# we need leading 0s and trailing 1s

def invert_submask(cdr):
    mask = [0, 0, 0, 0]
    inv_sub = '0' * cdr
    inv_sub = inv_sub.ljust(32, '1')
    mask[0] = int(inv_sub[0:8], 2)
    mask[1] = int(inv_sub[8:16], 2)
    mask[2] = int(inv_sub[16:24], 2)
    mask[3] = int(inv_sub[24:32], 2)
    return mask


inv_submask = invert_submask(cidr)

# do a bitwise OR operation on the inverted subnet mask and network address to get the broadcast address

broadcast_add = [0, 0, 0, 0]
for x in range(0, 4):
    broadcast_add[x] = int(inv_submask[x]) | int(network_add[x])

first_host = [0, 0, 0, 0]
last_host = [0, 0, 0, 0]

# find the first host by adding 1 to the 4th octet of the network address
# and by subtracting 1 from the 4th octet broadcast address
# the other octets are the same

for x in range(0, 3):
    first_host[x] = str(network_add[x])
first_host[3] = str(network_add[3] + 1)

for x in range(0, 3):
    last_host[x] = str(broadcast_add[x])
last_host[3] = str(broadcast_add[3] - 1)

# convert everything to a string in order to join together
for x in range(0, 4):
    network_add[x] = str(network_add[x])
    broadcast_add[x] = str(broadcast_add[x])
    submask[x] = str(submask[x])

print(f'Subnet Mask: {".".join(submask)}')
print(f'First Host: {".".join(first_host)}')
print(f'Last Host: {".".join(last_host)}')
print(f'Network Address: {".".join(network_add)}')
print(f'Broadcast Address: {".".join(broadcast_add)}')

# the first octet of the IP address helps determine the class
# therefore how many mandatory host bits are required before subnetting
# we subtract this from the CIDR to get the amount of borrowed bits
# we do math on that to find the subnets available

# for hosts we subtract the CIDR from max number of bits to get host bits
# we do math on that to find the hosts available

first = ip_binary[0]

if first.startswith('0'):
    cls = 8
elif first.startswith('10'):
    cls = 16
elif first.startswith('11'):
    cls = 24

borrowed = cidr - cls

net_bits = 32 - cidr
print(f'CIDR: /{cidr}')
print(f'Subnets Available: {2 ** borrowed}')
print(f'Hosts Available: {2 ** net_bits - 2}')

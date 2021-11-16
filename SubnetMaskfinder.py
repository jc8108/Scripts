# Created by Joshua Curry
# A program to help determine the subnet address
# Input subnet + hosts required outputs possible subnet addresses
# Use this with my SubnetTool to find other information for the subnet


network = input('Enter subnets required: ')
hosts = input('Enter max hosts required: ')

# need to add 2 to the hosts required for network address and broadcast address
hosts = hosts + 2


# find the amount of binary 1s required to create the number of hosts
# loops through 'power of x' and when it finds a match, x is the amount of 1s needed

def find_bits(needed):
    for x in range(0, 33):
        bt = 2 ** x
        if bt >= needed:
            bits = x
            return bits


# create a string of 1s and 0s and then split every 8 of them
# this creates each octet for the subnet mask
# then convert them to a int and then a string in order to join them together

def submask_from_cidr(cdr):
    subnet_binary = '1' * cdr
    subnet_binary = subnet_binary.ljust(32, '0')
    mask = [0, 0, 0, 0]
    mask[0] = int(subnet_binary[0:8], 2)
    mask[1] = int(subnet_binary[8:16], 2)
    mask[2] = int(subnet_binary[16:24], 2)
    mask[3] = int(subnet_binary[24:32], 2)
    for x in range(len(mask)):
        mask[x] = str(mask[x])
    return mask


network = find_bits(network)
hosts = find_bits(hosts)

# creating the CIDR by required bits from the class and the bits you need to borrow from the host

a = network + 8
b = network + 16
c = network + 24

print(f'{network} subnet bits required to allow {2 ** network} subnets.')
print(f'{hosts} host bits required to allow {(2 ** hosts) - 2} hosts.\n')

asub = submask_from_cidr(a)
bsub = submask_from_cidr(b)
csub = submask_from_cidr(c)

# checking if the required CIDR + the required hosts bits are under 32 bits
# the CIDR + host bits must be under 32 bits for a valid address

if a + hosts <= 32:
    print(f'For a Class A network this would have a /{a} CIDR notation.\n'
          f'With {a} network bits and {hosts} host bits required, this is possible.\n'
          f'Subnet mask: {".".join(asub)}\n')
else:
    print(f'For a Class A network this would have a /{a} CIDR notation.')
    print(f'With {a} network bits and {hosts} host bits required, this would not be possible.\n')

if b + hosts <= 32:
    print(f'For a Class B network this would have a /{b} CIDR notation.\n'
          f'With {b} network bits and {hosts} host bits required, this is possible.\n'
          f'Subnet mask: {".".join(bsub)}\n')
else:
    print(f'For a Class A network this would have a /{b} CIDR notation.\n')
    print(f'With {b} network bits and {hosts} host bits required, this would not be possible.\n')

if c + hosts <= 32:
    print(f'For a Class A network this would have a /{c} CIDR notation.\n'
          f'With {c} network bits and {hosts} host bits required, this is possible.\n'
          f'Subnet mask: {".".join(csub)}\n')
else:
    print(f'For a Class C network this would have a /{c} CIDR notation.')
    print(f'With {c} network bits and {hosts} host bits required, this would not be possible.')

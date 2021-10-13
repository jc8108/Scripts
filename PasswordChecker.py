# Created by Joshua Curry
# The purpose of this program is to check your password against the top X passwords in a password dump.

#  file to search passwords in
dumpfile = input('Enter FILEPATH of password list:\n')

rank = input('Enter NUMBER of top passwords to check (press enter to check all):\n')

password = input('Enter PASSWORD to check in wordlist:\n')


def custom_check():  # checking only a certain amount of passwords
    print(f'Searching for password in top {rank} passwords...\n{dumpfile}\n')
    not_found = True
    for x in range(len(head)):
        head[x] = head[x].strip()  # creates list and strips newline char
        if head[x] == password:
            print(f'Password found. Ranked number {x} in most common passwords.')
            not_found = False
        if not_found:
            print(f'Password not found.')


def check_all():  # checking every password in a list
    print(f'Searching entire password list...\n{dumpfile}')
    not_found = True
    for x in range(len(all)):
        all[x] = all[x].strip()  # creates list and strips newline char
        if all[x] == password:
            print(f'Password found. Ranked number {x} in most common passwords out of {len(all)}.')
            not_found = False
    if not_found:
        print(f'Password not found in {len(all)}')


with open(dumpfile, "r", encoding='utf-8') as wordlist:  # checks top/all depending on input
    if rank == '':  # creating a list with all lines in it
        all = wordlist.readlines()
        check_all()
    else:
        head = [next(wordlist) for t in range(int(rank))]  # gather just the top X amount of lines
        custom_check()

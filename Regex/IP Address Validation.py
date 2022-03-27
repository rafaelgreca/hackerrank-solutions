import re
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    string = sys.stdin.readline()
    
    ipv4 = re.findall(r'(\d+\.){3}\d+', string)
    if len(ipv4)>0:
        ipv4_numbers = re.findall(r'\d+', string)
        check_numbers = [1 if int(number) > 255 else 0 for number in ipv4_numbers]
        if sum(check_numbers) >= 1:
            sys.stdout.write('Neither\n')
        else:
            sys.stdout.write('IPv4\n')
    else:
        ipv6 = re.findall(r'(\w+\:){7}\w+', string)
        if len(ipv6)>0:
            ipv6_letters = re.findall(r'[g-z]+', string)
            if len(ipv6_letters) > 0:
                sys.stdout.write('Neither\n')
            else:
                sys.stdout.write('IPv6\n')
        else:
            sys.stdout.write('Neither\n')
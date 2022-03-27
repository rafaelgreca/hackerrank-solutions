import re
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    string = sys.stdin.readline()
    
    username_detected = re.findall(r'^[\_\.][0-9]{1,}[a-zA-Z]{0,}$|^[\_\.][0-9]{1,}[a-zA-Z]{0,}\_$', string)
    if len(username_detected)>0:
        sys.stdout.write('VALID\n')
    else:
        sys.stdout.write('INVALID\n')
import re
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    string = sys.stdin.readline()
    
    starts_hackerrank = re.findall(r'^hackerrank', string)
    ends_hackerrank = re.findall(r'hackerrank$', string)
    
    if len(starts_hackerrank)>0 and len(ends_hackerrank)==0:
        sys.stdout.write('1\n')
    elif len(starts_hackerrank)==0 and len(ends_hackerrank)>0:
        sys.stdout.write('2\n')
    elif len(starts_hackerrank)>0 and len(ends_hackerrank)>0:
        sys.stdout.write('0\n')
    else:
        sys.stdout.write('-1\n')
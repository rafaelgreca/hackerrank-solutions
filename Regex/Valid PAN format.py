import re
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    string = sys.stdin.readline()
    
    pan_detected = re.findall(r'^[A-Z]{5}\d{4}[A-Z]$', string)
    if len(pan_detected)>0:
        sys.stdout.write('YES\n')
    else:
        sys.stdout.write('NO\n')
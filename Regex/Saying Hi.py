import re
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    string = sys.stdin.readline()
    
    saudation_detected = re.findall(r'^([Hh][Ii]\s[^Dd])', string)
    if len(saudation_detected)>0:
        sys.stdout.write(string)
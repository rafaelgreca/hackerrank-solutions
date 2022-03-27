import re
import sys

n = int(sys.stdin.readline())
strings = []

for _ in range(n):
    strings.append(sys.stdin.readline())

t = int(sys.stdin.readline())
    
for _ in range(t):
    subword_uk = sys.stdin.readline().strip()
    subword_us = subword_uk.replace('our', 'or').strip()
    count = 0
    
    for string in strings:
        subwords_detected = re.findall(r'\b{}\b|\b{}\b'.format(subword_us, subword_uk), string)
        count += len(subwords_detected)
        
    sys.stdout.write(str(count) + '\n')
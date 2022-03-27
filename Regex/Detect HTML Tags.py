import re
import sys

n = int(sys.stdin.readline())
tags = []

for _ in range(n):
    string = sys.stdin.readline()
    
    tag_detected = re.findall(r'(?<=\<)[^\>\s]+(?=\>)|(?<=\<)[^\/]+(?=\/\>)|(?<=\<)[^\>]+(?=\/\>)', string)
    if len(tag_detected)>0:
        tags.extend([tag.split()[0].replace('/', '') for tag in tag_detected])

tags = list(set(tags))
tags.sort()
sys.stdout.write(';'.join(tags))
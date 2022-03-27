import re
import sys

n = int(sys.stdin.readline())
count = 0

for _ in range(n):
    string = sys.stdin.readline()
    
    hackerrank_detected = re.findall(r'[\@|\#]?hackerrank', string.lower())
    count += len(hackerrank_detected)

sys.stdout.write(str(count))
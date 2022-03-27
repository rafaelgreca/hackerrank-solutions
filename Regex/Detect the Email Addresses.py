import re
import sys

n = int(sys.stdin.readline())
emails = []

for _ in range(n):
    string = sys.stdin.readline()
    
    email_detected = re.findall(r'[\w\.]+\@[\w+\.]+[a-z]+', string)
    if len(email_detected)>0:
        emails.extend([email for email in email_detected])

emails = list(set(emails))
emails.sort()
sys.stdout.write(';'.join(emails))
import re
import sys

n = int(sys.stdin.readline())
phones = []

for _ in range(n):
    string = sys.stdin.readline()
    
    phone_detected = re.findall(r'(\d{1,3}[\-\s])(\d{1,3}[\-\s])(\d{4,10})', string)
    if len(phone_detected)>0:
        phones.append('CountryCode='+str(phone_detected[0][0][:-1])+',LocalAreaCode='+str(phone_detected[0][1][:-1])+',Number='+str(phone_detected[0][2]))

sys.stdout.write('\n'.join(phones))
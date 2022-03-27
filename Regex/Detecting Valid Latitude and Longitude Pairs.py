import re
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    string = sys.stdin.readline()
    
    coordinate_validation = re.findall(r'[\d\.]+', string)
    
    if coordinate_validation[0][0] == '0' or coordinate_validation[1][0] == '0':
        sys.stdout.write('Invalid\n')
    elif coordinate_validation[0][-1] == '.' or coordinate_validation[1][-1] == '.':
        sys.stdout.write('Invalid\n')
    else:
        X = float(coordinate_validation[0])
        Y = float(coordinate_validation[1])
        
        if abs(X)<=90 and abs(Y)<=180:
            sys.stdout.write('Valid\n')
        else:
            sys.stdout.write('Invalid\n')
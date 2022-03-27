import re
import sys

n = int(sys.stdin.readline())
html_attributes = {}

for _ in range(n):
    html = sys.stdin.readline()
    html_detected = re.findall(r'\<[^\>]+\>', html)
    html_detected = [h for h in html_detected if '</' not in h]
    
    if len(html_detected) > 0:
        for h in html_detected:
            tag_detected = re.findall(r'(?<=\<)[a-z0-9]+', h)
            attribute_detected = re.findall(r'[a-z]+(?=\=\".+\")|[a-z]+(?=\=\'.+\')', h)
            if len(tag_detected) > 0 and tag_detected[0] in html_attributes.keys():
                html_attributes[tag_detected[0]].extend([t for t in attribute_detected])
            else:
                if len(attribute_detected) == 0:
                    html_attributes[tag_detected[0]] = []
                else:
                    html_attributes[tag_detected[0]] = [t for t in attribute_detected]

html_attributes = dict(sorted(html_attributes.items(), key=lambda item: item[0]))

for k in html_attributes.keys():
    if len(html_attributes[k]) > 0:
        attributes = list(set(html_attributes[k]))
        attributes.sort()
        sys.stdout.write(str(k) + ':' + ','.join(attributes) + '\n')
    else:
        sys.stdout.write(str(k) + ':\n')
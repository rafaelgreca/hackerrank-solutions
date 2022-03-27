Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z\s]*\b'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
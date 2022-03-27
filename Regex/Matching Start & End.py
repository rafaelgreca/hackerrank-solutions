Regex_Pattern = r"^(\d)\w{3}(\w\.)$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
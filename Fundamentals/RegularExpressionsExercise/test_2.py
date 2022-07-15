# ----- Флагове / Flags ------

import re

# re.I re.IGNORECASE

# text = 'MARIO mariO is Python developer at a BioPharmacy. Mario loves ML and AI'
# result = re.findall('Mario', text, re.IGNORECASE)
# print(result)
# ---------------------------------------------------

# re.X re.VERBOSE

# text = 'Mario is Python developer at a BioPharmacy, his age is 32'
# result = re.search(r'''(^\w{5}) # match 5 letters at the start
#                     .+(\d{2}$) # match 2 digits at the end''', text, re.VERBOSE)
#
# print(result.group(1))
# print(result.group(2))
# ---------------------------------------------------

# re.M re.MULTILINE
text = 'Mario is Python developer at a BioPharmacy, his age is 32'
result = re.findall(r'^\w{3}', text, re.MULTILINE)
# /// верифицира начало ^ и край $ на текст///
print(result)

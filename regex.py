import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d-\d\d')
mo = phoneNumRegex.search('Marcame a mi cel 844-431-74-90')
print(mo.group())

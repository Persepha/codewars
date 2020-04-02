import re

def clean_string(s):
    while '#' in s:
        if re.search('[^#]#', s):
            s = re.sub('[^#]#', '', s)
        else:
            return re.sub('#+', '', s)
    return s

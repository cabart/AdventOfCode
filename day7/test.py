import re


def splitIt (s):
    print(re.split(" bags?[(\.\n)|,]",s))
    print(re.split(" bags?[\.\n|,]+",s))
    return

str1 = "2 dark red bags, 3 vibrant pink bags."
str2 = "2 dark orange bags."

splitIt(str1)
splitIt(str2)

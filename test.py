a = "12345[111]"
import re
pattern = r'\[.*?\]'
b = re.sub(pattern, '', a)
print(b)


# import re
# pattern = r'\[.*?\]'
# s = """Issachar is a rawboned[a] donkey lying down among the sheep pens.[b]"""
# a = re.sub(pattern, '', s)
# print(a)
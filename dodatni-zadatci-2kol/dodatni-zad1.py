"""
1.	Napisati funkciju koja prima string i vraća novi string koji nastaje 
tako da se iz primljenog stringa izbace svi zarezi.
"""

def bezzareza(string):
    novi_str = string.replace("," , "")
    return novi_str

print(bezzareza("ha,ha,, 123he,h,e,!"))
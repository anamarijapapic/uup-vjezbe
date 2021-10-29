"""
1. kolokvij zima 2018-2019 F

3. Napisati funkciju koja kao parametar prima broj i vraca True ako su prva
i zadnja znamenka broja jednake. U suprotnom vraca False.
"""

def jednake(broj):
    zadnja = broj % 10
    while broj > 9:
        broj = broj // 10
    prva = broj % 10
    if prva == zadnja:
        return True
    else:
        return False
    
print(jednake(1868793))
print(jednake(89568))

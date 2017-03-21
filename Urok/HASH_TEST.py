def hash(astring, tablesize):
    
    sum = 0
    
    for pos in range(len(astring)):
        sum = sum + (ord(astring[pos])*(30**pos))
        
    return sum%tablesize

x = hash('Hjdfkjs;djgdfjlgjsjhdfshjdhfjhsdHJHJHUFHUDHsJhf7436872634', 100)

print(x)

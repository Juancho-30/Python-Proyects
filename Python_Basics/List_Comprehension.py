temps = [221, 224, 340, -9999, 230]

newTemps = [temp / 10 if temp != -9999 else 0 for temp in temps]

#isinstance("abc", class (str,int, float))

print(newTemps)
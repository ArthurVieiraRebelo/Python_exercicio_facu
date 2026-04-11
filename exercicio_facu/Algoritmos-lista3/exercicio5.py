ze = 130
chico = 150
anos = 0
for i in range(100):
    if chico > ze:
        chico += 20
        ze += 30
        anos += 1
print(f"Zé passou chico em {anos+1} anos")

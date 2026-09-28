print("Insère un nombre de secondes : ")
nbr1=int(input())
f1= nbr1 // 3600
f2= nbr1 % 3600
f3= f2 // 60
f4= f2 % 60
print(f"{f1}h, {f3}min, {f4}sec")
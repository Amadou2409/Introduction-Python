year = int(input("Hello, en quelle année es-tu né(e) ? "))
age = 2026 - year
print(f"A la fin de l'année 2026, tu auras {age} ")
if age < 12 :
    print ("Tu es un enfant")
if age >= 12 and age <= 17:
    print ("Tu es un adolescent")
else :
    print (" Tu es un adulte")
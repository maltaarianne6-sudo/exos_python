T=[12.5, 14, 9.5, 17, 21, 19.5, 11]
moyenne=sum(T)/len(T)
print(f"Température moyenne : {moyenne:.2f} °C")
print("Température maximale", max(T), "°C")
print("Température minimale", min(T), "°C")
for jours in T:
    if jours > 15:
        print(f"jours > 15°C : {jours}")
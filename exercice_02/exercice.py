for T in [-3, 0, 15, 31]:
    if T < 0:
        print(T, "°C : gel")
    elif T < 15:
        print(T, "°C : froid")
    elif T < 25:
        print(T, "°C : chaud")
    else:
        print(T, "°C : très chaud")

for A in [2024, 1900, 2000]:
    if A % 4 == 0 and (A % 100 != 0 or A % 400 == 0):
        print(A, ": bissextile")
    else:
        print(A, ": non bissextile")
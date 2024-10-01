n = int(input("Quantos termos você quer ver: "))
t1 = 0
t2 = 1
print(f"{t1} - {t2}", end ='')

cont = 3
encontrado = False

while cont <=n:
    t3 = t1 + t2 
    print(f" - {t3}", end = '')
    cont += 1
    t1 = t2
    t2 = t3
print(" FIM")

if n == 0 or n ==1:
    encontrado = True
if encontrado:
    print(f"\nO número {n} pertence à sequência de Fibonacci.")

else:
    print(f"O numero {n}, não pertence à sequência de Fibonacci. ")
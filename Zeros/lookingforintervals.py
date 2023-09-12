
import numpy as np

#Dados
G = 6.67*10**-11
Ms = 1.98*10**30
Mt = 5.98*10**24
R = 1.49*10**11
T = 3.15576*10**7
w = 2*np.pi/T

func = lambda r :(G * Ms )/r**2 - (G*Mt)/(R-r)**2 - r*w**2 

# Defina o intervalo inicial
a = 0.1*10**11
b = 1.48*10**11
tol = 0.01
def find_interval(a,b,tol):
    # Verifique se a função muda de sinal no intervalo [a, b]
    if func(a) * func(b) > 0:
        print("A função não muda de sinal no intervalo [a, b]. Escolha outro intervalo inicial.")
    else:
        # Execute o método da bisseção para encontrar o intervalo [r1, r2] com r2 - r1 = 0.01
        while (b - a) >= tol:
            # Encontre o ponto médio do intervalo
            c = (a + b) / 2

            # Calcule o valor da função no ponto médio
            fc = func(c)

            # Verifique se o ponto médio é a solução
            if fc == 0:
                break

            # Atualize o intervalo [a, b] com base no sinal de fc
            if func(a) * fc < 0:
                b = c
            else:
                a = c

        r1 = a
        r2 = b

        print(f"O intervalo (r1, r2) que possivelmente contém a solução é ({r1}, {r2}) com r2 - r1 = {r2 - r1:.2f}")
        
find_interval(a,b,tol)
'''

VC 2019 Cálculo Numérico: 11/09/2023 - Questão x
Nome: Enzo Gomes FRESE
Número: 21020
Turma A

'''

# importações das bibliotecas
import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np
import sympy as sp


# declaração da função dada
def p(d, t):
    if(d == 0): return 1; # P_0
    elif(d == 1): return t; # P_1
    else:
        a = (2 * (d - 1) + 1)/((d - 1) + 1);
        b = (-1) * ((d - 1)/((d - 1) + 1));

        return a * t * p((d - 1), t) + b * p((d - 1) - 1, t);

# arredondamento de n casas decimais
n = 4;

# tolerância e máximas iterações
tol = 0.0000001;
maxIter = 1000;

#Dados
G = 6.67*10**-11
Ms = 1.98*10**30
Mt = 5.98*10**24
R = 1.49*10**11
T = 3.15576*10**7
w = 2*np.pi/T

f = lambda r :(G * Ms )/r**2 - (G*Mt)/(R-r)**2 - r*(w)**2 
df_dr = lambda r: (-2 * G * Ms) / r**3 + (2 * G * Mt) / (R - r)**3 - w**2
h = lambda x : x

# método da bisseção
def bisec (f,a,b,tol):
    if(f(a)*f(b)<0):
        c = (a+b)/2
        if(abs(f(c)) < tol): return round(c,3)
        if(f(a)*f(c)<0):
            return bisec(a,c,f)
        elif(f(b)*f(c)<0):
            return bisec(c,b,f)  
    else: return "não foi possível encontrar a raiz ;-;"  
    
def find_interval(a,b,tol):
    # Verifique se a função muda de sinal no intervalo [a, b]
    if f(a) * f(b) > 0:
        print("A função não muda de sinal no intervalo [a, b]. Escolha outro intervalo inicial.")
    else:
        # Execute o método da bisseção para encontrar o intervalo [r1, r2] com r2 - r1 = 0.01
        while (b - a) >= tol:
            # Encontre o ponto médio do intervalo
            c = (a + b) / 2

            # Calcule o valor da função no ponto médio
            fc = f(c)

            # Verifique se o ponto médio é a solução
            if fc == 0:
                break

            # Atualize o intervalo [a, b] com base no sinal de fc
            if f(a) * fc < 0:
                b = c
            else:
                a = c

        r1 = a
        r2 = b

        print(f"O intervalo (r1, r2) que possivelmente contém a solução é ({r1}, {r2}) com r2 - r1 = {r2 - r1:.2f}")    
        
# método de Newton-Raphson
def newtonRaphson(f, dfdx, x0, tol, maxIter):

    i = 0;
    x_k = [x0];
    y_k = [f(x0)];

    while(abs(f(x_k[-1])) > tol or i > maxIter):

        next_x = x_k[-1] - f(x_k[-1])/dfdx(x_k[-1]);
        
        x_k.append(next_x);
        y_k.append(f(next_x));
        i+=1
       # print(x_k);
        #print(y_k);    
 
    return x_k[-1];
def steffesen(f, x0, tol, maxIter):

    def g(x):
        return (f(x + f(x))/f(x)) - 1;

    i = 0;
    x_k = [x0];
    y_k = [f(x0)];

    while(abs(f(x_k[-1])) > tol or i > maxIter):

        next_x = x_k[-1] - f(x_k[-1])/g(x_k[-1]);
        
        x_k.append(next_x);
        y_k.append(f(next_x));

    # print(x_k);
    # print(y_k);    

    return x_k[-1];


def graph(a, b, c=1000):
    x = np.linspace(a, b, c)
    x = np.linspace(a, b, c)
    y_1 = f(x)
    y_2 = h(x)
    plt.plot(x, y_1, label="f1(x)")
    plt.plot(x, y_2, label="f2(x)")
    plt.grid(True)
    plt.show()

# a) 
find_interval(0.1*10**11, 1.48*10**11, 0.01)
# b)
print(bisec(f,147617750096.14825,147617750096.1561,0.001))
# c)
print(newtonRaphson(f,df_dr,10**5,0.001,100))
#d )
print(steffesen(f, 10**5, 0.001, 1000))
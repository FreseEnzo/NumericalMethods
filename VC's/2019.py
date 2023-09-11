'''

VC Cálculo Numérico: 12/09/2023 - Questão x
Nome: Enzo Gomes FRESE
Número: 21020
Turma A

'''

# importações das bibliotecas
import pandas as pd;
import matplotlib.pyplot as plt;

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
print("oi")
# método da bisseção
def bissection(f, d, xMin, xMax, tol, maxIter):

    i = 0;
    a = xMin;
    b = xMax;
    err = b - a;

    if(f(d, a) * f(d, b) > 0):
        return 'error';

    while((err > tol) and (i < maxIter)):

        x = (a + b)/2;

        if(f(d, x) * f(d, a) < 0):
            b = x;
        elif(f(d, x) * f(d, b) < 0):
            a = x;
        elif(f(d, x) == 0):
            return x;

        err = b - a;
        i += 1;

    return x;

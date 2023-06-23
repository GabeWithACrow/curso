def somar(x,y):
    resultado = x+y
    return resultado

def subtrair(x,y):
    resultado = x-y
    return resultado

def multiplicar(x,y):
    resultado = x*y
    return resultado

def dividir(x,y):
    resultado = x/y
    return resultado

def exponencial(x,y):
    resultado = x**y
    return resultado

def calcular(x,y):
    z=somar(x,y)
    t=(exponencial(x,y))**2
    w=dividir(x,y)
    u=multiplicar(x,y)
    resultado=(t/z)*(w/u)

    x=((exponencial(x,y)**2)/somar(x,y))*(dividir(x,y)/multiplicar(x,y))

    return x

if __name__ == "__main__":
    a = int(input("valor de a"))
    b = int(input("valor de b"))
    print("soma =", somar(a,b))
    print("subtrai =", subtrair(a,b))
    print("multiplica =", multiplicar(a,b))
    print("divide =", dividir(a,b))
    print("exponencial =", exponencial(a,b))
    print("calcular =", calcular(a,b))
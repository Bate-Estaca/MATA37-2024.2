meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto", "setembro","outubro","novembro","dezembro"]

def extendedData(dd,mm,aaaa):
    if (dd > 31) | (dd<0) | (mm>12) | (mm<0) |(aaaa<0):
        return None
    return "{} de {} de {}".format(dd,meses[mm-1],aaaa)


dd = int(input("Insira o dia: "))
mm = int(input("Insira o mês: "))
aaaa = int(input("Insira o ano: "))

print(extendedData(dd,mm,aaaa))

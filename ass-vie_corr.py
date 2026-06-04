def c(n):
    if n==0:
        return c0
    else:
        return ( (c(n-1)+12*m)*(1+t/100))
    
print("Calcul du capital/Interets quand les interets sont calculés une fois par an")
c0=int(input("ENtrez le placement de départ"))
m=int(input("Entrez le montant du versement mensuel:"))
t=float(input("Entrez le taux annuel en %"))
na=int(input("Entrez le nombre d'années"))
print("Le capital acquis avec interets est de",round(c(na),2), "euros au bous de", na ,"ans avec des versements mensuels de",m,"euros.")
print("Les interets gagnes au taux annuel de",t,"% sont de ", round(c(na)-na*m*12-c0,2),"euros")
print("Sans placement avec interets le capital acquis serait de",round(na*m*12+c0,2),"euros")
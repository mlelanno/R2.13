s=float(input("Entrez le montant du prêt ou crédit"))
t=float(input("Entrez le taux annuel en %"))
n=int(input("Entrez le nombre d'années"))

tm=t/12/100
a=(1+tm)**(12*n)
m=s*tm*a/(a-1)

print("la mensualité avec interets est de", round(m,2),"euros")
print("Le montant des interets remboursés sont de",round(m*12*n-s,2),"euros")
print("Le taux mensuel est de",tm)
print("\nTableau d'amortissement")
print("Mois - Mensualité - Intérêts - Capital remboursé - Capital restant du - Intérêts remboursés")
ir=0.0
for j in range(n*12):
    i=tm*s
    cr=m-i
    crd=s-cr
    ir=i+ir
    print("",j+1,"  -  ",round(m,1),"    -   ", round(i,1),"    -    ",round(cr,1),"        -        ",round(crd,1),"          -       ",round(ir,1))
    s=crd
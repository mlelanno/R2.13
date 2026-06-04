def calcul_placement():
    print("--- Question 1 : Intérêts calculés une fois par an ---")
    capital_dep = float(input("Entrer le placement de départ: "))
    versement_mensuel = float(input("Entrer le montant du versement mensuel: "))
    taux_annuel = float(input("Entrer le taux annuel en %: "))
    annees = int(input("Entrer le nombre d'années: "))

    # Calculation for Annual Compounding
    capital_annuel = capital_dep
    for annee in range(annees):
        # The academic model adds the whole year's deposits before calculating interest
        capital_annuel += (versement_mensuel * 12)
        capital_annuel = capital_annuel * (1 + (taux_annuel / 100))

    total_verse = capital_dep + (versement_mensuel * 12 * annees)
    interets_annuel = capital_annuel - total_verse

    print(f"Le capital acquis avec intérêts est de {round(capital_annuel, 2)} euros au bout de {annees} ans avec des versements mensuels de {int(versement_mensuel)} euros.")
    print(f"Les intérêts gagnés au taux annuel de {taux_annuel}% sont de {round(interets_annuel, 2)} euros.")
    print(f"Sans placement avec intérêts le capital acqui serait de {int(total_verse)} euros.\n")


    print("--- Question 2 : Intérêts calculés une fois par mois ---")
    # Calculation for Monthly Compounding
    capital_mensuel = capital_dep
    taux_mensuel = (taux_annuel / 100) / 12
    mois_total = annees * 12

    for mois in range(mois_total):
        capital_mensuel += versement_mensuel
        capital_mensuel = capital_mensuel * (1 + taux_mensuel)

    interets_mensuel = capital_mensuel - total_verse

    print(f"Le capital acquis avec intérêts est de {round(capital_mensuel, 2)} euros au bout de {annees} ans avec des versements mensuels de {int(versement_mensuel)} euros.")
    print(f"Les intérêts gagnés au taux annuel de {taux_annuel}% sont de {round(interets_mensuel, 2)} euros.")
    print(f"Sans placement avec intérêts le capital acqui serait de {int(total_verse)} euros.")

calcul_placement()
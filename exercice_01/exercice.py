produit="clavier"
prix_ht=19.90
quantité=3
taux_tva=0.2
total_ht=prix_ht*quantité
total_ttc=total_ht*(1+taux_tva)
print(f"Total TTC : {total_ttc:.2f} euros")
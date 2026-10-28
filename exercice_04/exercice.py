ventes = [
    {"produit": "café", "prix": 2.5, "quantite": 120},
    {"produit": "thé", "prix": 2.0, "quantite": 80},
    {"produit": "jus", "prix": 3.5, "quantite": 45},
]

ca_par_produit = {}
for vente in ventes:
    ca_par_produit[vente["produit"]] = vente["prix"] * vente["quantite"]
print(ca_par_produit)

total = sum(ca_par_produit.values())
print(f"Total : {total:.2f} euros")

meilleur_produit = ""
meilleur_ca = 0
for produit, ca in ca_par_produit.items():
    if ca > meilleur_ca:
        meilleur_ca = ca
        meilleur_produit = produit
print(f"Meilleur produit : {meilleur_produit}")
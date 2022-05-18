shopping_list = {
    'spożywczy': ['chleb', 'bułki', 'rogal'],
    'warzywniak': ['pomidory', 'cebula', 'ogórek'],
    'stacja benzynowa': ['benzyna', 'kawa']
    }

for k, v in shopping_list.items():
    print(f"Idę do {k.capitalize()} i kupuję tam {[item.capitalize() for item in v]}")
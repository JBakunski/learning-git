shopping_list = {
    'spożywczy': ['chleb', 'bułki', 'rogal'],
    'warzywniak': ['pomidory', 'cebula', 'ogórek'],
    'stacja benzynowa': ['benzyna', 'kawa']
    }

number_of_items = 0

for k, v in shopping_list.items():
    print(f"Idę do {k.capitalize()} i kupuję tam {[item.capitalize() for item in v]}")
    number_of_items += len(v)

print(f"W sumie kupuję {number_of_items} produktów.")

# Dodana modyfikacja

print("'Hiszpańska inkwizycja', to najlepszy skecz grupy Monty Pythona")

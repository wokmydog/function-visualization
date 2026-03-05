import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import functions

# vytvoření složky pro obrázky
os.makedirs("images", exist_ok=True)

# generování hodnot x
x = np.linspace(-10, 10, 1000)

# načtení funkcí z příkazové řádky
choices = sys.argv[1:]

if len(choices) == 0:
    print("Použití: python main.py linear sin quadratic exp custom")
    sys.exit()

plt.figure()
valid_choices = []

# projdeme všechny zadané funkce
for choice in choices:

    if choice == "linear":
        y = functions.linear(x, 2, 1)
        plt.plot(x, y, label="2x+1")
        valid_choices.append(choice)

    elif choice == "quadratic":
        y = functions.quadratic(x, 1, -2, 1)
        plt.plot(x, y, label="x²-2x+1")
        valid_choices.append(choice)

    elif choice == "sin":
        y = functions.sinus(x)
        plt.plot(x, y, label="sin(x)")
        valid_choices.append(choice)

    elif choice == "exp":
        y = functions.exponential(x)
        plt.plot(x, y, label="e^x")
        valid_choices.append(choice)

    elif choice == "custom":
        y = functions.custom(x)  # bezpečný log(|x| + 1)
        plt.plot(x, y, label="log(|x|+1)")
        valid_choices.append(choice)

    else:
        print(f"Neznámá funkce: {choice}")

# nastavení grafu
plt.title("Vybrané funkce")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# automatický název souboru podle vybraných funkcí
filename = "_".join(valid_choices) + ".png"
plt.savefig(f"images/{filename}")
plt.show()
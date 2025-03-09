# Importujemy moduł random do generowania losowych liczb
# Dokumentacja modułu random: https://docs.python.org/3/library/random.html
import random

try:
    # Tworzenie dwóch list z losowymi liczbami
    list1 = [random.randint(1, 10) for _ in range(5)]  # Lista z 5 losowymi liczbami (1-10)
    list2 = [random.randint(1, 10) for _ in range(5)]  # Druga lista z 5 losowymi liczbami (1-10)

    # Łączenie list za pomocą funkcji zip()
    # Dokumentacja zip(): https://docs.python.org/3/library/functions.html#zip
    zipped_list = list(zip(list1, list2))

    # Wypisanie wyników
    print("Lista 1:", list1)
    print("Lista 2:", list2)
    print("Połączone listy (zip):", zipped_list)

    # Użycie jednej funkcji z modułu random - np. random.choice()
    # Dokumentacja random.choice(): https://docs.python.org/3/library/random.html#random.choice
    random_pair = random.choice(zipped_list)
    print("Losowa para z połączonych list:", random_pair)

except Exception as e:
    # Obsługa potencjalnych wyjątków za pomocą try-except
    # Dokumentacja obsługi wyjątków: https://docs.python.org/3/tutorial/errors.html
    print("Wystąpił błąd:", e)

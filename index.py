from to_bin import to_bin as tb
from add_zero import add_zero as az
from reverse_bin import reverse as rvs
from two_complement import two_complement

number = int(input("Quel est l'entier dont vous voulez faire le complément à 2 ? "))
how_many_bits = int(input("Sur combien de bits souhaitez-vous encoder votre nombre entier ? "))

binary = tb(number)

if len(binary) > how_many_bits:
    print(f"Binary number inserted is over: {how_many_bits}")
elif number >= 0:
    result = az(binary, how_many_bits - len(binary))
    print(f"Le complément à 2 de l'entier {number} sur {how_many_bits} bits est {result}")
else:
    abs_binary = tb(abs(number))
    result = two_complement(rvs(az(abs_binary, how_many_bits - len(abs_binary))))
    print(f"Le complément à 2 de l'entier {number} sur {how_many_bits} bits est {result} ")
from reverse_bin import reverse

def two_complement(binary):
    binary = str(binary)
    binary = binary[::-1]
    first_zero = binary.index('0')
    sample = binary
    sample = reverse(sample[:first_zero+1])
    binary = sample + binary[len(sample):]
    binary = binary[::-1]

    return binary

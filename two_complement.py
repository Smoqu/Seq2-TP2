from reverse_bin import reverse

def two_complement(binary):
    binary = str(binary)
    binary = binary[::-1]
    for b in binary:
        b = int(b)
        if binary[b] == "0":
            rev = reverse("0")
            binary = binary.replace(binary[0], rev)
            break
        elif binary[b] == "1":
            rev = reverse("1")
            binary = binary.replace(binary[0], rev)
            # if binary[b+1] == "1":
            #     rev = reverse("1")
            #     binary.replace(binary[b+1], rev)
            # elif binary[b+1] == "0":
            #     rev = reverse("0")
            #     binary.replace(binary[b+1], rev)
            #     break
        print(b)

    return binary


print(two_complement("11110011"))
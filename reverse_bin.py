def reverse(binary):
    binar = ""
    for b in binary:
        if b == "0":
            binar += "1"
        elif b == "1":
            binar+= "0"
        else:
            return 'Number must be binary'
        
    return binar
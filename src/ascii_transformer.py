# This modules handles string to ascii transformation and vice versa 

# design -> basic encoding implementation
# what i think -> we have to find a better way 


def asciToString(number):
    string_number =  str(number)
    if string_number[0]!= '1':
        raise ValueError("invalid ascii message: don't have padding")
    string_number = string_number[1:]
    n = len(string_number)
    i = 0
    message = ""
    while i < n:
        ascii = string_number[i:i+3]
        message += chr(int(ascii))
        i+=3
    return message



def stringToasci(message):
    asci_message= ""
    for c in message:
        asci_c = ord(c)
        asci_message += f"{asci_c:03d}"
    return int('1' + asci_message)




# This function takes asci message and transform it to the actual message, the reason we need length
# because when the asci get transformed  to ind it could lose the first digits if they are 0.
# that's why we need tp remember the length so we can restore the 0s
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


#this a message to ascii encoding.
def stringToasci(message):
    asci_message= ""
    for c in message:
        asci_c = ord(c)
        asci_message += f"{asci_c:03d}"
    ##FLAG#### to save information we need. to add a way to save the first digits if they are
    ##added 1 as padding so we won't lost the first digits if they are 0 when we transofrm to int
    return int('1' + asci_message)

import base64
#written by Matt Sepela and Rasheed Elsaleh

def encrypt(message):
    z = bytearray(message, "ascii")
    m1 = int('11110000',2)
    m2 = int('00001111',2)
    encoded_message= ""
    for c in z:
        n1 = c & m1
        n2 = c & m2
        n1 = n1 >> 4
        n2 = n2 << 4
        t = n1 | n2
        encoded_message += hex(t)
    output = base64.b64encode(encoded_message)
    return output

def decrypt(input):
    """
    Write me!
    """

if __name__ == "__main__":
    t = encrypt(message)
    print t
    #printed encrypted message
    """
    Encrypted Message: MHg2NjB4YzYweDE2MHg3NjB4YjcweDM2MHgxNjB4ZTYweGY1MHg3NzB4NTYweGY1MHgzNzB4NDcweGY2MHg3MHhmNTB4NzcweDk2MHg0NzB4ODYweGY1MHhkNjB4NTYweGQ2MHg1NjB4MzcweGY1MHg3MHhjNjB4NTYweDE2MHgzNzB4NTYweGQ3
    """

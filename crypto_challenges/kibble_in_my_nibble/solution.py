import base64
#written by Matt Sepela and Rasheed Elsaleh

message = "flag{can_we_stop_with_memes_please}"

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
    t = base64.b64decode(input)
    r = [int(i,16) for i in t.split("0x") if i]
    decoded_message= ""
    m1 = int('11110000',2)
    m2 = int('00001111',2)
    for c in r:
        n1 = c & m1
        n2 = c & m2
        n1 = n1 >> 4
        n2 = n2 << 4
        decoded_message += chr(n1 | n2)
    return decoded_message


if __name__ == "__main__":
    t = encrypt(message)
    print(t)
    print(decrypt(t))

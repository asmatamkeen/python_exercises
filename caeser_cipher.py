import string 
alphabet=string.ascii_letters
def encryption():
    msg=input("Type your message:")
    shift=int(input("Type the shift number:"))
    result=''
    for X in msg:
        if X==" ":
            result+=" "
        else:
            msg_index=alphabet.find(X)
            x=(msg_index+shift) % 26
            result+=alphabet[x] 

    print(f"Here's the encrypted result:{result}")

def decryption():
    msg=input("Type your message:")
    shift=int(input("Type the shift number:"))
    result=''
    for X in msg:
        if X==" ":
            result+=" "
        else:
            msg_index=alphabet.find(X)
            x=(msg_index-shift)
            if x<0:
                x1=x+26
            else:
                x1=x 
            x2=x1 % 26
            result+=alphabet[x2]
    
    print(f"Here's the decrypted result:{result}")
    


def cipher():
    a=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:")
    if a=='encrypt':
        encryption()
    else:
        decryption()

cipher()

while True:
    b=input("Type 'yes' if you want to go again. Otherwise typr 'no':")
    if b=='yes':
        cipher()

    else:
        break




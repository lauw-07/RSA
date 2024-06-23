import math
def rsa(p, q):
    #Generate public key
    #Find Euler's Totient Function (etf)
    n = p*q
    etf = (p-1) * (q-1)
    #Generate private key
    pubExp = getPubExp(etf)
    publicKey, privateKey = generateKeys(n, etf, pubExp)
    print(f"Public Key: {publicKey}")
    print(f"Private Key: {privateKey}")
    #Encrypt
    plaintext = int(input(f"Enter the integer to encrypt (Must be between 0 and {n}): "))
    ciphertext = encryptRSA(publicKey, plaintext)
    print(f"Encrypted message: {ciphertext}")
    
    userInput = input("Do you want to decrypt the message? (Press Y for yes or enter for no): ")
    if userInput.upper() == "Y":
        decryptedMsg = decryptRSA(privateKey, ciphertext)
        print(f"Decrypted message: {decryptedMsg}")

def getGcd(a, b):
    if b == 0:
        return a
    return getGcd(b, a%b)

def getPubExp(etf):
    pubExp = int(input(f"Enter the Public Key Exponent (Must be a prime number between 0 and {etf}. Common choices include 3, 17, 65337): "))
    
    while (getGcd(pubExp, etf) != 1) or not (pubExp >= 0 and pubExp < etf): 
        pubExp = int(input("Invalid Exponent, Please try again: "))
    
    return pubExp

def extendedEuclideanAlgorithm(a, b):
    #Returns the gcd(a, b), x coefficient 
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extendedEuclideanAlgorithm(b, a%b)
    x = y1
    y = x1 - (a//b)*y1
    
    return gcd, x, y

def getModularMultiplicativeInverse(e, etf):
    gcd, x, y = extendedEuclideanAlgorithm(e, etf)
    if gcd != 1:
        raise Exception("No such Modular Multiplicative Inverse exists")
    else:
        return x%etf

def generateKeys(n, etf, pubExp):
    privExp = getModularMultiplicativeInverse(pubExp, etf)
    return (pubExp, n), (privExp, n)

def encryptRSA(publicKey, plaintext):
    pubExp, n = publicKey

    while not (plaintext > 0 and plaintext < n):
        plaintext = int(input(f"Must be between 0 and {n}. Please try again: "))

    ciphertext = pow(plaintext, pubExp, n)
    return ciphertext

def decryptRSA(privateKey, ciphertext):
    privExp, n = privateKey
    plaintext = pow(ciphertext, privExp, n)
    return plaintext

def checkPrime(num):
    if (num < 2):
        return False
    
    for i in range(2, math.floor(math.sqrt(num))):
        if num%i == 0:
            return False
        
    return True

def test():
    p = int(input("Please enter a value for p (Note must be prime): "))

    errorMsg = "Must be a prime number. Please try again: "
    while checkPrime(p) is not True:
        p = int(input(f"{errorMsg}"))
        
    q = int(input("Please enter a value for q (Note must be prime): "))    
    while checkPrime(q) is not True:
        q = int(input(f"{errorMsg}"))
        
    rsa(p, q)


def exampleQu1():
    print("\nQu 1")
    p, q, e, m = 53, 71, 97, 1579

    n = p*q
    etf = (p-1)*(q-1)

    pubKey, privKey = generateKeys(n, etf, e)
    c = encryptRSA(pubKey, m)
    print(f"c = {c}")

def exampleQu2():
    print("\nQu 2")
    p, q, e, c = 61, 53, 17, 2790

    n = p*q
    etf = (p-1)*(q-1)

    pubKey, privKey = generateKeys(n, etf, e)
    m = decryptRSA(privKey, c)
    print(f"m = {m}")

exampleQu1()
exampleQu2()
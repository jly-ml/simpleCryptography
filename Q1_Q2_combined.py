"""
JENNIFER LY
CSC 451
ASSIGNMENT 6
    """
import math

#GIVEN INFOMRATION
p = 19
q = 15
e = 11
m = 7

print('Given(s): m value = ', m, ' //  p value = ', p, ' // q value = ' , q, ' // e = ', e, ' // d =  ?')
print('')
#CALCULATONS
n = p*q
cipher = int(math.pow(m,e)% (p*q))
theta = (p-1) * (q-1)

print('Calculations Done: ')
print('Ciphertext/Ecryption = ', cipher)
print('(p-1)*(q-1) = ', theta)
print('')

#MAIN CALCULATION TO FIND 'D'
print('FACT: (e *d) mod ((p-1) * (q-1)) = 1')
for d in range(1,24):
   checker =  (e * d ) % theta
   if(checker == 1 ):
       print('FOUND IT, D VALUE IS: ', d)
       print('')
       break

   print('Invalid tested d value: ', d)

print('Verification + Decryption with calculated value of d')
print('(e *d) mod ((p-1) * (q-1)) = ', ((e*d) % theta))
print('Decryption: C^(d) mod 285 = ', pow(cipher,d,n))

print('Final Table: m value = ', m, ' //  p value = ', p, ' // q value = ' , q, ' // e = ', e, ' // d = ', d)


print('**********************QUESTION TWO**************************')
demokey = 15
alpha_key = ['a', 'b', 'c', 'd' ,'e', 'f', 'g','h',
             'i', 'j', 'k', 'l', 'm','n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encryptedstring = 'WTAAD'
encryptedhwk = "CLYFZLJBYL"
num_decrypted = []
num_encrypted = []

print('Sample Encrypted String: ', encryptedstring)

print(alpha_key.index('h'), 'heree')
print("Numerical Cipher Value: ", end='')
for x in encryptedstring.lower()
    num_encrypted.append(alpha_key.index(x))
    num_decrypted.append(pow(alpha_key.index(x)-demokey,1,26))

print('')
print('Encrypted Numerical Values', num_encrypted)
print('Decrypted Numerical Values: ', num_decrypted)
print('Decrypted Message: ', end='')
for x in num_decrypted:
    print(alpha_key[x], end='')


for test_dkey in range(0,26):
    num_decrypted = []
    num_encrypted = []

    for x in encryptedhwk.lower():
        num_encrypted.append(alpha_key.index(x))
        num_decrypted.append(pow(alpha_key.index(x) - test_dkey, 1, 26))
    print('')
    print('Encrypted Numerical Values', num_encrypted)
    print('Decrypted Numerical Values: ', num_decrypted)
    print('Decrypted Message: ', end='')
    for x in num_decrypted:
        print(alpha_key[x], end='')
    print('')
    print('with Key Value = ', test_dkey)
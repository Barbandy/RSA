# coding: UTF-8
import argparse
import random
import BigInt


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('inFile')
    return parser.parse_args()

	
# проверка простого числа	
def Test_Prime(n):
    if not MillerRabin(n):
        raise ValueError("The selected number is not simple.")

		
def powmod(a, k, n):
    res, aa, kk = BigInt.BigInt(1), a, k
    while kk != 0:
        if (kk % 2) == 1:
            res = (res * aa) % n
        aa = (aa * aa) % n
        kk /= 2
    return res
	
	
# применение расширенного алгоритма Евклида	
def GCD_ex(a, b):
    m = b
    x1 = BigInt.BigInt(0)
    x2 = BigInt.BigInt(1)
    y1 = BigInt.BigInt(1)
    y2 = BigInt.BigInt(0)
	
    while b != BigInt.BigInt(0):
        q = a / b
        r = a % b
        a = b
        b = r
		
        xx = x2 - x1 * q
        yy = y2 - y1 * q
        x2 = x1
        x1 = xx
        y2 = y1
        y1 = yy
    x = x2
    y = y2

    return (x+m)%m
		

# тест Миллера-Рабина
def MillerRabin(m):
    m = m.getString()
    m = int(m)
    t = m - 1
    s = 0
    while t % 2 == 0:
        t /= 2
        s += 1
            
    for i in range(20):
        #a = BigInt.GenerateRandomMax(m - 1)
        a = random.randint(1, m-1)
        x = pow(a, t, m)
        if x == 1:
            return True # составное
        i = BigInt.BigInt(0)
    for i in range(s - 1):
        x = pow(x, 2, m)
        if x == m - 1:
            return True
    return x == m - 1
				
		
# генерация ключей		
def KeyGen(p, q, e):	
    n = p * q
    fi = (p - BigInt.BigInt(1)) * (q - BigInt.BigInt(1))
    d = GCD_ex(e, fi)
    pub_key = "{}\n{}".format(e, n)
    print "pub_key = ", pub_key
    priv_key = "{}\n{}".format(d, n)
    print "priv_key = ", priv_key

    return n, d

		
def main():
    print "RSA"
    args = getArgs()
	
    msg = BigInt.BigInt()
    msg.getFrom_txt(args.inFile)
	
    p = BigInt.BigInt()
    q = BigInt.BigInt()
    e = BigInt.BigInt()
	
    p.getFrom_txt("p.txt")
    q.getFrom_txt("q.txt")
    e.getFrom_txt("e.txt")

    Test_Prime(p)
    Test_Prime(q)
    Test_Prime(e)
	
    n, d = KeyGen(p, q, e)
    print "text = ", msg
    msg = BigInt.BigInt(str(msg))
    c =  powmod(msg, e, n)
    print "encrypt_text = ", c
    text = powmod(c, d, n)
		
    print "decrypt_text = ", text
    
    if msg == text:
        print"Success!"
    else:
        print "Failure!"

if __name__ == "__main__":
    main()	
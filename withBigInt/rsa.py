# coding: UTF-8
import argparse
import random
import BigInt


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('inFile')
    parser.add_argument('outFile')
    parser.add_argument('mode', choices=['e', 'd'])
    return parser.parse_args()


def GeneratePrime(bitLen):
    p = BigInt.GenerateRandomLen(bitLen)
    while not MillerRabin(p):
        p += 1
    return p	

	
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
    s = BigInt.BigInt(0)
    while t % 2 == 0:
        t /= 2
        s += 1
       
    for step in range(20):
        #a = BigInt.GenerateRandomMax(m-1)
        a = random.randint(1, m-1)
        x = pow(a, t, m)
        if x == 1:
            return True # составное
    i = BigInt.BigInt(0)
    while i < s - 1:
        x = (x * x) % m
        if x == m - 1:
            return True
        i = i + 1
    return x == m - 1
				
		
# генерация ключей		
def KeyGen(bitlen):
    p = BigInt.BigInt()
    q = BigInt.BigInt()
    e = BigInt.BigInt()
    p = GeneratePrime(bitlen)
    q = GeneratePrime(bitlen)
    while p == q:
        q = GeneratePrime(bitlen)
    e = GeneratePrime(40)	
    n = p * q
    fi = (p - BigInt.BigInt(1)) * (q - BigInt.BigInt(1))
    d = GCD_ex(e, fi)
    pub_key = "{}\n{}".format(e, n)
    priv_key = "{}\n{}".format(d, n)
  
    return pub_key, priv_key, n, d, e

		
def main():
    print "RSA"
    args = getArgs()
    bitlen = 1024	
    msg = BigInt.BigInt()
    msg.getFrom_txt(args.inFile)
    if 	args.mode == "e":
        pub_key, priv_key, n, d, e = KeyGen(bitlen)
        msg = BigInt.BigInt(str(msg))
        c =  powmod(msg, e, n)
        c.saveTo_txt(args.outFile)
        with open('pub.key', 'w') as pub:
            pub.write(pub_key)
        with open('priv.key', 'w') as priv:
            priv.write(priv_key)

    if args.mode == "d":   
        c = BigInt.BigInt()
        with open('priv.key') as priv:
            (d, n) = priv.read().split("\n") 
        d = BigInt.BigInt(d)
        n = BigInt.BigInt(n)     
        c.getFrom_txt(args.outFile)
        text = powmod(c, d, n)
        text.saveTo_txt("res.txt")
		
if __name__ == "__main__":
    main()	
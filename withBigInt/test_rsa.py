#coding: UTF-8
import random, pytest, rsa, BigInt


def GeneratePrime(bitLen):
    p = BigInt.GenerateRandomLen(bitLen)
    while not rsa.MillerRabin(p):
        p += 1
    return p


def test_rsa():
    msg = BigInt.BigInt()
    p = BigInt.BigInt()
    q = BigInt.BigInt()
    e = BigInt.BigInt()
    p = GeneratePrime(1024)
    q = GeneratePrime(1024)
    e = GeneratePrime(40)
    n, d = rsa.KeyGen(p, q, e)
    msg = BigInt.GenerateRandomMax(n-1)
    msg = BigInt.BigInt(str(msg))
    c =  rsa.powmod(msg, e, n)
    text = rsa.powmod(c, d, n)
    assert msg == text

	




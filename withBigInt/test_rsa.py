#coding: UTF-8
import random, pytest, rsa, BigInt


def test_rsa():
    msg = BigInt.BigInt()
    n = BigInt.BigInt()
    d = BigInt.BigInt()
    pub, priv, n, d, e = rsa.KeyGen(1024)
    msg = BigInt.GenerateRandomMax(n-1)
    msg = BigInt.BigInt(str(msg))
    c =  rsa.powmod(msg, e, n)
    text = rsa.powmod(c, d, n)
    assert msg == text
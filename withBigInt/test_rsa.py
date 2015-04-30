#coding: UTF-8
import pytest, rsa, BigInt
from hypothesis import given
#from hypothesis.searchstrategy import BasicStrategy


@given(str, int, int, int)
def test_md5(data, p, q, e):
    
    msg = BigInt.BigInt()
    msg = data
    n, d = rsa.KeyGen(p, q)
    msg = BigInt.BigInt(str(msg))
    c =  rsa.powmod(msg, e, n)
    text = rsa.powmod(c, d, n)	
    assert msg == text

	
#print strategy(Bitfields).example()	


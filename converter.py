from decimal import Decimal
from forex_python.converter import CurrencyRates,CurrencyCodes

def convert(cur1,cur2,amount):
    code = getCode(cur2)
    rate = getRate(cur1,cur2,amount)
    return f'{code} {rate:.2f}'

def getRate (cur1,cur2,amount):
    r = CurrencyRates()
    rate= r.convert(cur1,cur2,Decimal(amount))
    return rate
    

def getCode(curCode):
    c = CurrencyCodes()
    code = c.get_symbol(curCode)
    return code
print(convert('USD','EUR',200))
from decimal import Decimal
from forex_python.converter import CurrencyRates,CurrencyCodes
#single functionality function
def checkCur(cur):
        c = CurrencyRates() 
        if len(cur)<1:return 'Empty currency input'
        try:
                c.get_rates(cur) 
                return True
        except:
                return f'Invalid currency:{cur}'
def checkAmount(amount):
        if len(amount)<1:return 'Empty amount input'
        try:
                amtType = float(amount)
                return True if amtType >=0 else f'Negative amount: {amount}'
        except:
                return f'Invalid input: {amount}'
def getRate (cur1,cur2,amount):
        r = CurrencyRates()
        rate= r.convert(cur1,cur2,Decimal(amount))
        return rate

def getCode(curCode):
        c = CurrencyCodes()
        code = c.get_symbol(curCode)
        return code

#combine functions

def convert(cur1,cur2,amount):
        rate = getRate(cur1,cur2,amount)
        code = getCode(cur2)
        return f'{code} {rate:.2f}'

def check(arr,amount):
        message =[]
        for cur in arr:
                if checkCur(cur) is not True:
                        message.append(checkCur(cur))
        if checkAmount(amount) is not True:
                message.append(checkAmount(amount))
        return message


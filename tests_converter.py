from unittest import TestCase
from converter import checkAmount,checkCur,check,getCode,getRate,convert

class Converter(TestCase):
    """Examples of unit tests."""

    def checkAmtTest(self):
        self.assertEqual(checkAmount(),'Empty currency input')
        self.assertEqual(checkAmount(-1),'Negative amount -1')
        self.assertEqual(checkAmount('BNA'),'Invalid input: BNA')
        self.assertTrue(checkAmount('20'))
        self.assertTrue(checkAmount(20))
        self.assertTrue(checkAmount(0))
        self.assertTrue(checkAmount(10000000))
    def checkCurTest(self):
        self.assert
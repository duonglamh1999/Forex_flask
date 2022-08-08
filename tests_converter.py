from unittest import TestCase
from converter import checkAmount,checkCur,check,convert
from app import app
class Converter(TestCase):
    """Examples of unit tests."""
    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
    def checkAmtTest(self):
        self.assertEqual(checkAmount(),'Empty amount input')
        self.assertEqual(checkAmount(-1),'Negative amount -1')
        self.assertEqual(checkAmount('BNA'),'Invalid input: BNA')
        self.assertTrue(checkAmount('20'))
        self.assertTrue(checkAmount(20))
        self.assertTrue(checkAmount(0))
        self.assertTrue(checkAmount(10000000))
    def checkCurTest(self):
        self.assertEqual(checkCur(),'Empty currency input')
        self.assertEqual(checkCur('BNA'),'Invalid input: BNA')
        self.assertEqual(checkCur('20'),'Invalid input: 20')
        self.assertTrue(checkCur('USD'))
        self.assertTrue(checkCur('EUR'))
    def checkConvert(self):
        self.assertEqual(convert('USD','USD',1),'$ 1.00')
        self.assertEqual(convert('USD','USD',1.000),'$ 1.00')
    
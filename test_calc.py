import unittest
from test_suite import *
import test_suite

class TestCalc(unittest.TestCase):

    def test_add(self):
        """ Testing addition operation """

        self.assertEqual(int(test_suite.addition('5', '6')), 11)
        self.assertEqual(int(test_suite.addition('-55', '-67')), -122)
        self.assertEqual(int(test_suite.addition('012', '08')), 20)
        self.assertEqual(int(test_suite.addition('012', '028')), 40) # This is a bug
        self.assertEqual(int(test_suite.addition('012', '0')), 12) # This is a bug
        self.assertEqual(int(test_suite.addition('', '924')), 924)
        self.assertEqual(int(test_suite.addition('2345', '')), 2345)
        self.assertEqual(test_suite.addition('', ''), "ERR")

    def test_subtraction(self):
        """ Testing subtraction operation """

        self.assertEqual(int(test_suite.subtraction('13', '6')), 7)
        self.assertEqual(int(test_suite.subtraction('48', '76')), -28)
        self.assertEqual(int(test_suite.subtraction('055', '05')), 50) #This is a bug
        self.assertEqual(int(test_suite.subtraction(0, '34')), -34)
        self.assertEqual(int(test_suite.subtraction('', '924')), -924)
        self.assertEqual(int(test_suite.subtraction('987', '')), 987)
        self.assertEqual(test_suite.subtraction('', ''), "ERR")

    def test_multiplication(self):
        """ Testing multiplication operation """

        self.assertEqual(int(test_suite.multiplication('9', '7')), 63)
        self.assertEqual(int(test_suite.multiplication('23', '-87')), -2001)
        self.assertEqual(int(test_suite.multiplication('093', '039')), 3627)
        self.assertEqual(test_suite.multiplication('', '924'), "ERR")
        self.assertEqual(test_suite.multiplication('987', ''), "ERR")
        self.assertEqual(test_suite.multiplication('', ''), "ERR")

    def test_division(self):
        """ Testing division operation """

        self.assertEqual(int(test_suite.division('9', '3')), 3)
        self.assertEqual(int(test_suite.division('-480', '6')), -80)
        self.assertEqual(int(test_suite.division('099', '011')), 9) # This is a bug
        self.assertEqual(test_suite.division('38', '0'), "Infinity")
        self.assertEqual(test_suite.division('', '924'), "ERR")
        self.assertEqual(test_suite.division('987', ''), "ERR")
        self.assertEqual(test_suite.division('', ''), "ERR")

    def test_delete(self):
        """ Testing DEL button """

        self.assertEqual(test_suite.delete_button("2345+45=++++---="), "")
        self.assertEqual(test_suite.delete_button("++++---="), "")

if __name__ == "__main__":

    unittest.main()



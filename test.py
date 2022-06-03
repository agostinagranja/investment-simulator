import unittest
import FinanceTools as f

class BlackBoxTest(unittest.TestCase):

    # A) principal and contributions > 0 -> both capitalized
    def test_A(self):
        principal = 1000
        contribution = 500
        compounding_periods = 10

        result = f.get_final_capital(principal,contribution,compounding_periods)
        expected = (88119.04,1.97)

        self.assertEqual(result,expected)

    # B) principal > 0 and contributions = 0 -> only principal capitalized
    def test_B(self):
        principal = 1000
        contribution = 0
        compounding_periods = 10

        result = f.get_final_capital(principal,contribution,compounding_periods)
        expected = (1972.74,1.97)

        self.assertEqual(result,expected)
    
    # C) principal = 0 and contributions > 0 -> only contributions capitalized
    def test_C(self):
        principal = 0
        contribution = 500
        compounding_periods = 10

        result = f.get_final_capital(principal,contribution,compounding_periods)
        expected = (86146.29,0)

        self.assertEqual(result,expected)
    
    # D) principal and contributions = 0 -> 0
    def test_D(self):
        principal = 0
        contribution = 0
        compounding_periods = 10

        result = f.get_final_capital(principal,contribution,compounding_periods)
        expected = (0,0)

        self.assertEqual(result,expected)
    
    # E) compounding periods = 0 -> 0
    def test_E(self):
        principal = 1000
        contribution = 500
        compounding_periods = 0

        result = f.get_final_capital(principal,contribution,compounding_periods)
        expected = (1000,1)

        self.assertEqual(result,expected)

    # F) parameters < 0 -> raises ValueError
    def test_F(self):
        principal = -1000
        contribution = 0
        compounding_periods = 0

        self.assertRaises(ValueError,f.get_final_capital,principal,contribution,compounding_periods)

    # G) parameters != integer -> raises ValueError
    def test_G(self):
        principal = True
        contribution = 0
        compounding_periods = 0

        self.assertRaises(ValueError,f.get_final_capital,principal,contribution,compounding_periods)
       
unittest.main(argv=[''], verbosity=2, exit=False)

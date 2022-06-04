import unittest

from .token_with_escape import token_with_escape
from .token_with_escape_mutant1 import token_with_escape_mutant1
from .token_with_escape_mutant2 import token_with_escape_mutant2

class CoverageTests(unittest.TestCase):
    def test_statement_coverage(self):
        """Add tests to achieve statement coverage (as many as needed)."""
        # YOUR CODE HERE
        print(token_with_escape('one^|uno||three^^^^|four^^^|^cuatro|'))



    def test_kill_mutant_1(self):
        """Kill mutant 1"""
        #Test the 1st mutant here.
        print(token_with_escape_mutant1('one^|uno||three^^^^|four^^^|^cuatro|'))


        # Code here
        print('Print the execution of test_kill_mutant_1(design_input)')
        text1 = token_with_escape('one^|uno||three^^^^|four^^^|^cuatro|')
        text2 = token_with_escape_mutant1('one^|uno||three^^^^|four^^^|^cuatro|')
        message = "values are not equal"
        self.assertEqual(text1,text2,message)


        #print(token_with_escape_mutant1('one^|uno||three^^^^|four^^^|^cuatro|'))


    def test_kill_mutant_2(self):
        """Kill mutant 2"""
        # print(token_with_escape_mutant2('one^|uno||three^^^^|four^^^|^cuatro|'))


        # code here
        print('Print the execution of test_kill_mutant_2(design_input)')
        text3 = token_with_escape('one^|uno||three^^^^|four^^^|^cuatro|')
        text4 = token_with_escape_mutant2('one^|uno||three^^^^|four^^^|^cuatro|')
        message = "values are not equal"
        self.assertEqual(text3,text4,message)


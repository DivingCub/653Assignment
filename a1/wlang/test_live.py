import unittest

from . import ast, live


class TestLive(unittest.TestCase):
    def test_one(self):
        prg1 = "x := 10; if x > 10 then y:= 10 else y := 5 ; print_state"
        ast1 = ast.parse_string(prg1)


        v = live.StmtCounter1()
        c = v.visit(ast1)
        self.assertEqual(c,5)




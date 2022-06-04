
from . import ast


def main():
    ast1 = ast.parse_string('x := 10; y:= 20; z := x+y ; print_state ')
    print(ast1)
    # print(list(ast1.stmst))

    #count the statement number

    print("This program has:" , len(list(ast1.stmts)), "statement")


class StmtCounter1(ast.AstVisitor):

        def __init__(self):
            super().__init__()


        def visit_StmtList(self , node , *args , **kwargs):
            res = 0
            for s in node.stmts:
                res += self.visit(s, *args , **kwargs)

            return res

            # return len(list(node.stmts))

        def visit_IfStmt(self, node, *args, **kwargs):
            res =  self.visit_Stmt(self , node , *args , **kwargs )
            res += self.visit(node.then_stmt , *args , **kwargs )
            res += self.visit(node.else_stmt , *args , **kwargs )
            return res

        def visit_Stmt(self,node,*args,**kwargs):
            return 1






if __name__ == '__main__':
    main()

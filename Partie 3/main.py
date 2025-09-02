from opération import basic_ops
from opération import advanced_ops

def do_op(a,op,b):
    if op == "+":
        return basic_ops.add(a,b)
    if op == "-":
        return basic_ops.subtract(a,b)
    if op == "/":
        return advanced_ops.safe_divide(a,b)
    if op == "*":
        return advanced_ops.multiply(a,b)


print(do_op(0,"/",10))

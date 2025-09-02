def safe_divide(a,b):
    result=a/b
    print(result)

try: safe_divide(15,2)
except ZeroDivisionError as err:
    print("Impossible de diviser par zéro")


# Else with try except finally
try:
    print("from try block")
except :
    print("from except")
else:
    print("from else")
finally:
    print("from finally")

# from try block
# from else
# from finally


try:
    print(10/0)
    print("from try block")
except :
    print("from except")
else:
    print("from else")
finally:
    print("from finally")

# from except
# from finally
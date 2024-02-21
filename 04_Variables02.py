
"""
    x = "Mola"
def myFun():
    x = "Es mucho"
    print("Phyton ",x)
myFun()
"""

x = "Mola"
def myFun():
    global x
    x = "es mucho"
myFun()
print("Python" + x)

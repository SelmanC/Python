

class calc:
    test_string = "Hallo Welt!"
    
    @staticmethod
    def plus(a, b):
        return a+b
    
    @staticmethod
    def minus(a,b):
        return a-b
    
    

a = int(input("Erste Zahl: "))
b = int(input("Zweite Zahl: "))

print("\nStatisch:")
print("Plus:",str(calc.plus(a, b)))
print("Minus:", str(calc.minus(a, b)))

print("\nNicht Statisch:")

cal = calc()

print("Plus:",str(cal.plus(a, b)))
print("Minus:", str(cal.minus(a, b)))

print("\nAlter String Statisch:",calc.test_string)
print("\nAlter String Nicht Statisch:",cal.test_string)

calc.test_string = "Hallo Informatik Gruppe"

print("\nNeuer String Statisch:",calc.test_string)
print("\nNeuer String Nicht Statisch:",cal.test_string)

calc.test_string = "Hallo Welt 2"

print("\nGanz neuer String Statisch:",calc.test_string)
print("\nGanz neuer String Nicht Statisch:",cal.test_string)

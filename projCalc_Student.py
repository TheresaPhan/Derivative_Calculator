from sympy import *


x = Symbol("x")


def powerRule(): 
    print("This is the power rule. Using this format, you can identify problems that need product rules: ")
    coe_Num = int(input(" Enter the coefficient of your function, such as ax, where a is the coefficient: " ))
    power_Num = int(input(("Now enter the power. such as x^2: ")))
    real_deriv = diff(coe_Num * (x**power_Num),x)
   
    print( "Original Function: " + str(x**power_Num))
    print("Derivative: " + str(real_deriv))
    

def productRule(): 
    print("Product Rule","Enter based on the following format. With this, you can easily identify the product rule as well: \n(ax^b)(cx^d) ")
   
    coeNumA = int(input("Enter the coeffiecient,a, of the first part of your equation: "))
    powerNumA = int(input("Enter the power,b, of the first part of your equation: "))
    coeNumB = int(input("Enter the coefficient,c, of the second part of your eqation: "))
    powerNumB = int(input("Enter the power,d, of the second part of your equation: "))
    
    realderiv = diff((coeNumA * (x**powerNumA)) * (coeNumB * (x**powerNumB)),x)
   
    print("Original Function: " + str((coeNumA * (x**powerNumA)) * (coeNumB * (x**powerNumB))))
    print("Derivative: " + str(realderiv))

def quotientRule(): 
    tkinter.messagebox.showinfo("Quotient Rule","Enter based on the following format. With this, you can easily identify the quotient rule: \n (ax^b)/(cx^d)" )
    
    a = int(input("Enter the coeffiecient,a, of the first part of your equation: "))
    b = int(input("Enter the power,b, of the first part of your equation: "))
    c = int(input("Enter the coefficient,c, of the second part of your eqation: "))
    d = int(input("Enter the power d, of the second part of your equation: "))
    
    realDeriv = diff((a * (x**b))/(c * (x**d)),x)
    int(input( "Original Function: " + str((a * (x**b))/(c * (x**d)))))
    int(input("Dervative: " + str(realDeriv)))

def trigDeriv(): 
    print( "You are about to find the derivative of a trig function")
    print("From the list, choose a trig function and type its corresponding number:")
    
    trigSel = input( "1:sin(x), 2: cos(x), 3: tan(x), 4: csc(x), 5: sec(x), 6: cot(x)")
    
    coeNum = int(input("Enter the coefficient, such as 2sin(x) or 3cos(x): "))
    a = int(input("Enter the number inside the function, such as cos(2x)): "))
    b = int(input("Enter the power inside the function, such as cos(x**2)"))
    c = int(input("Enter the power on the outside of the function, such as (cos(x)**2)"))
    
    trigs = {"1": (coeNum * sin(a*(x**b)))**c, "2": (coeNum * cos(a*(x**b)))**c, "3": (coeNum * tan(a*(x**b)))**c, "4": (coeNum * csc(a*(x**b)))**c, "5": (coeNum * sec(a*(x**b)))**c,"6": (coeNum * cot(a*(x**b)))**c}#tangent and cotangent written in trig identity form 
    
    
    realderiv = diff(trigs[trigSel],x)
    print("Original Function", "Function: " +str(trigs[trigSel]))
    print("Dervative","Derivative: " + str(realderiv))  

    
def inverseTrig(): #review
    print("InverseTrig", "You are about to find the derivative of inverse trig functions.")
   
    print("From the list, choose a trig function and type its corresponding number: ")
    inTrigSel = input( "1:arcsin(x), 2: arccos(x), 3: arctan(x), 4: arccsc(x), 5: arcsec(x), 6: arccot(x) ")
    
    coeNum = int(input("Coefficient","Enter the coefficient, such as 2asin(x) or 3arccos(x): "))
    b = int(input("Inside Coefficient","Enter the number inside the function, such as arccos(2x)): "))
    c = int(input("Inside Power", "Enter the power inside the function, such as arccos(x**2)"))
    
    inTrigs = {"1": coeNum * asin(b*(x**c)), "2": coeNum * acos(b*(x**c)), "3": coeNum * atan(b*(x**c)), "4": coeNum * acsc(b*(x**c)), "5": coeNum * asec(b*(x**c)),"6": coeNum * acot(b*(x**c))}#1 + tan(x)^2 is equal to sec(x)
    
    
    realderiv = diff(inTrigs[inTrigSel],x)
    print( "Function: " + str(inTrigs[inTrigSel]))
    print("Derivative: " + str(realderiv)) 


def natLog(): 
    print("You are about to find the derivative of natural log functions")
    a = int(input("Enter the coefficient of your function, such as aln(x), where a is the coefficient: " ))    
    coe_Num = int(input("Coefficient Inside","Enter the coefficient of your function, such as ln(b*x), where b is the coefficient: " ))
    insidePow = int(input("Power","Now enter the inside power such as ln(x^2): " ))
    outsidePow = int(input("Power Outside", "Now enter the outsdie power, such as (ln(x))**2"))

    real_deriv = diff(ln(coe_Num*(x**insidePow)),x) * a
    
    print("Function: " + str(ln(coe_Num*(x**insidePow))))
    print("Your derivative is: " + str(real_deriv))


derivType = {"POWER RULE": powerRule, "PRODUCT RULE" : productRule, "QUOTIENT RULE" : quotientRule, "TRIG DERIVATIVES": trigDeriv, "INVERSE TRIG" : inverseTrig,"NATURAL LOG" :natLog}


def truDeriv(): #seeing if input is true and in the list
    print("Before we begin, here are the meanings of different math operators. x^.5 is the square root of x. x**2 is x squared. Sec(x)**2 is written as tan(x)**2 + 1, and -csc(x)**2 is written as cot(x)**2.")
    userDeriv = input("What derivative stradegy do you need help on? Product rule, quotient rule, power rule, trig derivatives, inverse trig, or natural log?: ")

    while (userDeriv.upper()) not in derivType:
        userDeriv = input("ERROR","Please check your spelling and try again: ")
    derivType[userDeriv.upper()]()
       
truDeriv()
        


from sympy import *

from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

x = Symbol("x")
root = Tk()
w = Label(root, text= "Derivative Calculator")
w.pack()

def powerRule(): 
    tkinter.messagebox.showinfo("Power Rule","This is the power rule. Using this format, you can identify problems that need product rules: ")
    coe_Num = tkinter.simpledialog.askinteger("Coefficient"," Enter the coefficient of your function, such as ax, where a is the coefficient: " )
    power_Num = tkinter.simpledialog.askinteger("Power","Now enter the power. such as x^2: ")
    real_deriv = diff(coe_Num * (x**power_Num),x)
   
    tkinter.messagebox.showinfo("Function", "Original Function: " + str(x**power_Num))
    tkinter.messagebox.showinfo("Derivative","Derivative: " + str(real_deriv))
    

def productRule(): 
    tkinter.messagebox.showinfo("Product Rule","Enter based on the following format. With this, you can easily identify the product rule as well: \n(ax^b)(cx^d) ")
   
    coeNumA = tkinter.simpledialog.askfloat("Coefficient A","Enter the coeffiecient,a, of the first part of your equation: ")
    powerNumA = tkinter.simpledialog.askfloat("Power A","Enter the power,b, of the first part of your equation: ")
    coeNumB = tkinter.simpledialog.askfloat("Coefficient B","Enter the coefficient,c, of the second part of your eqation: ")
    powerNumB = tkinter.simpledialog.askfloat("Power B","Enter the power,d, of the second part of your equation: ")
    
    realderiv = diff((coeNumA * (x**powerNumA)) * (coeNumB * (x**powerNumB)),x)
   
    tkinter.messagebox.showinfo("Fuction","Original Function: " + str((coeNumA * (x**powerNumA)) * (coeNumB * (x**powerNumB))))
    tkinter.messagebox.showinfo("Derivative","Derivative: " + str(realderiv))

def quotientRule(): 
    tkinter.messagebox.showinfo("Quotient Rule","Enter based on the following format. With this, you can easily identify the quotient rule: \n (ax^b)/(cx^d)" )
    
    a = tkinter.simpledialog.askfloat("Coefficient A","Enter the coeffiecient,a, of the first part of your equation: ")
    b = tkinter.simpledialog.askfloat("Power","Enter the power,b, of the first part of your equation: ")
    c = tkinter.simpledialog.askfloat("Coefficient","Enter the coefficient,c, of the second part of your eqation: ")
    d = tkinter.simpledialog.askfloat("Power","Enter the power d, of the second part of your equation: ")
    
    realDeriv = diff((a * (x**b))/(c * (x**d)),x)
    tkinter.messagebox.showinfo("Function", "Original Function:" + str((a * (x**b))/(c * (x**d))))
    tkinter.messagebox.showinfo("Dervative", str(realDeriv))

def trigDeriv(): 
    tkinter.messagebox.showinfo("Trig", "You are about to find the derivative of a trig function")
    tkinter.messagebox.showinfo("Function Selection","From the list, choose a trig function and type its corresponding number:")
    
    trigSel = tkinter.simpledialog.askstring("Function Selection", "1:sin(x), 2: cos(x), 3: tan(x), 4: csc(x), 5: sec(x), 6: cot(x)")
    
    coeNum = tkinter.simpledialog.askfloat("Coefficient","Enter the coefficient, such as 2sin(x) or 3cos(x): ")
    a = tkinter.simpledialog.askfloat("Inside Coefficient","Enter the number inside the function, such as cos(2x)): ")
    b = tkinter.simpledialog.askfloat("Inside Power","Enter the power inside the function, such as cos(x**2)")
    c = tkinter.simpledialog.askfloat("Outside Power", "Enter the power on the outside of the function, such as (cos(x)**2)")
    
    trigs = {"1": (coeNum * sin(a*(x**b)))**c, "2": (coeNum * cos(a*(x**b)))**c, "3": (coeNum * tan(a*(x**b)))**c, "4": (coeNum * csc(a*(x**b)))**c, "5": (coeNum * sec(a*(x**b)))**c,"6": (coeNum * cot(a*(x**b)))**c}#tangent and cotangent written in trig identity form 
    
    
    realderiv = diff(trigs[trigSel],x)
    tkinter.messagebox.showinfo("Original Function", "Function: " +str(trigs[trigSel]))
    tkinter.messagebox.showinfo("Dervative","Derivative: " + str(realderiv))  

    
def inverseTrig(): #review
    tkinter.messagebox.showinfo("InverseTrig", "You are about to find the derivative of inverse trig functions.")
   
    tkinter.messagebox.showinfo("Inverse Trig Selection","From the list, choose a trig function and type its corresponding number: ")
    inTrigSel = tkinter.simpledialog.askstring("Inverse Trig Selection", "1:arcsin(x), 2: arccos(x), 3: arctan(x), 4: arccsc(x), 5: arcsec(x), 6: arccot(x) ")
    
    coeNum = tkinter.simpledialog.askfloat("Coefficient","Enter the coefficient, such as 2asin(x) or 3arccos(x): ")
    b = tkinter.simpledialog.askfloat("Inside Coefficient","Enter the number inside the function, such as arccos(2x)): ")
    c = tkinter.simpledialog.askfloat("Inside Power", "Enter the power inside the function, such as arccos(x**2)")
    
    inTrigs = {"1": coeNum * asin(b*(x**c)), "2": coeNum * acos(b*(x**c)), "3": coeNum * atan(b*(x**c)), "4": coeNum * acsc(b*(x**c)), "5": coeNum * asec(b*(x**c)),"6": coeNum * acot(b*(x**c))}#1 + tan(x)^2 is equal to sec(x)
    
    
    realderiv = diff(inTrigs[inTrigSel],x)
    tkinter.messagebox.showinfo("Original Function", "Function: " + str(inTrigs[inTrigSel]))
    tkinter.messagebox.showinfo("Derivative","Derivative: " + str(realderiv)) 


def natLog(): 
    tkinter.messagebox.showinfo("Natural log","You are about to find the derivative of natural log functions")
    a = tkinter.simpledialog.askfloat("Coefficient Outside","Enter the coefficient of your function, such as aln(x), where a is the coefficient: " )    
    coe_Num = tkinter.simpledialog.askfloat("Coefficient Inside","Enter the coefficient of your function, such as ln(b*x), where b is the coefficient: " )
    insidePow = tkinter.simpledialog.askfloat("Power","Now enter the inside power such as ln(x^2): " )
    outsidePow = tkinter.simpledialog.askflaot("Power Outside", "Now enter the outsdie power, such as (ln(x))**2")

    real_deriv = diff(ln(coe_Num*(x**insidePow)),x) * a
    
    tkinter.messagebox.showinfo("Original Function","Function: " + str(ln(coe_Num*(x**insidePow))))
    tkinter.messagebox.showinfo("Derivative","Your derivative is: " + str(real_deriv))


derivType = {"POWER RULE": powerRule, "PRODUCT RULE" : productRule, "QUOTIENT RULE" : quotientRule, "TRIG DERIVATIVES": trigDeriv, "INVERSE TRIG" : inverseTrig,"NATURAL LOG" :natLog}


def truDeriv(): #seeing if input is true and in the list
    tkinter.messagebox.showinfo("Caution","Before we begin, here are the meanings of different math operators. x^.5 is the square root of x. x**2 is x squared. Sec(x)**2 is written as tan(x)**2 + 1, and -csc(x)**2 is written as cot(x)**2.")
    userDeriv = tkinter.simpledialog.askstring("Derivative Types","What derivative stradegy do you need help on? Product rule, quotient rule, power rule, trig derivatives, inverse trig, or natural log?: ")

    while (userDeriv.upper()) not in derivType:
        userDeriv = tkinter.simpledialog.askstring("ERROR","Please check your spelling and try again: ")
    derivType[userDeriv.upper()]()

       
truDeriv()
        


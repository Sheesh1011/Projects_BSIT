import os 
import textwrap
import run
import time
red = "\033[31m" #main title
green = "\033[32m" #comment
yellow = "\033[33m" #sub and output
blue = "\033[34m" #example and "main menu"
reset = "\033[0m"

name = input("\nWhat is your name? ")
print(f"\nHello👋🏻! {name.title()}")
print("Welcome to my Interactive Menu Program!")
time.sleep(1.4)

while True:
        os.system('cls')
        run.square_loading()
        os.system('cls')
        print("\n======= ",blue+"MAIN MENU"+reset," =======")
        print("1 - Data Types")
        print("2 - Print Statement")
        print("3 - Variables")
        print("4 - Operators")
        print("5 - Conditionals")
        print("6 - Loops")
        print("7 - Lists")
        print("8 - Functions")
        print("9 - Run your own code")
        print("10 - Exit the Program")
        time.sleep(0.1)
        choice = input("\nEnter the corresponding no. of your chosen menu: ")
    
        if choice == '1': #data type
            while True:
                os.system('cls')
                run.square_loading()
                os.system('cls')
                print("=======",red+"DATA TYPES"+reset,"=======")
                print(textwrap.fill("Data types categorize data items, indicating what kind of value they \nhold and what operations can be performed on them. In Python, everything is an object. Python data types act as classes, and variables are instances of those classes.",width=70))#definition?intro
                print("\nA. String")
                print("B. Float")
                print("C. Integer")
                print("D. Return to Main Menu")
                choices = input("--> ").upper()

                if choices == 'A': #str
                    os.system('cls')
                    print("=======", yellow+"STRING (str)"+reset, "=======")
                    print(textwrap.fill("A string is a sequence of characters enclosed in quotes.",width=70))#definition

                    print("\nExamples of strings:")#examples
                    print("\nprint(\"Hello World\")")
                    print("print(\"123\")", green + " #still a string because it is inside quotes" + reset)
                    print("print(\"Python\")")
                    print("\nYou use strings when working with text.")

                    exit = input("\nPress R to return to data types\nPress E to return to main menu\n-->").lower()
                    
                    if exit == "r": #return to data types
                        os.system('cls')
                        continue 
                    elif exit == "e": #return to main menu
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue
                elif choices == 'B': #float
                    os.system('cls')
                    print("=======", yellow+"FLOAT"+reset,"=======")
                    print("A float is a number with decimals.")#definition
                    print("Example: 3.14, 0.5, -9.8")#ex.
                    exit = input("\nPress R to return to data types\nPress E to return to main menu\n-->").lower()
                    
                    if exit == "r": #return to data types
                        os.system('cls')
                        continue 
                    elif exit == "e": #return to main menu
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue 
                elif choices == 'C': #int
                    os.system('cls')
                    print("=======",yellow+"INTEGER (int)"+reset,"=======")
                    print("An integer is a whole number with NO decimals.")#definition
                    print("Example: 10, -5, 0")#ex.
                    exit = input("\nPress R to return to data types\nPress E to return to main menu\n-->").lower()
                    
                    if exit == "r": #return to data types
                        os.system('cls')
                        continue 
                    elif exit == "e": #return to main menu
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue 
                elif choices == 'D': #main menu
                    os.system('cls')
                    break
                else: #invalid
                    os.system('cls')
                    print("Error")
                    input("Press enter to continue--> ")
                    os.system('cls')
                    continue  
        elif choice == '2': #printstatement
            while True:
                os.system('cls')
                run.square_loading()
                os.system('cls')
                print("=======",red+"PRINT STATEMENT"+reset,"=======")
                print(textwrap.fill("The print() statement is a built-in Python function used to display text, numbers, variables, or results on the screen. It sends output to the console so the user can see what the program is doing.",width=70))#definition
                print("\nA. Basic Print Usage")
                print("B. Printing Multiple Items")
                print("C. Escape Characters")
                print("D. Using \'sep\' and \'end\'")
                print("E. F Strings (Formatted Strings)")
                print("F. Return to Main Menu")
                choices = input("--> ").lower()

                if choices == "a": #basic
                        os.system('cls')
                        print("=======", yellow+"Basic Print Usage"+reset, "=======")
                        print(textwrap.fill("The print() function displays text or values on the screen.",width=70))#definition
                        
                        print("\nExamples:")#EXAMPLE
                        print('\nprint("Hello World!")')
                        print("print(123)")
                        print('print("Python is fun!")')
                        
                        print("\nOutput:")#OUTPUT
                        print("\nHello World!")
                        print("Python is fun!")
                        print("123")
                    
                        exit = input("\nPress R to return to print statement\nPress E to return to main menu\n--> ").lower()

                        if exit == "r":#return to print
                            os.system('cls')
                            continue
                        elif exit == "e":#return to main
                            os.system('cls')
                            break
                        else:#invalid
                            input("Invalid Choice. Press ENTER to return\n--> ")
                            os.system('cls')
                            continue 
                elif choices == "b":#multi
                        os.system('cls')
                        print("=======", yellow+"Printing Multiple Items"+reset, "=======")
                        print(textwrap.fill("You can print two or more value in a single print statement using commas (,).",width=70))#definition
                        
                        print("\nExamples:")#EXAMPLE
                        print('\nprint("Hello", "World!")',green+'\n#print strings'+reset)

                        print("\nOutput:\nHello World!") #OUTPUT

                        print('\n("Hello", 123)',green+'\n#print str and int'+reset)#EXAMPLE

                        print("\nOutput:\nHello 123")#OUTPUT
                    
                        exit = input("\nPress R to return to print statement\nPress E to return to main menu\n--> ").lower()#EXIT

                        if exit == "r":#return to print
                            os.system('cls')
                            continue
                        elif exit == "e":#return to main
                            os.system('cls')
                            break
                        else:#invalid
                            input("Invalid Choice. Press ENTER to return\n--> ")
                            os.system('cls')
                            continue 
                elif choices == "c": #esc charac
                        os.system('cls')
                        print("=======", yellow+"Escape Characters"+reset, "=======")
                        print(textwrap.fill("Escape chracters are special characters preceded by a backslash(\\). They allow you to do things like insert new lines, tabs, or quotes that are hard to type normally.",width=70))
                        #NEW LINE----
                        print("\n1. New Line (\\n) - this prints to a new line")#\n
                        print(blue+"Example:\n"+reset,"print(\"Hello\\nWorld\")")#x of \n
                        print(yellow+"\nOutput:"+reset,"\nprint(\"Hello\nWorld\")")#out\n
                        #TAB SPACE--------
                        print("\n2. Tab Space (\\t) - this adds a tab space")#\t
                        print(blue+"Example:\n"+reset,"print(\"Hello\\tWorld\")")#ex\t
                        print(yellow+"\nOutput:"+reset,"\n""Hello\tWorld")#out\t
                        #BACKSLASH---------
                        print("\n3. Backslash (\\\\) - this prints a backslash") #\\
                        print(blue+"Example:\n"+reset,"print(\"Hellow\\\\World\")") #ex\\
                        print(yellow+"\nOutput:"+reset,"\nHello\\World")#out\\
                        #DOUBL/SINGLE QUOTE----------
                        print("\n4. Single/Double Quote (\\' or \\\") - prints single or double quote")#\' \"
                        print(blue+"Example:\n"+reset,"print(\"\\\"Hello World\\\"\")")#x\' \"
                        print(yellow+"\nOutput:"+reset,"\n\"Hello World\"")#out\"
                        #BACKSPACE---------
                        print("\n5. Backspace (\\b) - deletes one character") #\b
                        print(blue+"Example:\n"+reset,"print(\"Hello\\bWorld\")")
                        print(yellow+"\nOutput:"+reset,"\nHello\bWorld")
                        #CARRIAGE RETURN-----
                        print("\n6. Carriage Return (\\r) - moves cursor to start of line")#\r
                        print(blue+"Example:\n"+reset,"print(\"Hello World.\\n\\rHello Universe\")")
                        print(yellow+"Output:\n"+reset,"Hello World.\n\rHello Universe")
                    
                        exit = input("\nPress R to return to print statement\nPress E to return to main menu\n--> ").lower()

                        if exit == "r":#return to print
                            os.system('cls')
                            continue
                        elif exit == "e":#return to main
                            os.system('cls')
                            break
                        else:#invalid
                            input("Invalid Choice. Press ENTER to return\n--> ")
                            os.system('cls')
                            continue 
                elif choices == "d": #use sep end
                    os.system('cls')
                    print(textwrap.fill("The print() function has two optional parameters:",width=70))

                    #sep 
                    print("\n======= ",yellow+" Separator(sep) "+reset," =======")
                    print(textwrap.fill("Decides what to place between multiple printed items. Space is the default separator",width=70))
                    print(blue+"\nExample:"+reset)
                    print(green+"\n#default"+reset,"print(\"Is\",\"python\",\"fun?\")",yellow+"\nOutput:"+reset,"\nIs python fun?")
                    print("print(1,2,3, sep=\"|\")",green+"\n#using sep"+reset,yellow+"\nOutput:"+reset)
                    print(1,2,3, sep="|")

                    #end
                    print("\n======= ",yellow+" End Character(end) "+reset," =======")
                    print(blue+"\nExample:"+reset)
                    print(textwrap.fill("Decides what to print after the line ends. New line (\\n) is the default separator",width=70))
                    print("print(\"Is python\", end=\" \")\n(\"fun?\")",green+"\n#default"+reset,yellow+"\nOutput:"+reset,"\nIs python fun?")
                    print("\nprint(\"No\", end=\"!!!\")",yellow+"\nOutput:"+reset)
                    print("No", end="!!!")

                    exit = input("\nPress R to return to print statement\nPress E to return to main menu\n--> ").lower()

                    if exit == "r":#return to print
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue 
                elif choices == "e":#fstrings
                        os.system('cls')
                        print("=======", yellow+" F-Strings (Formatted Strings) "+reset, "=======")
                        print(textwrap.fill("Let you insert variables inside strings easily using curly brace {}. It is a must to put 'f' before the opening quote.", width=70))
                        print("\nExamples:")#EXAMPLE
                        print('\nname = \"Kaithlyn\"')
                        print("age = 18")
                        print(green+'\n#basic'+reset, "\nprint(f\"My name is {name} and I am {age} years old\")")
                        print(blue+"\nOuput:"+reset,"My name is Kaithlyn and I am 18 years old")
                        print(green+'\n#embedded function calls'+reset, "\nprint(f\"My name in uppercase is {name.upper()}\")")
                        print(blue+"\nOuput:"+reset,"\nMy name in uppercase is KAITHLYN")
                    
                        exit = input("\nPress R to return to print statement\nPress E to return to main menu\n--> ").lower()

                        if exit == "r":#return to print
                            os.system('cls')
                            continue
                        elif exit == "e":#return to main
                            os.system('cls')
                            break
                        else:#invalid
                            input("Invalid Choice. Press ENTER to return\n--> ")
                            os.system('cls')
                            continue 
                elif choices == "f":#return main
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print("Error")
                    input("Press enter to continue...")
                    os.system('cls')
                    continue
        elif choice == '3':#VARIABLES
            while True:
                os.system('cls')
                run.square_loading()
                os.system('cls')
                print("======= ",red+"VARIABLES"+reset," =======")
                print(textwrap.fill("Variables are fundamental programming constructs that act as named storage locations for data, whose values can be modified throughout a program's execution",width=70))
                print(textwrap.fill("Rules for variables:\n- Must start with a letter or underscore\n- Case sensitive. Ex: age is not equal to Age\n- Can't be a Python keyword (if, for, while, etc..)",width=70))
                print("\nExample:\nstudent_name = \"Kaithlyn\"\nstudent_age = 18 ")#EXAMPLE
                print(green+"\n#It has no direct output but if you chose to print it"+reset,"\nprint(name, age, sep=\",\")")
                print(yellow+"Output:"+reset,"\nKaithlyn,18")#OUTPUT

                exit = input("\nPress E to return to main menu\n--> ").lower()

                if exit == "e":#return main
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print("Error")
                    input("Press enter to continue...")
                    run.square_loading()
                    os.system('cls')
                    continue
        elif choice == '4':#OPERATORS
            while True:
                os.system('cls')
                run.square_loading()
                os.system('cls')
                print("======= ",red+"OPERATORS"+reset, "=======")
                print(textwrap.fill("Operators are special symbols or keywords that perform operations on one or more operands, which can be values or variables. These operations form expressions that produce results, making operators fundamental for data manipulation and controlling program logic.",width=70))#definition
                print("\nA. Arithmetic Operators")
                print("B. Assignment Operators")
                print("C. Relational Operators")
                print("D. Logical Operators")
                print("E. Return to Main Menu")
                choices = input("--> ").lower()

                if choices == "a":#arithmetic
                    os.system('cls')
                    print("=======",yellow+"ARITHMETIC OPERATORS"+reset,"=======")
                    print(textwrap.fill("Arithmetic Operators are used for computation. It performs the standard mathematical computation on numeric values. These are the different types of arithmetic operatos:", width=70))
                    print("\n1. + (Addition) - adds numbers")
                    print("2. - (Subtraction) - subtract numbers")
                    print("3. * (Multiplication)")
                    print("4. / (Division)")
                    print("5. % (Modulus Division) - returns the remainder of a division opetation between two numbers.")
                    print("6. ** (Exponentiation) - ")
                    print("7. // (Floor Division) - ")
                    #EXAMPLE------------------------------
                    print(blue+"\n Example:"+reset)
                    print("\nn1 = 10 \nn2 = 3 \nadd = n1 + n2 \nminus = n1 - n2 \ntimes = n1 * n2 \ndivide = n1/n2 \nremainder = n1%n2 \nexponent = n1**n2 \nfloor = n1//n2")
                    print("\nprint(f\"Sum of {n1} and {n2} is {add}\")")
                    print("\nprint(f\"Difference of {n1} and {n2} is {minus}\")")
                    print("\nprint(f\"Product of {n1} and {n2} is {times}\")")
                    print("\nprint(f\"Quotient of {n1} and {n2} is {divide}\")")
                    print("\nprint(f\"Remainder of {n1} and {n2} is {remainder}\")")
                    print("\nprint(f\"{n1} exponent by {n2} is {exponent}\")")
                    print("\nprint(f\"Floor division of {n1} and {n2} is {floor}\")")
                    #OUTPUT--------------------------------
                    print(yellow+"\nOutput:"+reset)
                    print("Sum of 10 and 3 is 13")
                    print("Difference of 10 and 3 is 7")
                    print("Product of 10 and 3 is 30")
                    print("Quotient of 10 and 3 is 3.3333333333333335")
                    print("Remainder of 10 and 3 is 1", green+"#10 % 3 returns 1 (because 10 divided by 3 is 3 with a remainder of 1)"+reset)
                    print("10 exponent by 3 is 1000",green+"#10 raised to 3 (10^3) is 1000. Why: 10^3 = 10 * 10 * 10 = 1000"+reset)
                    print("Floor division of 10 and 3 is",green+"#Calculates to standard division but rounds the result down to nearest int(whole number)"+reset)

                    exit = input("\nPress R to return to operators\nPress E to return to main menu\n--> ").lower()

                    if exit == "r":#return
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue 
                elif choices == "b":#assignment
                    os.system('cls')
                    print("=======",yellow+"ASSIGNMENT OPERATORS"+reset,"=======")
                    print(textwrap.fill("Assignment operators are used to assign a value to a variable. Here are the ff operators:", width=70))
                    print(textwrap.fill("\n\n1. '=' assigns value on the on the right side", width=70))
                    print(textwrap.fill("\n\n2. '+=' adds the right side value to the variables current value. Updates variable with the resulting sum.", width=70))
                    print(textwrap.fill("\n\n3. '-=' subtracts the right side value to the variables current value. Updates variable with the resulting difference.", width=70))
                    print(textwrap.fill("\n\n4. '*=' multiplies the right side value to the variables current value. Updates the variable with the resulting product.", width=70))
                    print(textwrap.fill("\n\n5. '/=' divides the right side value to the variables current value. Updates the variable with the resulting floating-point quotient.", width=70))
                    #EXAMPLE---------------
                    print("\nExample:")
                    print("k = 10")
                    print("k += 10 is same as k = k + 10")
                    print("k -= 10 is same as k = k - 10")
                    print("k *= 10 is same as k = k * 10")
                    print("k /= 10 is same as k = k / 10")
                    print("k = 10")
                    print("k += 10")
                    print("print(k)")
                    print("k -= 10")
                    print("print(k)")
                    print("k *= 10")
                    print("print(k)")
                    print("k /= 10")
                    print("print(k)")
                    #OUTPUT----------------------
                    print(yellow+"\nOutput:"+reset)
                    print("\n10", end=" ")
                    print(textwrap.fill(green+"#variable k is intialized and printed with the value of 10"+reset, width=70))
                    print("\n20", end=" ")
                    print(textwrap.fill(green+"#The operator adds 10 to the current value of k (10 + 10 = 20)"+reset, width=70))
                    print("\n10", end=" ")
                    print(textwrap.fill(green+"#Operator subtracts 10 from the current value of k (20 - 10 = 10)"+reset, width=70))
                    print("\n100", end=" ")
                    print(textwrap.fill(green+"#Operator multiplies the current value of k by 10 (10 * 10 = 100)"+reset, width=70))
                    print("\n10.0", end=" ")
                    print(textwrap.fill(green+"#operator divides the current value of k by 10 (100 / 10 = 10.0)"+reset, width=70))
                    
                    exit = input("\nPress R to return to operators\nPress E to return to main menu\n--> ").lower()

                    if exit == "r":#return
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue 
                elif choices == "c":#relational
                    os.system('cls')
                    print("=======",yellow+"RELATIONAL OPERATORS"+reset,"=======")
                    print(textwrap.fill("Also known as comparison operators, are used to compare two operands and return a Boolean value (True or False). Here are the ff relational operators:", width=70))
                    print(textwrap.fill("1. Greater than (>) = Checks if the value on the left is strictly larger than the value on the right.", width=70))
                    print(textwrap.fill("2. Greater than or equal (>=) - Checks if the value on the left is larger than or equal to the value on the right.", width=70))
                    print(textwrap.fill("3. Less than (<) - Checks if the value on the left is strictly smaller than the value on the right.", width=70))
                    print(textwrap.fill("4. Less than or equal (<=) - Checks if the value on the left is smaller than or equal to the value on the right.", width=70))
                    print(textwrap.fill("5. Equal (==) - Checks if the value on the left is exactly the same as the value on the right.", width=70))
                    print(textwrap.fill("6. Not equal (!=) - Checks if the value on the left is not the same as the value on the right.", width=70))
                    #EXAMPLE----------------------------------
                    print(blue+"\n Example:"+reset)
                    print("n1 = 10")
                    print("n2 = 5")
                    print('s1 = "Python"')
                    print('s2 = "python"')
                    print(green+"\n# > (Greater Than)"+reset)
                    print("print(f\"{n1} > {n2} is {n1 > n2}\")")
                    print(green+"\n# >= (Greater Than or Equal To)"+reset)
                    print("print(f\"{n1} >= {n2} is {n1 >= n2}\")")
                    print(green+"\n# < (Less Than)"+reset)
                    print("print(f\"{n1} < {n2} is {n1 < n2}\")")
                    print(green+"\n# <= (Less Than or Equal To)"+reset)
                    print("print(f\"{n1} <= {n2} is {n1 <= n2}\")")
                    print(green+"\n# == (Equal To) - Checks value, NOT case sensitivity but python is case sensitive"+reset)
                    print("print(f\"'Python' == 'python' is {s1 == s2}\")")
                    print(green+"\n# != (Not Equal To)"+reset)
                    print("print(f\"{n1} != {n2} is {n1 != n2}\")")
                    #OUTPUT----------------------------------
                    print(yellow+"\nOutput:"+reset)
                    print("10 > 5 is True")
                    print("10 >= 5 is True")
                    print("10 < 5 is False")
                    print("10 <= 5 is False")
                    print("'Python' == 'python' is False")
                    print("10 != 5 is True")
                    
                    exit = input("\nPress R to return to operators\nPress E to return to main menu\n--> ").lower()

                    if exit == "r":#return
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue 
                elif choices == "d":#logical
                    os.system('cls')
                    print("=======",yellow+"LOGICAL OPERATORS"+reset,"=======")
                    print(textwrap.fill("Logical operators ( and , or , not ) are keywords used to combine multiple conditional statements or to reverse the logical state of an operand. They always return a Boolean value ( True or False ) and are crucial for building sophisticated decision-making logic. Here are the ff logical operators:", width=70))
                    #AND--------------------------
                    print(textwrap.fill("\n1. 'and' - returns True if both statement are true.", width=70))
                    print(textwrap.fill("\t1.2. If statement is both False the result will be False.", width=70))
                    print(textwrap.fill("\t1.3. If statement is False and True or True and False the result will be False.", width=70))
                    print(textwrap.fill("\t1.4. If statement is both True the result will be True.", width=70))
                    #OR-------------------------
                    print(textwrap.fill("\n2. 'or' - returns True if any of the statements is true.", width=70))
                    print(textwrap.fill("\t2.2. If statement is both False the result will be False.", width=70))
                    print(textwrap.fill("\t2.3. If statement is False and True or True and False the result will be True.", width=70))
                    print(textwrap.fill("\t2.4. If statement is both True the result will be True.", width=70))
                    #NOT---------------------------
                    print(textwrap.fill("\n3. 'not' - reverse the result.", width=70))
                    print(textwrap.fill("\t3.1. If statement is 'not' False the result will be True.", width=70))
                    print(textwrap.fill("\t3.2. If statement is 'not' True the result will be False.", width=70))
                    #EXAMPLE--------------------
                    print(blue+"\n Example:"+reset)
                    print("print((3 > 10) and (10 == 10))")
                    print("print((3 < 20) and (10 == 10))")
                    print("print(not((3 < 20) and (10 == 10)))")
                    #OUTPUT------------------------------
                    print(yellow+"\nOutput:"+reset)
                    print("False", green+"#Condition A is False"+reset)
                    print("True",green+"#Both conditions are True)"+reset)
                    print("False")
                    print(textwrap.fill(green+"#Both conditions are True but not is applied, so it reversed True to False)"+reset,width=70))
                    
                    exit = input("\nPress R to return to operators\nPress E to return to main menu\n--> ").lower()

                    if exit == "r":#return
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue 
                elif choices == "e":#return main
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print("Error")
                    input("Press enter to continue...")
                    run.square_loading()
                    os.system('cls')
                    continue
        elif choice == '5':#CONDITIONALS
            while True:
                os.system('cls')
                run.square_loading()
                os.system('cls')
                print("======= ",red+"CONDITIONALS"+reset, "=======")
                print(textwrap.fill("A conditional statement is a control flow structure that allows a program to execute specific blocks of code only if a certain pre-defined condition is True. Conditionals give your program a \"brain\" Without them, a program would simply execute every line of code sequentially from top to bottom, every single time.",width=70))
                print("\nA. If")
                print("B. If-else")
                print("C. If-elif-else")
                print("D. Nested Conditionals")
                print("E. Return to Main Menu")
                choices = input("--> ").lower()

                if choices == "a":#if
                    os.system('cls')
                    print("=======",yellow+"If"+reset,"=======")
                    print(textwrap.fill("The If statement executes a block of code only if its condition is True. It is the most basic control structure, allowing the program to decide whether to perform an action or skip it.",width=70))
                    print(blue+"\n Example:"+reset)#EXAMPLE
                    print("temperature = 35")
                    print("\nif temperature > 30:\n\tprint(\"Warning: High temp detected.\")")
                    print(yellow+"\nOutput:"+reset)#OUTPUT
                    print("Warning: High temp detected.")
                    print(textwrap.fill(green+"#35 > 30 is True but if temp was 25, this line would be skipped"+reset,width=70))
                    
                    exit = input("\nPress R to return to conditionals \nPress E to return to main menu\n--> ").lower()

                    if exit == "r":#return
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue 
                elif choices == "b":#if else
                    os.system('cls')
                    print("=======",yellow+"If-else"+reset,"=======")
                    print(textwrap.fill("The If-else statement executes one of two exclusive code blocks based on a single condition. The program must follow either the 'if' path (if True) or the 'else' path (if False).",width=70))
                    print(blue+"\n Example:"+reset)#EXAMPLE
                    print("temperature = 22")
                    print("\nif temperature > 30:\n\tprint(\"Danger!\")\nelse:\n\tprint(\"Safe!\")")
                    print(yellow+"\nOutput:"+reset)#OUTPUT
                    print("Safe!")
                    print(textwrap.fill(green+"#22 > 30 is False. This is the result because the 'if' condition was False"+reset,width=70))
                    
                    exit = input("\nPress R to return to conditionals\nPress E to return to main menu\n--> ").lower()

                    if exit == "r":#return
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue 
                elif choices == "c":#if elif else
                    os.system('cls')
                    print("=======",yellow+"If-elif-else"+reset,"=======")
                    print(textwrap.fill("The If-Elif-Else statement checks a series of conditions and executes the code block for the first one that is True. This structure handles multiple possible outcomes, exiting the check once any condition is met.",width=70))
                    print(blue+"\n Example:"+reset)#EXAMPLE
                    print("temperature = 18")
                    print("\nif temperature > 30:\n\tprint(\"It's a hot day.\")")
                    print("\nelif temperature > 20:\n\tprint(\"It's a warm day.\")")
                    print("\nelif temperature > 15:\n\tprint(\"It's a cool day.\")")
                    print("\nelse:\n\tprint(\"It's a cold day.\")")
                    print(yellow+"\nOutput:"+reset)#OUTPUT
                    print("It's a cool day.")
                    print(textwrap.fill(green+"#It skipped the first two blocks of code because the 3rd block resulted in True"+reset,width=70))
                    
                    exit = input("\nPress R to return to conditionals \nPress E to return to main menu\n--> ").lower()

                    if exit == "r":#return
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue 
                elif choices == "d":#nested
                    os.system('cls')
                    print("=======",yellow+"NESTED CONDITIONALS"+reset,"=======")
                    print(textwrap.fill("Nested conditionals place one conditional statement (like an if or if-else) entirely inside another. The inner condition is only checked and executed if the outer condition has already evaluated to True.",width=70))
                    print(blue+"\n Example:"+reset)#EXAMPLE
                    print("door_unlocked = True\ntime_ok = False")
                    print("\nif door_unlocked:")
                    print(green+"#Outer condition is True, so we proceed to the inner condition."+reset)
                    print("\tif time_ok:\n\t\tprint(\"Access Granted: Welcome!\")")
                    print("\n\telse:\n\t\tprint(\"Access Denied: It is currently outside business hours.\")")
                    print(green+"#Inner 'else' runs because time_ok is False"+reset)
                    print("\nelse:\n\tprint(\"Access Denied: Door is locked.\")")
                    print(green+"#If door_unlocked was False, this line would run."+reset)
                    print(yellow+"\nOutput:"+reset)#OUTPUT
                    print("Access Denied: It is currently outside business hours.")
                    
                    exit = input("\nPress R to return to conditionals \nPress E to return to main menu\n--> ").lower()

                    if exit == "r":#return
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue 
                elif choices == "e":#return main
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print("Error")
                    input("Press enter to continue...")
                    run.square_loading()
                    os.system('cls')
                    continue
        elif choice == '6':#LOOPS
            while True:
                os.system('cls')
                run.square_loading()
                os.system('cls')
                print("======= ",red+"LOOPS"+reset, "=======")
                print(textwrap.fill("Loops are programming structures that repeatedly execute a block of code as long as a condition is true or for every item in a sequence. ",width=70))
                print("\nA. For Loop")
                print("B. While Loop")
                print("C. Loop Control")
                print("D. Return to Main Menu")
                choices = input("--> ").lower()

                if choices == "a": #For Loops
                    os.system('cls')
                    print("=======", yellow+"FOR LOOPS (ITERATION)"+reset,"=======")
                    print(textwrap.fill("For loops are used for iteration: going through a sequence (like a list, string, or range of numbers) a specific number of times.", width=70))
                    print(blue+"\n Example 1 (Iterating a List):"+reset)
                    print('fruits = ["apple", "banana", "cherry"]')
                    print("for x in fruits:")
                    print("\tprint(x)")
                    print(yellow+"\nOutput:"+reset)
                    print("apple\nbanana\ncherry")
                    print(blue+"\n Example 2 (Using range()):"+reset)
                    print(green+"# The range(5) generates numbers from 0 up to (but not including) 5."+reset)
                    print("for i in range(5):")
                    print("\tprint(i)")
                    print(yellow+"\nOutput:"+reset)
                    print("0\n1\n2\n3\n4")

                    exit = input("\nPress R to return to loops menu\nPress E to return to main menu\n--> ").lower()
                    if exit == "r":
                        os.system('cls')
                        continue
                    elif exit == "e":
                        os.system('cls')
                        break
                    else:
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue
                elif choices == "b": # While Loops
                    os.system('cls')
                    print("=======", yellow+"WHILE LOOPS (CONDITION-BASED)"+reset,"=======")
                    print(textwrap.fill("While loops execute a block of code repeatedly AS LONG AS a specified boolean condition remains True. You must ensure the condition eventually becomes False to avoid an infinite loop.", width=70))
                    print(blue+"\n Example:"+reset)
                    print("count = 1")
                    print("while count < 4:",green+"# Loop runs while count is less than 4"+reset)
                    print("\tprint(f\"Current count: {count}\")")
                    print("\tcount += 1 ",green+"# CRUCIAL STEP: This increments the variable"+reset)
                    
                    print(yellow+"\nOutput:"+reset)
                    print("Current count: 1")
                    print("Current count: 2")
                    print("Current count: 3")
                    print(textwrap.fill(green+"#The loop stops when count becomes 4, because 4 < 4 is False."+reset, width=70))
                    
                    exit = input("\nPress R to return to loops menu\nPress E to return to main menu\n--> ").lower()
                    if exit == "r":#return to loops
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue
                elif choices == "c": # Loop Control (Break and Continue)
                    os.system('cls')
                    print("=======", yellow+"LOOP CONTROL (BREAK and CONTINUE)"+reset,"=======")
                    print(textwrap.fill("These two keywords allow you to change the execution flow inside a loop. They provide fine-grained control over when a loop should stop or when it should skip certain steps.", width=70))
                    print("\n1. 'BREAK' KEYWORD")
                    print(textwrap.fill("The 'break' keyword immediately terminates the current loop (both 'for' and 'while') and moves program execution to the statement immediately following the loop.", width=70))
                    print(blue+"\n Example (Break):"+reset)
                    print("for i in range(10):")
                    print("\tif i == 5:",green+"# Stop the loop when i is 5"+reset)
                    print("\t\tbreak")
                    print("\tprint(i, end=' ')")
                    print(yellow+"\nOutput:"+reset)
                    print("0 1 2 3 4")
                    print(textwrap.fill(green+"#The loop was exited when i became 5. 5 was never printed."+reset, width=70))
                    print("\n2. 'CONTINUE' KEYWORD")
                    print(textwrap.fill("The 'continue' keyword immediately stops the current iteration of the loop, skips any remaining code in that iteration, and forces the loop to proceed to the next iteration.", width=70))
                    print(blue+"\n Example (Continue):"+reset)
                    print("for num in range(6):")
                    print("\tif num % 2 != 0:",green+"# If the number is odd"+reset)
                    print("\t\tcontinue",green+"# Skip printing for this number"+reset)
                    print("\tprint(num, end=' ')")
                    
                    print(yellow+"\nOutput:"+reset)
                    print("0 2 4")
                    print(textwrap.fill(green+"#The odd numbers (1, 3, 5) were skipped by the 'continue' statement."+reset, width=70))

                    exit = input("\nPress R to return to loops menu\nPress E to return to main menu\n--> ").lower()
                    if exit == "r":#return to loops
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue
                elif choices == "d":
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print("Error")
                    input("Press enter to continue...")
                    run.square_loading()
                    os.system('cls')
                    continue
        elif choice == '7':#LISTS
            while True:
                os.system('cls')
                run.square_loading()
                os.system('cls')
                print("======= ",red+"LISTS"+reset, "=======")
                print(textwrap.fill("Lists are one of Python's most versatile data types, used to store collections of data. They are mutable (changeable), ordered, and can contain elements of different data types.",width=70))
                print("\nA. Creating and Accessing List")
                print("B. Removing")
                print("C. Utility Methods")
                print("D. Return to Main Menu")
                choices = input("--> ").lower()

                if choices == "a": #Creating and Accessing Lists
                    os.system('cls')
                    print("=======", yellow+"CREATING AND ACCESSING LISTS"+reset,"=======")
                    print(textwrap.fill("Lists are created using square brackets [ ] and are ordered, meaning elements retain their position. Elements can be accessed using their index, starting from 0.", width=70))
                    #CREATING LISTS
                    print("\n1. CREATING LISTS")
                    print(blue+"\n Example (Creation):"+reset)#EXAMPLE
                    print("# A list can hold different data types")
                    print('data = ["apple", 10, 3.14, True]')
                    print('empty_list = []')
                    #ACCESSING ELEMENTS (INDEXING)
                    print("\n2. ACCESSING ELEMENTS (INDEXING)")
                    print(textwrap.fill("Positive indexing starts from 0 (the first element). Negative indexing starts from -1 (the last element).", width=70))
                    print(blue+"\n Example (Indexing):"+reset)#EXAMPLE
                    print("my_list = ['A', 'B', 'C', 'D']")
                    print("print(my_list[0])")
                    print("print(my_list[-1])")
                    print(yellow+"\nOutput:"+reset)#OUTPUT
                    print("A")
                    print("D")
                    #ACCESSING SUBSETS (SLICING)
                    print("\n3. ACCESSING SUBSETS (SLICING)")
                    print(textwrap.fill("Slicing [start:end] returns a new list containing elements from the start index up to, but NOT including, the end index.", width=70))
                    print(blue+"\n Example (Slicing):"+reset)#EXAMPLE
                    print("numbers = [10, 20, 30, 40, 50]")
                    print("print(numbers[1:4]) # From index 1 up to 4 (exclusive)")
                    print("print(numbers[:3])  # From start up to index 3 (exclusive)")
                    print(yellow+"\nOutput:"+reset)#OUTPUT
                    print("[20, 30, 40]")
                    print("[10, 20, 30]")

                    exit = input("\nPress R to return to lists\nPress E to return to main menu\n--> ").lower()
                    if exit == "r":#return to lists
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue
                elif choices == "b": # Removing Items from a List
                    os.system('cls')
                    print("=======", yellow+"REMOVING ITEMS FROM A LIST"+reset,"=======")
                    print(textwrap.fill("There are three primary ways to remove elements: remove() (by value), pop() (by index), and clear() (all elements).", width=70))
                    #REMOVE Method--------------
                    print("\n1. 'REMOVE()' METHOD (By Value)")
                    print(textwrap.fill("Removes the FIRST occurrence of the specified VALUE. If the value is not found, it raises an error.", width=70))
                    print(blue+"\n Example (remove):"+reset)#EXAMPLES
                    print('planets = ["Mars", "Earth", "Jupiter", "Earth"]')
                    print('planets.remove("Earth")')
                    print('print(planets)')
                    print(yellow+"\nOutput:"+reset)#OUTPUT
                    print("['Mars', 'Jupiter', 'Earth']", green+"#Only the first 'Earth' was removed."+reset)
                    #POP Method-----------
                    print("\n2. 'POP()' METHOD (By Index)")
                    print(textwrap.fill("Removes and RETURNS the item at the given INDEX. If no index is specified, it removes the LAST item.", width=70))
                    print(blue+"\n Example (pop):"+reset)#EXAMPLE
                    print('data = [10, 20, 30]')
                    print('removed = data.pop(1) # Remove the item at index 1 (which is 20)')
                    print('print(f"Removed: {removed}. List: {data}")')
                    print(yellow+"\nOutput:"+reset)#OUTPUT
                    print("Removed: 20. List: [10, 30]")
                    #CLEAR Method----------------------
                    print("\n3. 'CLEAR()' METHOD (All Items)---")
                    print(textwrap.fill("Removes ALL elements from the list, leaving it empty. The list object still exists.", width=70))
                    print(blue+"\n Example (clear):"+reset)#EXAMPLE
                    print('items = [1, 2, 3]')
                    print('items.clear()')
                    print('print(items)')
                    print(yellow+"\nOutput:"+reset)#OUTPUT
                    print("[]")

                    exit = input("\nPress R to return to lists menu\nPress E to return to main menu\n--> ").lower()
                    if exit == "r":#return to lists
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue
                elif choices == "c": # Utility Methods
                    os.system('cls')
                    print("=======", yellow+"UTILITY AND MANIPULATION METHODS"+reset,"=======")
                    print(textwrap.fill("These methods cover everything from changing a list's order to performing checks, adding items, and determining its size or element locations.", width=70))
                    #ADDING----------
                    print("\n 1. ADDING ITEMS")
                    print(textwrap.fill("Methods used to add elements to a list:", width=70))
                    print(blue+"\n Example (append/insert):"+reset)#EXAMPLE
                    print('data = ["cat", "dog"]')
                    print('data.append("bird")', green+'#adds to the end'+reset)
                    print('data.insert(0, "fish")', green+'# Inserts at index 0'+reset)
                    print('print(data)')
                    print(yellow+"\nOutput:"+reset)#OUTPUT
                    print("['fish', 'cat', 'dog', 'bird']")
                    # Sorting and Reversing------------------
                    print("\n2. ORDERING METHODS")
                    print(textwrap.fill("Methods used to change the order of elements in the list IN-PLACE (meaning the original list is modified).", width=70))
                    print(blue+"\n Example (sort/reverse):"+reset)#example
                    print('nums = [30, 10, 20]')
                    print('nums.sort() # Sorts in ascending order')
                    print('nums.reverse() # Reverses the current order')
                    print('print(nums)')
                    print(yellow+"\nOutput:"+reset)#output
                    print("[30, 20, 10]")
                    #Information Methods--------------
                    print("\n 3. INFORMATION METHODS")
                    print(textwrap.fill("Functions and methods used to check the list's status or find element information.", width=70))
                    print(blue+"\n Example (len/index/count):"+reset)#example
                    print('letters = ["a", "b", "a", "c", "d"]')
                    print('length = len(letters)')
                    print('first_b = letters.index("b")',green +'Find the index of the first \'b\''+reset)
                    print('a_count = letters.count("a")',green+'# Count how many \'a\'s there are'+reset)
                    print('print(f"Length: {length}")')
                    print('print(f"Index of \'b\': {first_b}")')
                    print('print(f"Count of \'a\': {a_count}")')
                    print(yellow+"\nOutput:"+reset)#output
                    print("Length: 5")
                    print("Index of 'b': 1")
                    print("Count of 'a': 2")

                    exit = input("\nPress R to return to lists\nPress E to return to main menu\n--> ").lower()
                    
                    if exit == "r":#return to lists
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue
                elif choices == "d":
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print("Error")
                    input("Press enter to continue...")
                    run.square_loading()
                    os.system('cls')
                    continue
        elif choice == '8':#FUNCTIONS
            while True:
                os.system('cls')
                run.square_loading()
                os.system('cls')
                print("======= ",red+"FUNCTIONS"+reset, "=======")
                print(textwrap.fill("Functions are blocks of organized, reusable code that are used to perform a single, related action. They make code modular and easier to manage.", width=70))
                print("\nA. Defining and Calling Functions")
                print("B. Arguments and Parameters")
                print("C. The Return Statement")
                print("D. Return to Main Menu")
                choices = input("--> ").lower()

                if choices == "a": #Defining and Calling Functions
                    os.system('cls')
                    print("=======", yellow+"DEFINING AND CALLING FUNCTIONS"+reset,"=======")
                    print(textwrap.fill("A function is defined using the 'def' keyword, followed by the function name and parentheses (). The code block inside the function must be indented.", width=70))
                    #Defining a Function----------
                    print("\n1. DEFINITION (def keyword)")
                    print(textwrap.fill("Defining a function creates the function but does not run its code.", width=70))
                    print(blue+"\n Example (Definition):"+reset)
                    print("def introduce():")
                    print("\tprint(\"My name is Hal.\")")
                    print("\tprint(\"I am a Python program.\")")
                    #Calling a Function
                    print("\n2. CALLING A FUNCTION")
                    print(textwrap.fill("To execute the code inside a function, you must call it by using its name followed by parentheses.", width=70))
                    print(blue+"\n Example (Call):"+reset)
                    print("#Code runs the definition above, then:")
                    print("introduce() # Calls the function")
                    print(yellow+"\nOutput:"+reset)
                    print("#The function executes here")
                    print("My name is Hal.")
                    print("I am a Python program.")

                    exit = input("\nPress R to return to functions\nPress E to return to main menu\n--> ").lower()
                    if exit == "r":#return to functions
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue
                elif choices == "b": #arguments and Parameters
                    os.system('cls')
                    print("=======", yellow+"ARGUMENTS AND PARAMETERS"+reset,"=======")
                    print(textwrap.fill("A parameter is the variable listed inside the parentheses in the function DEFINITION. An argument is the actual value passed to the function when it is CALLED.", width=70))
                    #Simple Parameter Example--------------------
                    print("\n1. PASSING A SINGLE ARGUMENT")
                    print(textwrap.fill("The function requires one piece of information (parameter) to execute its task.", width=70))
                    print(blue+"\n Example:"+reset)
                    print("def greet(name): # 'name' is the parameter")
                    print("\tprint(f\"Hello, {name}!\")")
                    print("\ngreet(\"Alice\") # \"Alice\" is the argument")
                    print(yellow+"\nOutput:"+reset)
                    print("Hello, Alice!")

                    #Multiple Parameters Example--------
                    print("\n2. MULTIPLE ARGUMENTS")
                    print(textwrap.fill("Functions can accept multiple arguments, which must be provided in the correct order (positional arguments).", width=70))
                    print(blue+"\n Example:"+reset)
                    print("def calculate_sum(a, b): # 'a' and 'b' are parameters")
                    print("\tprint(a + b)")
                    print("\ncalculate_sum(10, 5) # 10 and 5 are arguments")
                    print(yellow+"\nOutput:"+reset)
                    print("15")

                    exit = input("\nPress R to return to functions\nPress E to return to main menu\n--> ").lower()
                    if exit == "r":#return to functions
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                        continue                
                elif choices == "c": #The Return Statement
                    os.system('cls')
                    print("=======", yellow+"THE RETURN STATEMENT"+reset,"=======")
                    print(textwrap.fill("The \'return\' statement is used to exit a function and send a result back to the place where the function was called. This allows the function's output to be used in other calculations or stored in a variable.", width=70))
                    #Basic Return Example-----------------
                    print("\n1. BASIC RETURN")
                    print(textwrap.fill("A function calculates a value and sends it back using \'return\'. This value can be captured.", width=70))
                    print(blue+"\n Example:"+reset)
                    print("def multiply_by_two(number):")
                    print("\tresult = number * 2")
                    print("\treturn result",green+"# Function output is 20"+reset)
                    print("\noutput = multiply_by_two(10)",green+"# The returned 20 is stored in \'output\'"+reset)
                    print("print(output)")
                    print(yellow+"\nOutput:"+reset)
                    print("20")
                    #Return vs. Print Example---- ---
                    print("\n2. RETURN vs. PRINT")
                    print(textwrap.fill("A function that only 'print's cannot be used in expressions; a function that 'return's CAN.", width=70))
                    print(blue+"\n Example:"+reset)
                    print("# This will NOT work: print(add_and_print(5, 5) + 10)")
                    print("def add_and_return(x, y):")
                    print("\treturn x + y")
                    print("\ntotal = add_and_return(5, 5)")
                    print("grand_total = total + 10")
                    print("print(f\"Grand Total: {grand_total}\")")
                    print(yellow+"\nOutput:"+reset)
                    print("Grand Total: 20")
                    print(textwrap.fill(green+"#The returned value (10) was successfully used in the 'grand_total' calculation."+reset, width=70))

                    exit = input("\nPress R to return to functions\nPress E to return to main menu\n--> ").lower()
                    
                    if exit == "r":#return to functions
                        os.system('cls')
                        continue
                    elif exit == "e":#return to main
                        os.system('cls')
                        break
                    else:#invalid
                        input("Invalid Choice. Press ENTER to return\n--> ")
                        os.system('cls')
                elif choices == "d":
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print("Error")
                    input("Press enter to continue...")
                    run.square_loading()
                    os.system('cls')
                    continue
        elif choice == '9': # RUN YOUR OWN CODE
            while True:
                os.system('cls')
                run.square_loading()
                os.system('cls')
                print("=======", red+"RUN YOUR OWN CODE"+reset, "=======")
                print(textwrap.fill(yellow+"CAUTION: This feature allows you to execute arbitrary Python code. Type carefully! The interpreter runs everything you type.", width=70))
                print(textwrap.fill("All code will be executed sequentially using the built-in 'exec' function.", width=70))

                run.code_exe()
                        
                exit_choice = input("\nPress R to Run More Code\nPress E to return to main menu\n--> ").lower()
                
                if exit_choice == "r":
                    os.system('cls')
                    continue
                elif exit_choice == "e":
                    os.system('cls')
                    break
                else:
                    input("Invalid Choice. Press ENTER to return to Run Your Own Code menu\n--> ")
                    os.system('cls')
                    continue
        elif choice == '10':
            os.system('cls')
            run.square_loading()
            os.system('cls')
            print("Goodbyee👋🏻")
            break
        else:
            os.system('cls')
            print("Error. Please try again!")
            os.system('cls')
            run.square_loading()
            os.system('cls')
            continue    
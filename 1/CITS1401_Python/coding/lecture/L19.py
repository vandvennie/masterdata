def chaoticain():
    print("This program illustrates a chaotic function")
    try:
        x = float(input("Enter a number between 0 and 1: "))
        if x>1 or x<0:
            print("The value is not between 0 and 1.\nThe default value is '0.5'")
            x=0.5
    except ValueError:
       print("The entered value is not numerichell. Cannot proceed")
       print("Program will be run for default value '0.5'")
       x=0.5
        #return
    except ZeroDivisionError:
        print("There is mathematical problem of diciding a value by zero")
        print("Program terminated")

    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(i, x)
    #except:
    #    print("There is an error.")
chaoticain()
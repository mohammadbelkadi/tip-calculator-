def tipcalculator():

    print("Thanks for eating with us")

    # Here the user inputs the bill (tax not included at this point)
    # The input function allows the user to take the users input 
    #  we must use float because we may be dealing with decimals
    amount = float(input("Enter your bill amount ($): "))

    # user then inputs the tip percentage
    tip = float(input("what percentage of tip do you want to give? "))

    # Here the tip is calculated 
    x = ((0.01*tip)*amount)
    print("the tip will be $",x)

    # Here we ask the user how many people ar splitting the bill.
    split = float(input("How many people are spliting the bill: "))

    Y = float((amount + (0.01 * tip)* amount) + amount * .10) 
    print("The total is $",Y)

    tip2 = float((amount + (0.01 * tip)* amount) + amount * .10) / split
    print("The amount each person has to pay is $", tip2)

    tip3 = (input("would you like to add another tip?"))
    if tip3 == "yes":
        tipcalculator()
    else:
        print("have a nice day")
tipcalculator()

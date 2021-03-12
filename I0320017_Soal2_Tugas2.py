print(
    """============================================================================
    Hello There
    welcome to your personal assistant, my name is Aria
    you can give me command by typing some numbers
    type 20 to show all command
    type 00 to stop the program
============================================================================
    """
)
def elsee():
    print("anything else?")
need = 0
while need == 0:
    need2 = int(input("what do you need? "))
    need = need * 0
    if need2 == 1:
        print("your name is Berlian Safri Prakoso")
        elsee()
    elif need2 == 2:
        print("you are 19 years old")
        elsee()
    elif need2 == 3:
        print("according to this map, you are on Eden Project")
        elsee()
    elif need2 == 4:
        from datetime import date
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        print("today is ", d2)
        elsee()
    elif need2 == 5:
        print("ordering, Bakso :)")
        bakso = float(input("how many servings of bakso do you want?"))
        print(f"the prices for your bakso is Rp.{bakso * 14000} Rupiah")
        elsee()
    elif need2 == 20:
        print("""
        1. your name
        2. your age
        3. location
        4. date
        5. order bakso
        20. show all command
        00. stop program""")
        elsee()
    elif need2 == 00:
        print("Program Stopped!.\nthank you")
        break

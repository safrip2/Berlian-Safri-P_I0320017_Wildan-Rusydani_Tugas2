print(
    """============================================================================
    Hello There
    welcome to your personal assistant, my name is Aria
    you can give me command by typing some numbers
    0 to show all command
============================================================================
    """
)
def elsee():
    print("anything else?")
need = int(input("what do you need: "))
if need == 1:
    print("Your name is Berlian Safri Prakoso")
    elsee()
elif need == 2:
    print("according to this map, you are on Broadgreen Hospital Liverpool")
    elsee()
elif need == 3:
    from datetime import date
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print("today is ", d2)
    elsee()
elif need == 4:
    print("you don't remember it? you have no girlfriend, so sad :(")
    elsee()
elif need == 5:
    print("alright, the soup would come in 5 minutes")
    elsee()
elif need == 6:
    print("your height is 173 cm")
    elsee()
elif need == 7:
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("now is", current_time)
    elsee()
elif need == 8:
    temp = (input("your temperature is 98.6 Fahrenheit, want to see in Celcius?"))
    if temp.upper() == "YES":
        print(f"your body temperature is {(98.6 -32) * 0.56 } Celcius")
        elsee()
elif need == 0:
    print(
        """
        1 = name
        2 = location
        3 = date
        4 = am i single?
        5 = order soup
        6 = height
        7 = current time
        8 = temperature
        """
    )
else:
    print("this feature will bring to you soon")


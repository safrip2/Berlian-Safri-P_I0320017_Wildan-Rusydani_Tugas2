print(
    """============================================================================
    welcome to your personal assistant, my name is alexa
    here i will help you to find your past memories
    cause i know that you had problem to remember something after you had vichile accident
    You can give me commands by typing
    1. who am i
    2. where am i
    3. what day is it
    4. etc.
============================================================================
    """
)
def questionmark():
    print("anything else?")
need1 = input("What do you need?")
while need1.upper() == "WHO AM I":
    print("Your Name is Berlian Safri Prakoso")
    questionmark()
    input()
elif need1.upper() == "WHERE AM I":
    print("according to this map, you are in your house, jayakatwang street 60 Madiun")
elif need1.upper() == "WHAT DAY IS IT":
    from datetime import date
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print("today is ", d2)



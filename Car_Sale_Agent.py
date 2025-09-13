def car_sale_agent():
    print("Welcome to the car sale agent :) ")
    print("We sell: luxury, suv and electric cars :) ")
    # This is a task 1 :- 
    task1 = input("Which car do you want to buy? :) :- ")
    if task1 == "i want to buy a suv car":
        print("Robot :- Good choice!!! Do you want me to suggest you some exclusive models? :) ")
    elif task1 == "i want to buy a luxury car":
        print("Robot :- Good choice!!! Do you want me to suggest you some exclusive models? :) ")
    elif task1 == "i want to buy an electric car":
        print("Robot :- Good choice!!! Do you want me to suggest you some exclusive models? :) ")
    else:
        print("Robot :- Sorry, we don't have that category. Try: LUXURY, SUV and ELECTRIC cars. :( ")
        exit()
        return    
    # This is a task 2 :- 
    task2 = input("Which model should i suggest you? :) :- ")
    if task2 == "suggest me some models related to suv category":
        print("Robot :- Okay. try: Defender, Scorpio, VENUE this is a some suv car model name. :) ")
    elif task2 == "suggest me some models related to luxury category":
        print("Robot :- Okay. try: BMW, Audi, Jaguar this is a some luxury car model name. :) ")
    elif task2 == "suggest me some models related to electric category":
        print("Robot :- Okay. try: MG Comet EV, MG Windsor EV, BYD Seal this is a some electric car model name. :) ")
    else:
        print("Robot :- Sorry, we don't have that car name. i suggest you some car name. :( ")
        exit()
        return    
    # This is a task 3 :- 
    task3 = int(input("Can I ask your budget :) :- "))
    if task3 >= 100000 and task3 <= 800000:
        print("Robot :- Recommended: Defender, Scorpio, VENUE (Affordable & reliable). :) ")
    elif task3 >= 1000000 and task3 <= 5000000:
        print("Robot :- Recommended: MG Comet EV, MG Windsor EV, BYD Seal. (Eco-friendly). :) ")
    elif task3 >= 8000000 and task3 <= 10000000:
        print("Robot :- Recommended: BMW, Audi, Jaguar (Spacious & powerful). :) ")
    else:
        print("Sorry, I can't sell any car for this price range. :( ")
        exit()
        return    
    # This is a task 4 :- 
    task4 = input("Do you have any specific choice of color :) :- ")
    if task4 == "can you suggest some color for my car":
        print("Robot :- Yes sir i suggest some color for your car try: Silver, Gray, Black, White. :) ")
    else:
        print("Robot :- Sorry sir this color not available. :( ")
        exit()
        return    
    # This is a task 5 :- 
    task5 = input("Can you give me your opinion on your choice of color :) :- ")
    if task5 == "show me some suggestion for of silver color cars":
        print("Robot :- Nice color choice sir, I also like this color :) ")
    elif task5 == "show me some suggestion for of gray color cars":
        print("Robot :- Nice color choice sir, I also like this color :) ")
    elif task5 == "show me some suggestion for of black color cars":
        print("Robot :- Nice color choice sir, I also like this color :) ")
    elif task5 == "show me some suggestion for of white color cars":
        print("Robot :- Nice color choice sir, I also like this color :) ")
    else:
        print("Robot :- Sorry this color unavailable :( ")
        exit()
        return
    # This is a task 6 :- 
    task6 = input("What is your mode of payment :) :- ")
    if task6 == "cash" or task6 == "card":
        print("Robot :- Congratulation sir for buying a brand new car :) ")
    else:
        print("Sorry, try again your payment is unsuccessful. :( ")
# Run the agent
car_sale_agent()

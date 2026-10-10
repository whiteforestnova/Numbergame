import random
rand = random.randint(1,100)
rand1 =  str(rand)
if rand != 500:
    print("pick a number, 1 through 100, after 15 attempts. you lose")
    extra = 0
    extr2 = 14
    while True:
        askin = int(input(""))
        extra += 1
        extr2 -= 1
        extr3 = str(extr2)
        extr = str(extra)
        if askin == rand:
            print("Congrats you won!!!")
            print("you won on your " + extr + " attempt")
            
            ask = str(input("do you wanna play again?"))
            if ask == "yes":
                pass
            else:
                break
        if askin > rand:
            print("less than that. " + extr3 + " attempts left" )
        if askin < rand:
            print("more than that. " + extr3 + " attempts left")
        
        if extra == 15:
            print("you lost, number was " + rand1)
            ask = str(input("do you wanna play again?"))
            if ask == "yes":
                pass
            else:
                break
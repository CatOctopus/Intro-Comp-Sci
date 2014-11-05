def moovie_dingo():
        total=0
        weather=input("Is it raining? ")
        if weather=="no" or weather=="No":
            numppl=eval(input("How many people are in your party? "))
            for i in range (numppl):
                age=eval(input("Enter your age: "))
                ID=input("Enter if you are a nurse, student, or veteran. ")
                if age<12:
                    price=0
                elif age<60:
                    price=12
                else:
                    price=7
                if ID=="student":
                    price=price*.7
                elif ID=="nurse":
                    price=price*.65
                elif ID=="veteran":
                    price=price*.6
                else:
                    price=price
                print(str(price))
                total=total+price
            print (str(total))
        else:
            print ("We're closed m80")
        

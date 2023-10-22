def payparking(self):
    option = input("Would you like to pay by cash or card?")
    for x in option: 
        if x == "card": 
            print("Please tap your card below.")
            break
            
        elif y == "cash":
            payment = int(input("Enter payment amount using the keypad?"))

            if payment == 50:
                print("Thank you, your payment has been complete.")
            if payment <= 49: 
                print("There is still a remaining balance, please make additional payment.")
            else: 
                print("Payment completed.")

    else:
        print("Invalid response, please choose an either cash or card.")
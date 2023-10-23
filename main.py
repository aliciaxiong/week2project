# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary
# - 50 MAX SPOTS

#Anthony 
# Your parking gargage class should have the following methods:
# - takeTicket
#    - This should decrease the amount of tickets available by 1
#    - This should decrease the amount of parkingSpaces available by 1

#    - payForParking
#    - Display an input that waits for an amount from the user and store it in a variable
#    - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#    - This should update the "currentTicket" dictionary key "paid" to True 
#    - and remember input is just like print, except input is the built in function that displays your message like a print statement but allows 
# the user to enter into the console their input
# so print("My print statement.") > prints the console
#       whatevervariablehere = input("Please enter something here: ") 
#Alicia
#    - payForParking
#    - Display an input that waits for an amount from the user and store it in a variable
#    - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#    - This should update the "currentTicket" dictionary key "paid" to True 

    #Eddie
 # -leaveGarage
#    - If the ticket has been paid, display a message of "Thank You, have a nice day"
#    - If the ticket has not been paid, display an input prompt for payment
#       - Once paid, display message "Thank you, have a nice day!"
#    - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#    - Update tickets list to increase by 1 (meaning add to the tickets list)

class parkingGarage():
    def __init__(self, availability = 50, TakenTicket = False):
        self.parkingSpaces = availability
        self.tickets = availability
        self.TakenTicket = TakenTicket
        self.currentticket = {50 : True}

    def takeTicket(self):
        selfPark = input('Would you like to park your car? yes or no?').lower()
        self.parkingSpaces = 50
        self.tickets = 50
        while True:
            if selfPark == 'yes' and {self.parkingSpaces} != 0:
                print( 'Ticket has been printed, please take and display on your front windshield.')
                self.parkingSpaces -= 1
                self.tickets -= 1
                break
            elif selfPark == 'no' or self.parkingSpaces == 0:
                print( 'Please exit using the right lane, have a nice day :)')
                break
            else:
                print('Error, invalid input. Please restart and try again')
                break
        print(f'Remaining available spaces: {self.parkingSpaces}')

    def payParking(self):
        print("Please scan your ticket.")
        #assuming the ticket has been scanned.
        payment_option = (input("Thank you for choosing us, would you like to pay by cash or card?"))
        while True:  
            if payment_option == "card":
                payment2 = print(input("Please enter your payment and then tap your card below."))
                #assuming the card automatically deducts $50.00
                if self.currentticket[50] == True: 
                    print("Please take your receipt and continue forward to the gate. You have 15 minutes to exit the garage.")
                    break
                elif self.currentticket[50] != True: 
                    print("Please try again.")
                    break
                else:
                    print("Please follow the prompt on screen. Please press the button below for asstance.")
                    break

            if payment_option == "cash":
                payment = int(input("This machine does not provide change, please use exact amount only. Enter payment amount using the keypad."))
                if self.currentticket[50] == True:
                    print("Thank you, your payment has been complete. Please take your receipt and continue forward to the gate. You have 15 minutes to exit the garage.")
                    break
                elif self.currentticket[50] != True: 
                    print("There is still a balance, please make full payment.")
                    break
                else: 
                    print("Please follow the prompt on screen. Please press the button below for asstance.")
                    break 
            else:
                print("Invalid response, please choose either cash or card. Please press the button below for asstance.")
                break 

    def leavegarage(self):
        print("Scan your receipt below.")
        #assuming receipt is good to go
        self.parkingSpaces += 1
        self.tickets += 1
        print("Have a great day, thank you for choosing us.")

    def runner(self):
        while True:
            choice = input('What would you like to do? park, pay, leave ')
            if (choice == 'park'):
                self.takeTicket()
            elif (choice == 'pay'):
                self.payParking()
            elif(choice == 'leave'): 
                self.leavegarage()
            else: 
                print('Invalid input, please try again')
        
projectoop = parkingGarage()
projectoop.runner()

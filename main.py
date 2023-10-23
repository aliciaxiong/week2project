# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary
# - 50 MAX SPOTS

class Parkingarage():
    def __init__(self, taketicket, payparking, leavegarage):
        self.taketickets = []
        self.payparking = []
        self.leavegarage = []
    
    #Anthony 
    # Your parking gargage class should have the following methods:
# - takeTicket
#    - This should decrease the amount of tickets available by 1
#    - This should decrease the amount of parkingSpaces available by 1

    def taketickets(self):
        pass

#Alicia
#    - payForParking
#    - Display an input that waits for an amount from the user and store it in a variable
#    - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#    - This should update the "currentTicket" dictionary key "paid" to True 

    def payparking(self):
        option = input("Would you like to pay by cash or card?")
        for x in option: 
            if x == "card": 
                print("Please tap your card below.")
                break
            elif x == "cash":
                payment = int(input("Enter payment amount using the keypad?"))

                if payment >= 50:
                    print("Thank you, your payment has been complete.")
                if payment <= 49: 
                    print("There is still a remaining balance, please make additional payment.")
                else: 
                    print("Payment completed.")
        else:
            print("Invalid response, please choose an either cash or card.")

    #Eddie
 # -leaveGarage
#    - If the ticket has been paid, display a message of "Thank You, have a nice day"
#    - If the ticket has not been paid, display an input prompt for payment
#       - Once paid, display message "Thank you, have a nice day!"
#    - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#    - Update tickets list to increase by 1 (meaning add to the tickets list)

    def leavegarage(self):
        pass


    projectoop = Parkinggarage('taketicket', 'payparking', 'leavegarage')
    projectoop.runner()
    
    
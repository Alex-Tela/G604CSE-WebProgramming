variable1 = "string 1";
print(variable1.find('str'))


'''
I can create an Account with the following information: username, password...

Once I have an account, I can then change my password, log-in and add a new card.

A card should hold the following details: card number, exp details, billing address, code...

When I have a valid card, I can then search for products.

A product has...

If I find a product I like, I can add it to cart...

Once I have some products added to the cart I can purchase them using the card attached to my account.
'''

'''
Nouns:

-> Account
--properties
--> Username
--> Password
-- actions
--> create
--> change_password
--> login
--> add_card

-- CreditCard
-- Product
-- ShoppingCart
'''

class Account:
    def __init__(self, username, password, credit_card):
        self.username = username
        self.password = password
        self.credit_card = credit_card

    def changePassword(self, new_password):
        if (new_password == self.password):
            print("Change password")
        else:
            self.password = new_password

    def add_card(self, card):
        self.credit_card = card

'''
FE forms collect input
FE JS code makes HTTP request to BE endpoint with user input
BE receives request + input
BE figures out what to do ( and what resources to use)
BE will use the resources methods and data to execute what the user requested
BE resource will return some result (error or data)
'''
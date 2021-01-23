class Payment():

    def __init__(self, name):
        self.total = 0
        self.name = name       
        
        
    def total_sum(self):
        
        while True:
            try:
                payed = (float(input(f"Insert amount payed, if {self.name} is over insert 0 ")))

                if payed != 0:
                    self.total += payed 
                elif payed == 0:
                     break

            except:
                print ("Invalid number, retry")
                continue
        
            
def total_payment(user1_total, user2_total):
    
    total_payed = user1.total + user2.total
    highest_amount = round(( total_payed / 100 ) * 63)
    lowest_amount = round(( total_payed / 100 ) * 37)
    print(f"{user1.name} pays {highest_amount} and {user2.name} pays {lowest_amount}")
    


user1 = Payment('Valentino')
user2 = Payment('Noemi')

user1.total_sum()
user2.total_sum()    
    
total_payment(user1.total,user2.total)             

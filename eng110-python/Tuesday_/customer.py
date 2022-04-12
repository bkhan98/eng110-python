class Customer:
    def __init__(self,name,membership_type):  #We have to put self(initilizer) within any method
        self.name=name    #know as parameters
        self.membership_type=membership_type     # parameters
        # print("customer created")  -  usually dont have print() in init but just for demonstration

    def update_membership(self, new_membership):
        self.membership_type=new_membership

# c= Customer("Caleb", "Premium") - This is possible for single data but when it is for 100's use the next code below
# c2= Customer("Bilal", "Silver")  - The below version is simplified

customers = [Customer("Caleb", "Premium"),
             Customer("Bilal", "Silver")]

print(customers[1].membership_type)
print(customers[1].name)
customers[1]

print(customers[1].membership_type)
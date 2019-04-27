class Good():
    def __init__(self,Id,owner_Id):
        self.Id=Id
        self.owner_Id=owner_Id
    def change_owner_Id(self,Id,address_list):
        number_of_agent=len(address_list)
        for i in range(number_of_agent):       
            if address_list[i][0]==Id:
                self.owner_Id=Id
    def get_owner_Id(self):
        return self.owner_Id
    def get_Id(self):
        return self.Id
    def print_owner_Id(self):
        print("Good",self.Id," is now belong to",self.owner_Id)
    

        

import random
class Agent():
    def __init__(self,Id,address_list):
        self.list=[]
        self.Id=Id
        self.money=random.randint(50,100)
        print("Agent",self.Id,"has",self.money)
        address_list.append([self.Id,self.list])
        #Agent_list.append(self)



    def get_Id(self):
        return self.Id
    def get_Agent_list(self):
        return self.list
    def print_list(self):
        print(self.list)
    def print_number(self):
        print(self.Id)
    def get_Agent(self):
        return self

    
    def process_data(self,address_list):
        for data in range(len(self.list)):
            print("message is received by",self.Id)
            data=self.list[0]
            information_type=data[0]
            Send_Id=data[1]
            receive_Id=data[2]
            price=data[3]
            Good=data[4]
            self.list.remove(self.list[0])
            if information_type== 0:
                self.send(address_list,"accept_bidder",Send_Id,price,Good) 
            if information_type== 2:
                if self.money>price:
                    self.send(address_list,"accept",Send_Id,price,Good)
                else:
                    self.send(address_list,"reject",Send_Id,price,Good)
            if  information_type== 5:
                print(self.Id," won this turn")
            if  information_type== 6:
                print(self.Id,"can not afford ")
            if  information_type== 7:
                print(self.Id,"is winner")
            
    def send(self,address_list,information_type,receive_Id,price,Good):
        number_of_agent=len(address_list)
        for i in range(number_of_agent):        
            if address_list[i][0]==receive_Id:
                if information_type=="accept_bidder":
                    information_type=1
                    price=0
                    Good=0
                    address_list[receive_Id][1].append([information_type,self.Id,receive_Id,price,Good])
                    print("Agent:",self.Id,"message sent accept bidder message to ",receive_Id)

                if information_type=="accept":
                    information_type=3 
                    price=price+random.randint(0,5)
                    if price >self.money:
                        price=self.money
                    address_list[receive_Id][1].append([information_type,self.Id,receive_Id,price,Good])
                    print("Agent:",self.Id," sent accept message sent to",receive_Id)

                if information_type=="reject":
                    information_type=4
                    price=0
                    Good=Good   
                    address_list[receive_Id][1].append([information_type,self.Id,receive_Id,price,Good])
                    print("Agent:",self.Id," sent reject message to" ,receive_Id)


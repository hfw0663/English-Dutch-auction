import random
from Good import Good
class Auctioneer():
    def __init__(self,Id,Number_of_Goods,address_list):
        self.list=[]
        self.Id=Id
        self.Good_list=[]
        address_list.append([self.Id,self.list])
        if Number_of_Goods>0:
            self.Number_of_Goods=Number_of_Goods
            print("Auctioneer",self.Id,"has",self.Number_of_Goods,"Goods")
            for i in range(self.Number_of_Goods):
                self.Good_list.append([int(i),Good(int(i),int(self.Id))])
        else:
            print("Number of good should not be zero")
    def get_Good_list(self):
        return self.Good_list
    def get_Id(self):
        return self.Id
    def get_Agent_list(self):
        return self.list
    def print_list(self):
        print(self.list)
    def print_Id(self):
        print(self.Id)
    def process_data(self):
        data=self.list[0]
        information_type=data[0]
        Send_Id=data[1]
        receive_Id=data[2]
        price=data[3]
        Good=data[4]
        self.list.remove(self.list[0])
        return information_type,Send_Id,price,Good

    def send(self,address_list,information_type,receive_Id,price,Good):
        Number_of_agent=len(address_list)
        for i in range(Number_of_agent):        
            if address_list[i][0]==receive_Id & receive_Id!=self.Id:
                if information_type=="initial_bidding":
                    information_type=0
                    price=0
                    Good=0   
                    address_list[receive_Id][1].append([information_type,self.Id,receive_Id,price,Good])
                    print("Auctioneer:",self.Id," sent initial message to ",receive_Id)
                if information_type=="information_of_good":
                    information_type=2
                    address_list[receive_Id][1].append([information_type,self.Id,receive_Id,price,Good])
                    print("Auctioneer:",self.Id," sent information of Goods message to ",receive_Id)
                if information_type=="result of a turn":
                    information_type=5
                    address_list[receive_Id][1].append([information_type,self.Id,receive_Id,price,Good])
                    print("Auctioneer:",self.Id," sent you win this turn message to ",receive_Id)
                if information_type=="Fail":
                    information_type=6
                    address_list[receive_Id][1].append([information_type,self.Id,receive_Id,price,Good])
                    print("Good",Good,"fail to bid")
                if information_type=="Winner":
                    information_type=7
                    address_list[receive_Id][1].append([information_type,self.Id,receive_Id,price,Good])
                    print("Agent",receive_Id,"is winner of good",Good,"(",price,")")
                #if information_type!="initial_bidding"|"information_of_good"|information_type!="result of a turn"|information_type!="Fail"|information_type!="Winner":
                #    print("Auctioneer",self.Id,"can not send this kind of message")

    def initial_bidding(self,address_list):
        Number_of_agent=len(address_list)
        for i in range(Number_of_agent):
            if address_list[i][0]!= self.Id: 
                self.send(address_list,"initial_bidding",address_list[i][0],0,0)
        print("initial_bidding messages have sent to every agent")
    
    def process_initial_data(self,address_list,Agent_list):
        account=0
        flag=0
        Number_of_processing=len(Agent_list)
        for i in range(Number_of_processing):
            Agent_list[i].process_data(address_list)

        for data in range(Number_of_processing):
            print("message is received")
            data=self.list[0]
            information_type=data[0]
            Send_Id=data[1]
            receive_Id=data[2]
            if receive_Id==self.Id:
                if information_type== 1:
                    account=account+1
                    self.list.remove(self.list[0])
                    print("Agent",Send_Id,"has approved to attent bidding")
                else:
                    print("Wrong type of message")
                    self.list.remove(self.list[0])
                if account==len(address_list)-1:
                    print("All agents are ready")
                    flag=1
                else:
                    flag=0
            else: 
                print("message Id is not match")
        return flag
    
    def English_auction(self,address_list,Agent_list,Good_Id,initial_price,flag,Time):
        if flag==1:
            print("English auction begins")
            English_flag=1
            account=1
            Number_of_agent=len(Agent_list)
            highest_price=initial_price
            Turn_winner=self.Id
            increase=1
            acution_flag=0
            result_list=[]

            while(acution_flag==0):    
                if account<int(Time):
                    Number_of_agent=len(Agent_list)
                    print("price",highest_price)
                    for i in range(1,Number_of_agent+1):
                        if address_list[i][0]!= self.Id: 
                            self.send(address_list,"information_of_good",address_list[i][0],highest_price,Good_Id)

                    for i in range(Number_of_agent):
                        Agent_list[i].process_data(address_list)
                    
                    #print("Auctionner list",self.list)
                    account_accept=0
                    account_same=0
                    same_list=[]
                    for i in range(Number_of_agent):
                        information_type,Agent_Id,Agent_price,Agent_Good_Id=self.process_data()
                        if Agent_Good_Id!=Good_Id:
                            acution_flag=1
                            print("Wrong Id of Good of message.Bidding cancels")
                        
                        if information_type == 3 :
                            account_accept=account_accept+1   
                            if highest_price<Agent_price:
                                highest_price=Agent_price
                                Turn_winner=Agent_Id
                            if highest_price==Agent_price:
                                account_same=account_same+1
                                same_list.append(Turn_winner)
                                same_list.append(Agent_Id)
                    if account_accept>0:
                        if account_same==0:
                            self.send(address_list,"result of a turn",Agent_Id,highest_price,Good_Id)
                            result_list.append([Turn_winner,highest_price])
                            for i in range(Number_of_agent):
                                Agent_list[i].process_data(address_list)
                        else:
                            n=random.sample(list(set(same_list)), 1)
                            self.send(address_list,"result of a turn",n[0],highest_price,Good_Id)
                            result_list.append([n[0],highest_price])
                            for i in range(Number_of_agent):
                                Agent_list[i].process_data(address_list)
                    else:
                        if account == 1:
                            for i in range(Number_of_agent):
                                if address_list[i][0]!= self.Id: 
                                    self.send(address_list,"Fail",address_list[i][0],initial_price,Good_Id)
                            for i in range(Number_of_agent):
                                Agent_list[i].process_data(address_list)
                            acution_flag=1
                        else:    
                            self.send(address_list,"Winner",result_list[account_accept-2][0],result_list[account_accept-2][1],Good_Id)
                            print("result of price",result_list[account-2][1])
                            for i in range(Number_of_agent):
                                Agent_list[i].process_data(address_list)
                            acution_flag=1
                            English_flag=0
                            self.Good_list[Good_Id][1].change_owner_Id(result_list[account_accept-2][0],address_list)
                            self.Good_list[Good_Id][1].print_owner_Id()
                            return English_flag,highest_price
                    print("Information of Good has sent to every agent ,turn:",account)
                    account=account+1
                    highest_price=highest_price+increase
                else:
                    print("Time is running out")
                    acution_flag=1
                    English_flag=1
                    #account=account+1
                    return English_flag,highest_price,account                
        else:
            print("English auction is not allowed")
            account=account+1

    def Dutch_auction(self,address_list,Agent_list,Good_Id,initial_price,reserve_price,flag,account_English,Time):
        if flag ==1:
            print("Dutch auction begins")
            account=account_English
            Number_of_agent=len(Agent_list)
            price=initial_price
            acution_flag=0
            result_list=[]
            Turn_winner=self.Id
            while(acution_flag==0):
                if account<int(Time):
                    print("price",price)
                    for i in range(1,Number_of_agent+1):
                        if address_list[i][0]!= self.Id: 
                            self.send(address_list,"information_of_good",address_list[i][0],price,Good_Id)
                    for i in range(Number_of_agent):
                        Agent_list[i].process_data(address_list)
                    account_accept=0
                    account_same=0
                    same_list=[]
                    for i in range(Number_of_agent):                       
                        information_type,Agent_Id,Agent_price,Agent_Good_Id=self.process_data()
                        if Agent_Good_Id!=Good_Id:
                            acution_flag=1
                            print("Wrong Id of Good of message.Bidding cancels")                      
                        if information_type == 3 :
                            account_accept=account_accept+1
                            same_list.append(Agent_Id)
                            if account_accept<2:
                                Turn_winner=Agent_Id
                            else:          
                                same_list.append(Turn_winner)
                                same_list.append(Agent_Id)
                    if  account_accept==0:
                        price=price/2
                        if price<reserve_price:
                            print("price is lower than reserve price")
                            for i in range(1,Number_of_agent+1):
                                if address_list[i][0]!= self.Id: 
                                    self.send(address_list,"Fail",address_list[i][0],price,Good_Id)

                    else:
                        if account_accept == 1:
                            self.send(address_list,"Winner",Turn_winner,price,Good_Id)
                            acution_flag=1
                            self.Good_list[Good_Id][1].change_owner_Id(Turn_winner,address_list)
                            self.Good_list[Good_Id][1].print_owner_Id()
                        else:
                            price=price*1.2
                            n=random.sample(list(set(same_list)), 1)
                            result_list.append([n[0],price])
                    print("Information of Good has sent to every agent ,turn:",account)
                    account=account+1
                
                else:
                    print("Time is running out")
                    for i in range(1,Number_of_agent+1):
                        if address_list[i][0]!= self.Id: 
                            self.send(address_list,"Fail",address_list[i][0],price,Good_Id)
        else:
            print("Dutch auction is not allowed")

    def print_Good_Id(self):
        n=len(self.Good_list)
        for i in range(n):
            print(self.Good_list[i][1].get_owner_Id())






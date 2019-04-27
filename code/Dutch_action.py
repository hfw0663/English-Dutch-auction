from Agent import Agent 
from Auctioneer import Auctioneer

address_list=[]
Agent_list=[]
##############################################
#You can change these values 
Number_of_Good=2 
Number_of_Agent=3
initial_price=40    #this is the start price of auction
reserve_price=10    #this is the cost of good
Time_English=10     #this is the time of english
Time_Dutch=10       #this is the time of dutch    
rate=3              #this is used to increase the pprice before dutch auction .this value should be higher than 1.
##############################################
#these should not be changed
Time_English=Time_English+1
Time_Dutch=Time_Dutch+1
Auctioneer1=Auctioneer(0,Number_of_Good,address_list)
for i in range(1,Number_of_Agent+1):
    Agent_list.append(Agent(i,address_list))
Good_list=Auctioneer1.get_Good_list()

 
for n in range(Number_of_Good):
    Auctioneer1.initial_bidding(address_list)
    flag=Auctioneer1.process_initial_data(address_list,Agent_list)
    print("Good",Auctioneer1.Good_list[n][1].get_Id(),"is ready to be bade")
    flag,price,account=Auctioneer1.English_auction(address_list,Agent_list,Good_list[n][1].get_Id(),initial_price,flag,Time_English)
    price=price*rate
    Auctioneer1.Dutch_auction(address_list,Agent_list,Good_list[n][1].get_Id(),price,reserve_price,flag,account,Time_Dutch)
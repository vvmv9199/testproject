st=["MAHARASHTRA","KERALA","BIHAR"]
ct=["MUMBAI","THIRUVANANTHANPURAM","PATNA"]
ans='y'
while(ans=='y'):
      flag=0
      states=input("Enter name of the state")
      for i in range(0,len(ct)):
          if(states==st[i]):
              print("capital is ",ct[i])
              flag=1
              break
      if(flag==0):
            print("Error")
      ans=input("want to try again??")
                
              
              
      
      

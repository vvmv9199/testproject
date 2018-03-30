ques=["who was the first prime minister of India?","who is the current CEO of GOOGLE?","what is the capital of Rajasthan?",
   "which city of India is also known as Pink city?","who is the ceo of watsapp?"]
ans=["Jawaharlal Nehru","Sundar pichai","Jaipur","Jaipur","Jan koum"]
m=0
for i in range(0,len(ques)):
    print(ques[i])
    aws=input("Enter the answer")
    if(aws==ans[i]):
        m=m+1
        
print("Your score is ",m)


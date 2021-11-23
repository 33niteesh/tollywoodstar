import random
import webbrowser as wb
print(".                                       Play Tolly wood star Game:                                    .")
lis=['Aa Okkati Adakku','Pelli Neeku Sukham Naaku','Pellaniki Premalekha Priyuraliki Subhalekha','Pellante Noorella Panta','Pellam Chebithe Vinali','Pellam Chatu Mogudu']
while(True):
    l=5
    str1=random.choice(lis)
    li=[str(str1[f].lower()) for f in range(len(str1))]
    l2=["_" for i in range(len(li))]
    while(0==0):
       print(l2)
       print("enter letter:")
       mn=input("")
       s=str(mn)
       if(s not in li):
           l=l-1
           pk="_"
           print("choise remain:",l)
           print("Hint : To know words in title choose space and vovels as word")
       elif(s in li):
         for i in range(len(l2)):
           if(li[i]==s):
               l2[i]=li[i]
               
           
              

       if(l==0):
         
         print("you lost")
         print("press  yes to buy life")   
         hi=input()
         if(hi=="yes"):
           wb.open("https://razorpay.com/payment-link/plink_IOwdYuThVLuG0E")
           l=l+1
         else:
           print('word is:',li)
           print("you lost")
           break
         
         
       if(l2==li):
         p=input("Enter upi:")
         print("you won and hidden word is:",li)
         print("you will recive bonus of rs 12")
         break
       
    break
    
  



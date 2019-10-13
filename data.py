while(True): 
 user_input_length=0
 while(user_input_length<=2 or user_input_length>=10000):
  user_input_length=int(input("введите длину массива в диапозоне от 2 до 10000\n"))
 user_input=input("введите числа") 
 user_input=user_input.replace(" ","").replace(",","") 
 data=list(user_input) 
 data=data[:user_input_length]
 divided_3=[] 
 others=[] 
  
 for num in data: 
  if int(num)%3 == 0: 
   divided_3.append(num) 
  else: 
   others.append(num) 
 divided_3.sort() 
 others.sort() 
 result=divided_3+others 
 print(" ".join(result))

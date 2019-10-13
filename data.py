while(True): 
 user_input=input("введите числа") 
 user_input=user_input.replace(" ","").replace(",","") 
 data=list(user_input) 
 
 divided_3=[] 
 others=[] 
 
 if len(data) >=2 and 10000 >= len(data): 
  for num in data: 
   if int(num)%3 == 0: 
   divided_3.append(num) 
  else: 
   others.append(num) 
 else: 
 print("введите число в интервале от 2 до 10000") 
 divided_3.sort() 
 others.sort() 
 result=divided_3+others 
 print(" ".join(result))

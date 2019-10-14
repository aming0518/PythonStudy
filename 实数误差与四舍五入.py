money=input("input money")
print(money)
print(int(eval(money)),"元")
print(int(eval(money)*10)%10,"角")
print(int(round(eval(money),2)*100)%10,"分")



#10.03    10.02999999 分的单位上会出现误差
 
print(round(10.03,2))
print(round(10.0299999,2))  #四舍五入到两位
#item dictionory
d={"Product A": 20, "Product B": 40, "Product C": 50}
item={}
unit={}
discount={}
discount2={}
l=[]             #discount per item if unit > 10
l_unit=[]   #total unit item-wise
cost= []


t_cost=0
t_unit=0
Prod_A=int(input("enter number of Prod_A unit buy: "))
cost_Prod_A=Prod_A * 20
cost.append(cost_Prod_A)
if (Prod_A)>0:
    item['Prod_A']=cost_Prod_A
    unit['Prod_A']=Prod_A
    l_unit.append(Prod_A)
    t_cost +=cost_Prod_A
    t_unit +=Prod_A
    if (Prod_A>10):
        discount2['Prod_A']=cost_Prod_A * 0.05
        l.append(cost_Prod_A * 0.05)
        
    
Prod_B=int(input("enter number of Prod_B unit buy: "))
cost_Prod_B=Prod_B * 40
cost.append(cost_Prod_B)
if (Prod_B)>0:
    item['Prod_B']=cost_Prod_B
    unit['Prod_B']=Prod_B
    l_unit.append(Prod_B)
    t_cost +=cost_Prod_B
    t_unit +=Prod_B
    if (Prod_B>10):
        discount2['Prod_B']=cost_Prod_B * 0.05
        l.append(cost_Prod_B * 0.05)
    
Prod_C=int(input("enter number of Prod_C unit buy: "))
cost_Prod_C=Prod_C * 50 
cost.append(cost_Prod_C)
if (Prod_C)>0:
    item['Prod_C']=cost_Prod_C
    unit['Prod_C']=Prod_C
    l_unit.append(Prod_C)
    t_cost +=cost_Prod_C
    t_unit +=Prod_C
    if (Prod_C>10):
        discount2['Prod_C']=cost_Prod_C * 0.05
        l.append(cost_Prod_C * 0.05)
    
print(item,unit)
if (len(l)>0):
    m=max(l)
#print(m)
#print(discount2)
for i in discount2:
    if (discount2[i]==m):
        discount['bulk_5_discount']=m

if (t_cost)>200:
    t_cost= t_cost - 10
    discount['flat_10_discount']=10
if (t_unit>20):
    t_cost = t_cost - (t_cost * 0.1)
    discount['bulk_10_discount']=round(t_cost * 0.1, 1)
    
k=max(cost)
#print(k)
if (t_unit > 30):
    for j in unit:
        if (unit[j]>15):
            if (item[j]==k):
                if (j =='Prod_A'):
                    t_Prod_A=unit[j] * 20
                    z= t_Prod_A - (t_Prod_A * 0.5)
                    discount['tired_50_discount']=z
                    break
                elif (j =='Prod_B'):
                    t_Prod_B=unit[j] * 40
                    z= t_Prod_B - (t_Prod_B * 0.5)
                    discount['tired_50_discount']=z
                    break
                elif (j =='Prod_C'):
                    t_Prod_C=unit[j] * 50
                    z= t_Prod_C - (t_Prod_C * 0.5)
                    discount['tired_50_discount']=z
                    break
            
# print(discount)
# print(discount2)
print(discount)

subtotal=0
l2=[] #discount value
for i in item:
    subtotal +=item[i]
    print(i,unit[i], item[i] )
print("Subtotal: ",subtotal)
for i in discount:
    l2.append(discount[i])
m3=max(l2)
for i in discount:
    if (discount[i]==m3):
        print(i,m3)
main_total=subtotal - m3
ask=['y','Y','Yes','yes']
ask_4_gift=input("Do you want for gift wrap:")
if (ask_4_gift in ask):
    gift_fee= t_unit * 1
    shipping_fee= (t_unit/10) * 5
    print('shipping_fee:',shipping_fee)
    print('gift_fee:',gift_fee)
    print("Total: ",main_total + gift_fee + shipping_fee) 
else:
    print("Total: ",main_total)
    
    
    
    
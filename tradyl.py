country_code=input("enter the country  name")
product_code=input("enter the  product_code")
weight_in_kg=float(input("enter the  weight_kg"))
if country_code=="UK" and weight_in_kg<5:
    shipping_cost=5
elif country_code=="UK" and weight_in_kg>=5:
    shipping_cost=15
elif country_code=="US" and weight_in_kg<10:
    shipping_cost=5
elif country_code=="US" and weight_in_kg>=10:
    shipping_cost=15
else:
    shipping_cost=0
if product_code[0:3]=="123" and  len(product_code)>0 and len(product_code)<=8:
        final_value=shipping_cost*1.2*(1+0.18)
        print(final_value,"INR")
elif product_code[0:3]=="234" and len(product_code)>0 and len(product_code)<=8:
        final_value_one=shipping_cost*1.5*(1+0.18)
        print(final_value_one,"INR")
else:
    final_value_two=shipping_cost*1*(1+0.18)
    print(final_value_two,"INR")

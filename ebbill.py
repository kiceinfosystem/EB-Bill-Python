print("Prepare EB Bill...")

ebno=input("Enter a EB  Number ")
pu=int(input("Enter a Previous Unit "))
cu=int(input("Enter a Current Unit "))
plan=input("Enter a Plan ")

nu=cu-pu
print("The total unit is ",nu)
print("Your plan is ",plan)

if plan=="home":
    print("Your plan is Home")

    if nu<=100:
        amt=0
    elif nu>100 and nu<=500:
        amt=(nu-100)*2 +0
       
    elif nu>500:
        amt=(nu-500)*5 + 0+800
        
        
elif plan=="industry":
    print("Your plan is Industry")
    if nu<=100:
        amt=nu*5
    elif nu>100 and nu<=500:
        amt=(nu-100)*10 +500
    elif nu>500:
        amt=(nu-500)*15 + 500+4000
elif plan=="commercial":
    print("Your plan is Commercial")
    if nu<=100:
        amt=nu*8
    elif nu>100 and nu<=500:
        amt=(nu-100)*15 +800
    elif nu>500:
        amt=(nu-500)*20 +800+6000


print("Total Amount=",amt)

gst=(amt*5)/100

print("GST Amount is ",gst)

namt=amt+gst

print("Net amount is ",namt)
          

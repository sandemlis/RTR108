hrs = input("Enter Hours:") #45 Hours
h = float(hrs)
rate = input("Enter Rate:") #10.50 Rate
r = float(rate)
if h > 40 :
	pay = ((h-40)*r*1.5)+40*r
else:
    pay=h*r
print(pay) #498.75 Pay

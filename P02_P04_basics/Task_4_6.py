def computepay(h,r):		   #Definē funkciju
    if h>40:
        pay=40*r+(h-40)*r*1.5
    else:
        pay=h*r
    return pay

hrs = float(input("Enter Hours:")) #Ievadam 45 stundas
rate = float(input("Enter Rate:")) #Ievadam 10.50 stundas likmi
p = computepay(hrs,rate)	   #Piesaucam definēto funkciju
print("Pay",p)			   #Izvada algu

#To find p
def prime(p):
	if p>1:
		for i in range(2,p):
			if((p%i) ==0):
				print("number is not prime",p)
				break
		else:
			print("number is prime ",p)
	else:
		print("number is not prime ",p)
#to find q
def prim(q):
	if q>1:
		for i in range(2,q):
			if((q%i) ==0):
				print("number is not prime",q)
				break
		else:
			print("number is prime ",q)
	else:
		print("number is not prime ",q)
p=int(input("enter a positive number = "))
prime(p) 
q=int(input("enter a positive number = "))
if(p!=q):
	prim(q)
else:
	print("both number is same")
#to find n or Φn
print("p=",p)
print("q=",q)
n=p*q
print("n=",n)
pn=(p-1)*(q-1)
print("Φ(n) = ",pn)
# to find e
def e(e,pn):
 print("**condition1: e must be greater than and less than phai of n**")
 e=int(input("Enter the value of e ="))
 pn=int(input("Enter the value of Φn ="))
 e(e,pn)
 while True:
    if e > 1 and e < pn:
      print("e or Φn fullfill the above condition")
      if pn > e:
        temp = pn
        pn = e
        e = temp
        for i in range(1, pn):
            if e % i == 0 and pn % i == 0:
                gcd = i
            print("GCD of e or Φn is =", gcd)
        if gcd != 1:
            print("GCD of e or Φn is not equal to 1")
            e = int(input("So, enter a new 'e'"))
            if gcd == 1:
             break
# to find d 
def D(e,pn):
 for k in range(1, e+1):
  d = ((k*pn)+1)/e
  if d == int(d):
    ans = int(d);
    print("d=", ans)
e= int(input("enter the value of e="))
pn= int(input("enter the value of pn="))
D(e,pn)
# for encryption or decryption
m=int(input("enter the value of m="))
e=int(input("enter the value of e="))
me=pow(m,e);
C=me%n;
print("power=",me);
print("C=",C);
r=int(input("Enter the value of d"))
Cr=pow(C,r);
m=Cr%n;
print("power=",Cr);
print("M=",m);

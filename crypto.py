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
def root(p):
    for i in range(1, p-1):
        for r in range(1, p-1):    
             if(pow (r,i) % p != 1):  
                print("primative root is = ",r)
                return r
p=int (input ("enter a larger prime number = "))  
prime(p)
r=root(p) 
k = int(input("Enter a secert key (k): "))
a=pow(r,k)%p #now computing a
print( "a is =",a )
print ("encryption")
ks = int (input("enter a random integres for encryption ks= "))
m = int (input("enter a integres for encryption which is less then prime number  m= "))
s=pow(r,ks)%p
print ("s" ,s)
t=(pow(a,ks)*m)%p
print ("t",t)
print ("decryption")
D = ((t * pow(s, -k, p)) % p)  
print ("Decrypt message =",D)
print("\nSTUDENT  NAMES                   ROLL NUMBER")
print("SHAFAT-E-RASOOL                S22BINCE1M03028")
print("MUHAMMAD FAHAD SAEED           S22BINCE1M03015")
print("TEHREEM AMNA                   S22BINCE1M03012")

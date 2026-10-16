n= int(input(" Enter a Number: "))

print("--------------------------------- SQUARE PATTERN -------------------------------")

print(" Star Square Pattern: ")
for i in range(n):
    for j in range (n):
        print("*", end=" ")
    print()

print(" Number Square Pattern: ")
for i in range(1,n+1):
     for j in range(1,n+1):
          print(j, end=" ")
     print()

print(" Number Square Zig-Zag Pattern: ")
for i in range(1,n+1):
     for j in range(1,n+1):
          if(i+j)%2==0:
               print("1", end=" ")
          else:
               print("0", end=" ")
     print()

print(" Hollow Star Square Pattern: ")
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print(" Hollow Number Square Pattern: ")
for i in range(1, n+1):
     for j in range(1,n+1):
          if i==1 or i==n or j==1 or j==n:
               print(j, end=" ")
          else:
               print(" ", end=" ")
     print()

print("--------------------------------- RIGHT ANGLED TRIANAGLE AND ITS INVERSE PATTERN -------------------------------")

print(" Star Right Angled Triangle Pattern: ")
for i in range (1,n+1):
    print(" * " * i)

print(" Star Inverse Right Angled Triangle Pattern: ")
for i in range(n,0,-1):
    print(" * " * i)

print(" Number Right Angled Triangle Pattern: ")
for i in range(1,n+1):
    for j in range(1,i+1):
          print(j, end=" ")
    print()

print(" Number Inverted Right Angled Triangle Pattern: ")
for i in range(n,0,-1):
    for j in range(1,i+1):
          print(j,end=" ")
    print()

print(" Alphabet Right Angled Triangle Pattern: ")
for i in range(1,n+1):
    for j in range(1,i+1):
          print(chr(64+j),end=" ")
    print()

print(" Alphabet Inverted Right Angled Triangle Pattern: ")
for i in range(n,0,-1):
    for j in range(1,i+1):
          print(chr(64+j),end=" ")
    print()

print(" Hollow Star Right Angled Triangle Pattern: ")
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or i==n or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(" Hollow Star Inverted Right Angled Triangle Pattern: ")
for i in range(n,0,-1):
     for j in range(1,i+1):
          if j==1 or i==n or i==j:
               print("*",end=" ")
          else:
               print(" ",end=" ")
     print()

print("--------------------------------- PYRAMID AND ITS INVERSE PATTERN -------------------------------")

print(" Star Pyramid Pattern: ")
for i in range (1,n+1):
    print(" " * (n-i) + "*" * (2 * i-1))

print(" Star Inverted Pyramid Pattern: ")
for i in range (n,0,-1):
     print(" "* (n-i) + "*" * (2 * i-1))

print(" Number Pyramid Pattern: ")
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k, end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()

print(" Number Inverted Pyramid Pattern: ")
for i in range(n,0,-1):
    for j in range(n-i):
         print(" ",end=" ")
    for k in range(1,i+1):
         print(k,end=" ")
    for l in range(i-1,0,-1):
         print(l,end=" ")
    print()

print(" Alphabet Pyramid Pattern: ")
for i in range(1,n+1):
    for j in range(n-i):
          print(" ",end=" ")
    for k in range(1,i+1):
         print(chr(64+k),end=" ")
    for l in range(i-1,0,-1):
         print(chr(64+l),end=" ")
    print()

print(" Alphabet Inverted Pyramid Pattern: ")
for i in range(n,0,-1):
    for j in range(n-i):
          print(" ",end=" ")
    for k in range(1,i+1):
         print(chr(64+k),end=" ")
    for l in range(i-1,0,-1):
         print(chr(64+l),end=" ")
    print()

print(" Hollow Star Pyramid Pattern: ")
for i in range(1,n+1):
    for j in range(n-i):
          print(" ",end=" ")
    for k in range(1,2*i):
         if k==1 or k==2*i-1 or i==n:
              print("*", end=" ")
         else:
              print(" ",end=" ")
    print()

print(" Hollow Star Inverted Pyramid Pattern: ")
for i in range(n,0,-1):
     for j in range(n-i):
          print(" ", end=" ")
     for k in range(1,2*i):
          if k==1 or k==2*i-1 or i==n:
               print("*", end=" ")
          else:
               print(" ", end=" ")
     print()

print("--------------------------------- DIAMOND PATTERN -------------------------------")

print(" Star Diamond Pattern: ")
for i in range (1,n+1):
    print(" " * (n-i)+ "*" * (2*i-1))
for i in range(n-1,0,-1):
    print(" " * (n-i)+ "*" * (2*i-1))

print(" Number Diamond Pattern: ")
for i in range(1,n+1):
    for j in range(n-i):
          print(" ",end=" ")
    for k in range(1,i+1):
         print(k,end=" ")
    for l in range(i-1,0,-1):
         print(l,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
          print(" ",end=" ")
    for k in range(1,i+1):
         print(k,end=" ")
    for l in range(i-1,0,-1):
         print(l, end=" ")
    print()

print(" Alphabet Diamond Pattern: ")
for i in range (1,n+1):
    for j in range(n-i):
          print(" ", end=" ")
    for k in range(1,i+1):
         print(chr(64+k),end=" ")
    for l in range(i-1,0,-1):
         print(chr(64+l),end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
          print(" ", end=" ")
    for k in range(1,i+1):
         print(chr(64+k),end=" ")
    for l in range(i-1,0,-1):
         print(chr(64+l),end=" ")
    print()

print(" Hollow Star Diamond Pattern: ")
for i in range(1,n+1):
     for j in range(n-i):
               print(" ",end=" ")
     for k in range(1,2*i):
              if k==1 or k==2*i-1:
                   print("*", end=" ")
              else:
                   print(" ",end=" ")
     print()
for i in range(n-1,0,-1):
     for j in range(n-i):
          print(" ", end=" ")
     for k in range(1,2*i):
          if k==1 or k==2*i-1:
               print("*", end=" ")
          else:
               print(" ", end=" ")
     print()

print("--------------------------------- BUTTERFLY PATTERN -------------------------------")

print(" Star Butterfly Pattern: ")
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
            print("*",end=" ")
    for k in range(2*(n-i)):
            print(" ",end=" ")
    for j in range(i):
            print("*", end=" ")
    print()

print(" Hollow Star Butterfly Pattern:  ")
for i in range(1,n+1):
     for j in range(1,i+1):
          if j==1 or j==i:
               print("*",end=" ")
          else:
               print(" ",end=" ")
     for j in range(2*(n-i)):
          print(" ",end=" ")
     for j in range(1,i+1):
          if j==1 or j==i:
               print("*",end=" ")
          else:
               print(" ",end=" ") 
     print()
for i in range(n,0,-1):
     for j in range(1,i+1):
          if j==1 or j==i:
               print("*",end=" ")
          else:
               print(" ",end=" ")
     for j in range(2*(n-i)):
          print(" ",end=" ")
     for j in range(1,i+1):
          if j==1 or j==i:
               print("*",end=" ")
          else:
               print(" ",end=" ")
     print() 

print("--------------------------------- OTHER PATTERNS -------------------------------")

print(" Star Plus Pattern: ")
for i in range(1,n*2):
    for j in range(1,n*2):
        if(i==n) or (j==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print(" Star Cross Pattern: ")
for i in range(1,n+1):
     for j in range(1,n+1):
          if (i==j) or (i+j==n+1):
               print("*", end=" ")
          else:
               print(" ", end=" ")
     print()

print("Floyd's Triangle Pattern: ")
r=1
for i in range(1,n+1):
    for j in range(1,i+1):
          print(r,end=" ")
          r=r+1
    print()

print(" Pascal's Triangle Pattern: ")
for i in range(n):
     print(" "*(n-i),end=" ")
     r=1
     for j in range(i+1):
         print(r,end=" ")
         r = r*(i-j)//(j+1)
     print()
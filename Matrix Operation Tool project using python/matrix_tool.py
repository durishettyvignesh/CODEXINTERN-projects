import numpy as np

r1 = int(input("rows of 1st matrix : "))
c1 = int(input("cols of 1st matrix : "))

r2 = int(input("rows of 2nd matrix : "))
c2 = int(input("cols of 2nd matrix : "))


print("Enter 1st matrix :")
a = []
for i in range(r1):
      row = list(map(int,input().split()))
      a.append(row)

print("Enter 2nd matrix :")
b = []
for i in range(r2):
      row = list(map(int,input().split()))
      b.append(row)

a = np.array(a)
b = np.array(b)


print()
print("1 - add")
print("2 - sub")
print("3 - mul")
print("4 - trp")
print("5 - det")
print()

ch = int(input("what u want ? : "))

print()

if (ch == 1):
      if (a.shape == b.shape):
            print("ans :")
            print(a + b)
      else:
            print("not same shape")

elif (ch == 2):
      if (a.shape == b.shape):
            print("ans :")
            print(a - b)
      else:
            print("not same shape")

elif (ch == 3):
      if (a.shape[1] == b.shape[0]):
            print("ans :")
            print(a @ b)
      else:
            print("not valid for mul")

elif (ch == 4):
      print("1st trp :")
      print(a.T)
      print()
      print("2nd trp :")
      print(b.T)

elif (ch == 5):
      if (a.shape[0] == a.shape[1]):
            print("det of 1st : ",round(np.linalg.det(a),2))
      else:
            print("1st not sq")

      if (b.shape[0] == b.shape[1]):
            print("det of 2nd : ",round(np.linalg.det(b),2))
      else:
            print("2nd not sq")

else:
      print("wrong ch")


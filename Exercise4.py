n = int(input("Enter your number: "))
dList = []
for i in range(1, n+1):
 if n % i == 0:
  dList.append(i)
print(dList)
# &
print([i for i in range(1, n+1) if n % i == 0])

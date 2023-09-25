text = input()
count = 0
count_max=0
for i in range (len(text)):
    if text[i]==" ":
        count+=1
    else:
        count_max=max(count,count_max)
        count=0

print(count_max)
text = input()
count = 1
count_max=0
for i in range (len(text)-1):
    if text[i]==text[i+1]:
        count+=1
    else:
        count_max=max(count,count_max)
        count=1

count_max=max(count,count_max)
print(count_max)
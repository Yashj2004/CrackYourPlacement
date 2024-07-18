d={}
word="geeksforgeeks”
for i in range(len(word)):
    if word[i] in d:
        d[word[i]]+=1
    else:
        d[word[i]]=1
for key,count in d.items():
    if count>1:
        print(f"{key}, count: {count}")

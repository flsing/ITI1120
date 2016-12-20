s1="good"
s2="bad"
s3="silly"

#Task 1

print("ll" in s3)

print(s1!=(" "))
print(s1+s2+s3)
print(s1+s2+s3==" ")
print ((s3*10))
print (len(s1+s2+s3))


#Task 2

aha="abcdefgh"

print(aha[:4])
print(aha[3:6])
print(aha[-1])
print(aha[-3:-1])
print(aha[3:])
print(aha[-3:])
print(aha[0:7:3])
print(aha[1:5:3])


#Task 3

s = '''It was the best of times, it was the worst of times;it was the age
of wisdom, it was the age of foolishness;it was the epoch of belief, it was
the epoch of incredulity;it was ...'''

newS= s.replace(","," ")
newS=newS.replace(";"," ")
newS=newS.replace("\n"," ")
newS=newS.replace("."," ")
newS=newS.strip()
newS=newS.lower()
print(newS.count("it was"))
newS=newS.replace("was","is")
print(newS)

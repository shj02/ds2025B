s1 = list()
print(len(s1))
s1.append("Data structure") #push
s1.append("DataBase") #push
print(len(s1)) #size
print(s1[-1])  # peek > ['Data structure', 'DataBase']
s1.pop()
print(s1) #['Data structure']
s1.pop()
print(s1) #[]
# s1.pop()
# print(s1) 더 이상 뺄 게 없어서 오류 발생
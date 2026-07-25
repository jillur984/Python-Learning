# identy operator

a=10
b=20
print(id(a)) # RAM a kothay ase sei address ta dekhabe
print(id(b))


print(a is b) # 2 ta somman object kina ta check korbe


a="jillur"
b="jillur"
print(a is b) # true
print(a is not b) # false


# membership operator

a=[1,2,3,4,5]
m=3
print( m in a) # true

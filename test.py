hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
hour = ((mins+ dura%60))
# hour = (hour + dura//60 + (mins+ dura%60)//60)%24
# mins = (mins+ dura%60)%60
# print(hour,":",mins,sep="")

# a = (hour+dura)//60
print(hour)
# print(hour,":",a)
# mins+=a-60
# print("a= ",a)


# print(hour,":",a)
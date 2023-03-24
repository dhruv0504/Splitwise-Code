no_of_person = int(input("Enter no. of person:\t"))
names = []
expenses = []
indi_exp = 0 
net_amnt = []


for n in range(no_of_person):
    name = str(input(f"Enter Name {n+1}: \t"))
    expense = int(input(f"{name}, Enter your expense: \t"))
    names.append(name)
    expenses.append(expense)
    indi_exp += expense/no_of_person

for exp in expenses:
    net_amnt.append(round(exp-indi_exp,2))
# print(net_amnt)


flag = 0
while(flag == 0):
    if abs(max(net_amnt)) >= abs(min(net_amnt)):
        # print(abs(max(net_amnt)))
        # print(min(net_amnt))
        # print(abs(min(net_amnt)))
        # print(names[net_amnt.index(min(net_amnt))])
        # print(names[net_amnt.index(max(net_amnt))])
        print(f"{names[net_amnt.index(min(net_amnt))]} has to give {names[net_amnt.index(max(net_amnt))]} rupees {round(abs(min(net_amnt)),2)}")
        net_amnt[net_amnt.index(max(net_amnt))] += min(net_amnt)
        # print(net_amnt[net_amnt.index(max(net_amnt))])
        net_amnt[net_amnt.index(min(net_amnt))] = 0
        # print(net_amnt[net_amnt.index(min(net_amnt))])
        # print(net_amnt)
        
    else:
        # print(abs(max(net_amnt)))
        # print(min(net_amnt))
        # print(abs(min(net_amnt)))
        # print(names[net_amnt.index(min(net_amnt))])
        # print(names[net_amnt.index(max(net_amnt))])
        print(f"{names[net_amnt.index(min(net_amnt))]} has to give {names[net_amnt.index(max(net_amnt))]} rupees {round(abs(max(net_amnt)),2)}")
        net_amnt[net_amnt.index(min(net_amnt))] += max(net_amnt) 
        # print(net_amnt[net_amnt.index(min(net_amnt))])
        net_amnt[net_amnt.index(max(net_amnt))] = 0
        # print(net_amnt[net_amnt.index(max(net_amnt))])
        # print(net_amnt)
    
    # flag -= 1
    for i in range(len(net_amnt)):
        if int(net_amnt[i]) == 0 :
            flag = 1
        else:
            flag = 0
            break
    
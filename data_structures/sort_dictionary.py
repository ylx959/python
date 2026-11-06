fruits={"banana":123,"apple":34,"orange":234,"coconut":23}

#fruits.sort() list
#fruits=tuple(sorted(fruits))
#fruits=dict(sorted(fruits.items()))
fruits=dict(sorted(fruits.items(),key=lambda item:item[0],reverse=True)) #item[0]依key排序，reverse=True是由大到小
#fruits=dict(sorted(fruits.items(),key=lambda item:item[1],reverse=True))
print(fruits)
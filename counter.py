counter={}

def addToCounter(country):
    if country in counter:
        counter[country]+=1
    else:
        counter[country]=1
addToCounter("India")
addToCounter("US")
addToCounter("India")


print(len(counter))
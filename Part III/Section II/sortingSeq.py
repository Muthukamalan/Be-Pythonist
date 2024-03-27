a = {'a':300,'b':1,'c':30,'d':43,'e':-12}
# functionReturnValues = lambda k:a[k]
def functionReturnValues(k):
    return a[k]
print(sorted(a,key= functionReturnValues,reverse=True))


t = 0, 10+10j, 3-3j, 4+4j, 5-2j
print(sorted(t,key=lambda i:abs(i)))


sentences = 'this', 'bird', 'is', 'a', 'late', 'parrot'
print(sorted(sentences,key=lambda i:len(i)))
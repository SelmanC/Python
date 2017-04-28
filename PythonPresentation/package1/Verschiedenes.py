

liste = ["Eins", "Zwei", "Drei", 5, 6, 7]

print("Liste:")
for l in liste:
    print(l)
    
print("Drei" in liste)
    
    
set = set([0,1, 2, 2, 1])

print("\nSet:")
for s in set:
    print(s)
    
    
map = {1: "..."}
map[10] = "Hallo"
map[20] = "Welt"
map[4] = "!"

print("\nDictionary:")
for key, value in map.items():
    print("Key:", key,"Value:", value)
    
print("10=" + map.get(10))

tuple = ("Hallo", "Welt", "Tuple")

a, b, c = tuple
print("\nTupple:")
print(a,b,c)


print("\nFor Schleife:")

for i in range(5, 20, 2):
    print(i)
    
i = 0
end = False

print("\nWhile Schleife")
while(i<=5 and end is False):
    i+=1
    if(i == 3):
        end = True
        
    elif(i == 4):
        print("Geht gar nicht")
    
    else:
        print(i)
        

print("\List comprehension:")

l = []
    
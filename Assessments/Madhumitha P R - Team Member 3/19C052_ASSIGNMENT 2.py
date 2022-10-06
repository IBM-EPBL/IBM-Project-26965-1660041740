import random
temperature = random.randint(10, 300)
print(temperature)
humidity = random.randint(10, 102)
print(humidity)
if(temperature >= 150):
   print("Hazard")
elif(humidity >= 70):
   print("Hazard")
else:
   print("Not Hazard")

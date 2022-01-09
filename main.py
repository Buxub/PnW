from datetime import datetime, timedelta
#from beige import Beige


#input
turns = 7
heures = turns * 2



#calculations
if datetime.now().hour % 2 == 0:
    outOfBeige = datetime.now().replace(microsecond=0, second=0, minute=0) + timedelta(hours=heures)
else:
    outOfBeige = datetime.now().replace(microsecond=0, second=0, minute=0) + timedelta(hours=heures-1)

#output
print("Turns left: %s " % turns)
print("Hours left: %s " % heures)
print("Out of beige at:")
print(outOfBeige)





#land
moneyAvailable = 2,327,183.43
currentLand = 3000.0



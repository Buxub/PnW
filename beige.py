#think this works except I cannot remember why i made it



from datetime import datetime, timedelta
#datetime is part of python3


class Beige:

    def __init__(self, turns):
        self.turns = turns

    def beigeTime1(self):
        heures = self.turns * 2
        if datetime.now().hour % 2 == 0:
            print(datetime.now().replace(microsecond=0, second=0, minute=0) + timedelta(hours=heures))
        else:
            print(datetime.now().replace(microsecond=0, second=0, minute=0) + timedelta(hours=heures-1))

    beigeTime = Beige.beigeTime1

test = Beige(1)
Beige.beigetime(test)

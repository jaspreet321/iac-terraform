#multiple level inherittence, where class 'enhacment' is inhertting both the above classes 'employee' & 'player'

class employee:
    company = "disco"

class player:
    company = "cricket"

    def getplayerinsight(self):
        print("This employee is a good cricketer....\n")

class enhancement(employee, player):
      insight = "improvement"

e = employee()
p = player()
enh = enhancement()

enh.getplayerinsight()    #result of this line will show that inheritted class doesn't only inheritts the attributes of other class, but al                          so the function within those classes.

cash = float(17.50)
hours = float(raw_input("Hours worked in the past two weeks? ")) # def hours

def payment(): # calc reg pay
    return hours * cash

def over():
    if hours > 80:
        OT = (hours - 80) * 8.75 # calc overtime hours
        return OT
    else:
        OT = 0
        return OT

def final():
    return payment() + over()

print "Congrats! You've earned", final() , " dollars this pay period."

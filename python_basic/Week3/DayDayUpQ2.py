# DayDayUpQ2.py
def proAndRetro(dayfactor):
    dayup = pow(1 + dayfactor, 365) 
    daydown = pow(1 - dayfactor, 365)
    print("Progress: {:.2f}, Retrogress: {:.2f}".format(dayup, daydown))

df = 0.005
proAndRetro(df)
df = 0.01
proAndRetro(df)

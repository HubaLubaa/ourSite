from Person import Person
from Schedule import Schedule
import random
import math

    
admin = Person("Admin","M","1","1","1970","0",True)
admin.signUp()
sheetsID = "1kkxWR1f67VKH8Sjv1Cfe_yth6hKR58AITFSm32j6ojA"

tmp = Schedule(30)
tmp.createSchedule()
time = tmp.getFreeTime()

oldGirl = Person("89134829304","F","10","12","1960","1",False)
oldGirl.signUp()
oldGirl.visit("109","4")

'''weekDay = list(tmp.schedule.keys())
countLearn = Person.countLearn
mas = ["M","F"]
for i in range(countLearn):
    number = "+79134627228"
    randDay = str(random.randint(1,27))
    randMonth = str(random.randint(1,12))
    randYear = str(random.randint(1935,2010))
    randSex = mas[random.randint(0,1)]
    personID = str(i)
    isAdmin = False

    person = Person(number,randSex,randDay,randMonth,randYear,personID,isAdmin)
    person.signUp()

    randWeekDay = random.randint(0,6)
    randHour = random.randint(0, 18)
    totalTime = weekDay[randWeekDay] + " " +time[randWeekDay][randHour][1] # = День недели + Время (Понедельник 9:30)

    #person.visit("109",totalTime) # Обычная запись по одному человеку(долго)
    person.visitAnalytics("109",totalTime) # Статистика, запись по n человек

admin.writeAllData("A2:"+str(countLearn+1),Person.lerningData,sheetsID)



midRanges = [[0 for i in range(2)]for i in range(10)]
for i in range(10):
    for k in range(2):
        summ = sum(Person.statistics[i][k])
        lenn = len(Person.statistics[i][k])
        if lenn != 0:
            midRanges[i][k] = summ/lenn
    
arr = [[""],[""]]
for k in range(2):
    for i in range(1,8):
        arr[k].append(str(math.ceil(int(midRanges[i][k])/10)*10))
        
admin.writeRowsAnalitics("H-O",arr[0], 2 ,sheetsID)     # Средние мужчины
admin.writeRowsAnalitics("H-O",arr[1], 4 ,sheetsID)'''     # Средние женщины

        
    
    

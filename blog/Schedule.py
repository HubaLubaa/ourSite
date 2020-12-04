import datetime

class Schedule():

    busy = []
    weekDays = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"] # Дни недели
    schedule = {}
    counter = 0
    check = False

    def correctSchedule(self,visitTime,duration):
        day,ID = visitTime
        i = int(ID)+1
        while(i % 19 != 0):
            if i not in Schedule.busy:
                Schedule.schedule[day][i] -= 30-duration
            else:
                return
            i+=1


    # Можно использовать как врач отошел на несколько минут
    # так и пациент опоздал
    # так и очередь не двигается долгое время



    def missingDoctor(self,duration,IDmissing):
        i = IDmissing
        day = Schedule.weekDays[int(IDmissing/19)]
        while(i % 19 != 0):
            Schedule.schedule[day][i] += duration
            i+=1

    # Можно использовать как пациент не пришел
    # так
    def patientLeft(self,patient):
        Schedule.busy.remove(patient.busyIndex)
        day = Schedule.weekDays[int(patient.busyIndex/19)]
        i = patient.busyIndex+1
        while(i % 19 != 0):
            Schedule.schedule[day][i] -= patient.duration
            i+=1
        
    def getVisitTimeNormal(self,day,ID):
        return Schedule.schedule[day][ID]//60,Schedule.schedule[day][ID]%60
    
    def getVisitTime(self,ID):
        return Schedule.schedule[0][ID]
    
    def getFreeTime(): # Получение свободных дат приема
        if Schedule.counter == 0:
            Schedule.schedule = {}
            Schedule.schedule["Понедельник"] = {}
            Schedule.schedule["Вторник"] = {}
            Schedule.schedule["Среда"] = {}
            Schedule.schedule["Четверг"] = {}
            Schedule.schedule["Пятница"] = {}
            Schedule.schedule["Суббота"] = {}
            Schedule.schedule["Воскресенье"] = {}
            ID = 0
            for day in Schedule.schedule.keys():
                for i in range(480, 1021, 30):
                    Schedule.schedule[day][ID] = i
                    ID += 1
            Schedule.check = True

        mas = []
        i = 0
        for day in Schedule.schedule.keys():
            for person in Schedule.schedule[day].keys():
                if person not in Schedule.busy: 
                    time = Schedule.convertFromMinutsToStandart(Schedule.schedule[day][person])
                    mas.append((str(person),str(day)+" "+str(time)))
            i+=1
        return tuple(mas)
    
    def setBusy(self,ID):
        Schedule.busy.append(ID)
        
    def convertFromMinutsToStandart(minuts):
        if minuts%60 == 0:
            return str(minuts//60)+":"+str(minuts%60)+"0"
        elif (minuts%60)/10 < 1:
            return str(minuts//60)+":"+"0"+str(minuts%60)
        else:
            return str(minuts//60)+":"+str(minuts%60)
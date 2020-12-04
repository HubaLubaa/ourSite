from pprint import pprint
from .Schedule import Schedule
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import random
import datetime

class Person():
    
    weekDays = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"] # Дни недели
    #months = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
    countLearn = 500
    counterRegistred = 0
    counterVisit = 0
    statistics = [[[] for i in range(2)] for i in range(10)]
    lerningData = [[] for i in range(countLearn)]

    def __init__(self):
        print("You added user")

    def addData(self,phoneNumber,sex,birthDay,birthMonth,birthYear):
        self.phoneNumber = phoneNumber
        self.sex = sex
        birthDate = datetime.datetime(int(birthYear), int(birthMonth), int(birthDay))
        self.age = Person.calculate_age(birthDate)
        self.ages = [birthDay,birthMonth,birthYear]
        self.personID = Person.counterRegistred
        self.signedUp = False

        # Авторизуемся и получаем service — экземпляр доступа к API
        # Файл, полученный в Google Developer Console
        self.CREDENTIALS_FILE = 'C:/Users/User/djangogirls/blog/creds.json'
        # ID Google Sheets документа (можно взять из его URL)
        self.spreadsheet_id = ''
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        self.httpAuth = self.credentials.authorize(httplib2.Http())
        self.service = apiclient.discovery.build('sheets', 'v4', http = self.httpAuth)
    
    def checkOnBetween(duration,num,start,stop,sex,i):
        if start <= int(num) <= stop:
            Person.statistics[i][sex].append(duration)

    ''' Для машинного обучения
    def appendStat(sex,age,duration):
        start,stop,step = 0,0,10
        sexSTR = ["M","F"]
        for i in range(0,81,10):
            start = i
            stop = start+step
            Person.checkOnBetween(duration,age,start,stop,sexSTR.index(sex),i//10)
    '''

    def isUserExist(user):
        # --------------------------
        # Считывание количество зарегистрировавшихся пользователей
        CREDENTIALS_FILE = 'C:/Users/User/djangogirls/blog/creds.json'
        # ID Google Sheets документа (можно взять из его URL)
        spreadsheet_id = "18ij4fgaNkj2LpLYfN5H2CgTb908avNMYZfy-CU-lcZk"
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

        valuesCount = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range='F1:F1',
            majorDimension='ROWS'
        ).execute()
        Person.counterRegistred = int(valuesCount["values"][0][0])
        # --------------------------

        if Person.counterRegistred < 1:
            return False

        # --------------------------
        # Считывание номеров пользователей
        CREDENTIALS_FILE = 'C:/Users/User/djangogirls/blog/creds.json'
        # ID Google Sheets документа (можно взять из его URL)
        spreadsheet_id = "18ij4fgaNkj2LpLYfN5H2CgTb908avNMYZfy-CU-lcZk"
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
        values = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range='A2:A'+str(Person.counterRegistred+1),
            majorDimension='ROWS'
        ).execute()
        # -------------------------

        for i in range(len(values["values"])):
            if user in values["values"][i]:
                return True
        return False

    def getInfoNumber(number):
        # Считывание количество зарегистрировавшихся пользователей
        # -------------------------
        CREDENTIALS_FILE = 'C:/Users/User/djangogirls/blog/creds.json'
        # ID Google Sheets документа (можно взять из его URL)
        spreadsheet_id = "18ij4fgaNkj2LpLYfN5H2CgTb908avNMYZfy-CU-lcZk"
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

        valuesCount = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range='F1:F1',
            majorDimension='ROWS'
        ).execute()
        # ----------------------------

        # Считывание номеров пользователей
        # ----------------------------
        CREDENTIALS_FILE = 'C:/Users/User/djangogirls/blog/creds.json'
        # ID Google Sheets документа (можно взять из его URL)
        spreadsheet_id = "18ij4fgaNkj2LpLYfN5H2CgTb908avNMYZfy-CU-lcZk"
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
        valuesNum = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range='A2:A' + str(int(valuesCount["values"][0][0])+1),
            majorDimension='COLUMNS'
        ).execute()
        # ----------------------------

        index = 0
        for i in range(len(valuesNum["values"][0])):
            if valuesNum["values"][0][i] == number:
                index = i+1
        if index == 0:
            return False

        # Считывание данных(пол, возраст) пользователей
        # -----------------------------
        Person.counterRegistred = int(valuesCount["values"][0][0])
        CREDENTIALS_FILE = 'C:/Users/User/djangogirls/blog/creds.json'
        # ID Google Sheets документа (можно взять из его URL)
        spreadsheet_id = "18ij4fgaNkj2LpLYfN5H2CgTb908avNMYZfy-CU-lcZk"
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

        values = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range='B'+str(index+1)+":" +"E"+ str(index+1),
            majorDimension='ROWS'
        ).execute()
        # -----------------------------

        return values['values'][0]


    def signUp(self):
        # Считывание количества зарегестрированных пользователей
        # --------------------------
        CREDENTIALS_FILE = 'C:/Users/User/djangogirls/blog/creds.json'
        # ID Google Sheets документа (можно взять из его URL)
        spreadsheet_id = "18ij4fgaNkj2LpLYfN5H2CgTb908avNMYZfy-CU-lcZk"
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

        valuesCount = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range='F1:F1',
            majorDimension='ROWS'
        ).execute()
        # --------------------------

        # Запись данных в таблицу
        # ---------------------------
        self.spreadsheet_id = "18ij4fgaNkj2LpLYfN5H2CgTb908avNMYZfy-CU-lcZk"
        personData = [self.phoneNumber,self.sex,self.ages[0],self.ages[1],self.ages[2]]
        self.personID = Person.counterRegistred+2
        self.writeRows("A-E",personData)# Запись в базу данных в строчку
        self.signedUp = True
        Person.counterRegistred+=1
        # ---------------------------

        print("Signed up",self.personID)

    def calculateDuringTime(sex,age): # "Машинное обучение"
        if sex == "M":
            sex = 0.75
        else:
            sex = 1
        age = int(age)
        age /= 100
        return int(sex*age*30)+10
        
    def visit(self,roomID,visitTime,schedule):
        self.busyIndex = visitTime[1]
        Schedule.busy.append(self.busyIndex)

        self.duration = Person.calculateDuringTime(self.sex,self.age)
        schedule.correctSchedule(visitTime,self.duration)

        # Для машинного обучение
        # Person.appendStat(self.sex,self.age,self.duration)

        hour_min= schedule.getVisitTimeNormal(visitTime[0],visitTime[1])
        hour_min = Schedule.convertFromMinutsToStandart(hour_min[0]*60+hour_min[1])

        visitTime = visitTime[0]+" "+hour_min
        personData = [self.phoneNumber,self.sex,self.age,roomID,str(visitTime),self.duration]
        self.personID = Person.counterVisit+2
        Person.counterVisit += 1

        if self.signedUp == True:
            self.spreadsheet_id = "1ORgm83EGDTKsNwpJzQYMRtPuvJyrRu2dpOW9Cs6RtaU"
            self.writeRows("A-F",personData) # Запись в базу данных в строчку
            print("You are recorded")
        else:
            print("Error. you are not signed up")
            
    ''' Для машинного обучения
    def visitAnalytics(self,roomID,visitTime): 
        self.duration = Person.calculateDuringTime(self.sex,self.age)
        Person.appendStat(self.sex,self.age,self.duration)
        personData = [self.phoneNumber,self.sex,self.age,roomID,str(visitTime),str(self.duration)]
        if self.signedUp == True:
            for i in range(len(personData)):
                Person.lerningData[self.personID-2].append(personData[i])
    '''
        
    def writeRows(self,_range,dataInput):
        # Пример записи в файл в строчку
        # rows = ["A-B"] - example
        # dataInput = ["example1","example2"]

        _range = _range.split("-")
        self.personID = int(self.personID) # Строка в таблице начинается с 2
        rows = _range[0]+str(self.personID)+":"+_range[1]+str(self.personID)
        self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": rows,
                     "majorDimension": "ROWS",
                     "values": [dataInput]},
        	]
            }
        ).execute()
        
    def writeRowsAnalitics(self,_range,dataInput,personID,spreadsheetID):
        # Пример записи в файл в строчку
        # rows = ["A-B"] - example
        # dataInput = ["example1","example2"]
        _range = _range.split("-")
        rows = _range[0]+str(personID)+":"+_range[1]+str(personID)
        self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheetID,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": rows,
                     "majorDimension": "ROWS",
                     "values": [dataInput]},
        	]
            }
        ).execute()
        
    def writeAllData(self,_range,dataInput,spreadSheets):
        # Пример записи в файл матрицей
        # rows = "A1:C6" - example
        # dataInput = [["example1","example2"],["example3","example4"]]
        self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadSheets,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": _range,
                     "majorDimension": "ROWS",
                     "values": dataInput},
        	]
            }
        ).execute()
        
    def calculate_age(born):
        today = datetime.datetime.today()
        try: 
            birthday = born.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = born.replace(year=today.year, month=born.month+1, day=1)
        if birthday > today:
            return str(today.year - born.year - 1)
        else:
            return str(today.year - born.year)
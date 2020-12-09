from Schedule import Schedule
from Person import Person

from pprint import pprint
from .Schedule import Schedule
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import random
import datetime


def writeAllData(_range, dataInput, spreadSheets):
    # Пример записи в файл матрицей
    # rows = "A1:C6" - example
    # dataInput = [["example1","example2"],["example3","example4"]]
    CREDENTIALS_FILE = 'C:/Users/User/djangogirls/blog/creds.json'
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '1Wjpil_De7lmY1w6m5FVxGnVMNZ8V9pXJmW5L0LOi3ns'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": _range,
                 "majorDimension": "ROWS",
                 "values": dataInput},
            ]
        }
    ).execute()

weekDays = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"] # Дни недели
sc = Schedule()
sc.createSchedule()

admin = Person("Admin","M","1","1","1970","0",True)
admin.signUp()

oldGirl = Person("89134829304","F","10","12","1960","1",True)
oldGirl.signUp()
ID = 4
day = weekDays[int(ID/19)]
visitTime1 = [day,ID]
#visitTime = Schedule.convertFromMinutsToStandart(sc.schedule[day][4],4)
oldGirl.visit("109",visitTime1,sc)

man = Person("89134829454","M","20","2","1980","2",True)
man.signUp()
ID = 3
day = weekDays[int(ID/19)]

visitTime2 = [day,ID]
#visitTime = Schedule.convertFromMinutsToStandart(sc.schedule[day][3],3)
man.visit("109",visitTime2,sc)

man1 = Person("89134823214","M","11","3","1987","3",True)
man1.signUp()
ID = 5
day = weekDays[int(ID/19)]

visitTime3 = [day,ID]
#visitTime = Schedule.convertFromMinutsToStandart(sc.schedule[day][5],5)
man1.visit("109",visitTime3,sc)

man2 = Person("89134823222","M","10","3","1950","4",True)
man2.signUp()
ID = 10
day = weekDays[int(ID/19)]

visitTime4 = [day,ID]
#visitTime = Schedule.convertFromMinutsToStandart(sc.schedule[day][5],5)
man.visit("109",visitTime4,sc)
time4 = sc.getVisitTimeNormal(visitTime4[0],visitTime4[1])

#print(sc.getFreeTime()[0])
sc.patientLeft(oldGirl)
#print(sc.getFreeTime()[0])
from django.shortcuts import render
from .forms import UserForm,signUp,RoomChange,SignIn
from .Person import Person
from .Schedule import Schedule

person = Person()
schedule = Schedule()
#schedule.createSchedule(12)

def index(request):
  global person
  submitbutton= request.POST.get("submit")
  regBut = request.POST.get("reg")
  sig = request.POST.get("in")
  signed = request.POST.get("signed")
  offer = request.POST.get("offer")
  number=''
  sex=''
  day=''
  month=''
  year=''
  room=''
  signup=''
  roomChange=''
  numberIn=''
  checkOnSignIn = False


  form= UserForm(request.POST or None)
  signIn = SignIn(request.POST or None)
  if form.is_valid() and submitbutton == "Submit":
        number = form.cleaned_data.get("number")
        sex = form.cleaned_data.get("sex")
        day= form.cleaned_data.get("day")
        month= form.cleaned_data.get("month")
        year= form.cleaned_data.get("year")
        person.addData(number,sex,day,month,year)
        person.signUp()
  if signIn.is_valid ():
    numberIn = signIn.cleaned_data.get("number")
    if Person.isUserExist(numberIn):
        infos = Person.getInfoNumber(numberIn)
        if infos != False:
            checkOnSignIn = not checkOnSignIn
            person.addData(numberIn, infos[0], infos[1], infos[2], infos[3])
            person.signedUp = True
    signIn=''
  signup = signUp(request.POST or None)
  f = open("out.txt",'a')
  f.write(number + ' ' +' ' + '\n')
  f.close()
  roomChange = RoomChange(request.POST or None)
  submitbutton2 = request.POST.get("secsubmit")

  if signup.is_valid() and offer == "Оставить заявку":
    time = signup.cleaned_data.get("signup")
    day = Person.weekDays[int(int(time) / 19)]
    person.visit("109",[day,int(time)],schedule)
    schedule.setBusy(int(time))
  
  context= {'form': form, 'number': number, 'checkOnSignIn':checkOnSignIn,'person':person,'schedule': schedule,
            'sex':sex, 'submitbutton': submitbutton, 'submitbutton2': submitbutton2, 'regBut': regBut, 'sig': sig, 'signed':signed,
            'day':day,'month':month,'year':year,'room':room,'signUp':signup,'roomChange':roomChange, 'signIn':signIn,'offer':offer}

  return render(request, 'blog/post_list.html', context)


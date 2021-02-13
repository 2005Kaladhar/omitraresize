from ui_regularPage import Ui_MainWindow as Ui_RegularWindow
from ui_circularProgressBarSplashScreen import Ui_MainWindow
from ui_mainWindow import Ui_MainPage as Ui_AfterLogin
from ui_LoginForm import Ui_MainWindow as Ui_Login
import sys
import webbrowser

from PySide2 import QtCore
from PySide2.QtWidgets import *
import time
from tinydb import Query, TinyDB

from webAutomater import main_runner
import pyttsx3
from plyer import notification

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',190)
engine.setProperty('volume',1.0)

ChangeEmailAndPassword = False

def audio(text):
    engine.say(text)
    engine.runAndWait()

def notify(title, message, timeout=3, app_icon="icon.ico"):
    notification.notify(title=title,message=message,timeout=timeout,app_icon=app_icon)

db = TinyDB("SubjectAndDays.db")
timesdb = TinyDB('SubjectsAndTimes.db')
linkdicdb = TinyDB('Linkdic.db')
sublistdb = TinyDB('sublist.db')
personaldetailsdb = TinyDB('personaldetails.db')
User = Query()

# if db.all() == []:
#     OpenLoginScreen = True
# else:
#     OpenLoginScreen = False

# ------------------------------------------------------------------------------
print("In DB.ALL",db.all())
count = 0


def clearall():
    db.truncate()
    timesdb.truncate()
    linkdicdb.truncate()
    sublistdb.truncate()
    personaldetailsdb.truncate()

def dbinsert(key,value):
    db.insert({key:value})

def dbclear(db):
    db.truncate()

# --------------------------------------------------------------------------

# if db.all() == []:
#     OpenLoginScreen = True
# else:
#     OpenLoginScreen = False

if personaldetailsdb.all() == []:
    OpenLoginScreen = True
else:
    OpenLoginScreen = False

# ------------------------------------------------------------------------------

count = 0


class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ChangeEmailAndPass = globals()['ChangeEmailAndPassword']
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.Maximizebtn.clicked.connect(self.maxi)
        self.ui.Minimizebtn.clicked.connect(self.mini)

        self.main = Afterlogin()
        if self.ChangeEmailAndPass == True:
            self.ui.NextButton.setText("Save")
            self.personaldetails = personaldetailsdb.all()
            self.ui.Name.setText(str( list(self.personaldetails[0].values()) [0] ) )
            self.ui.Email.setText(str( list(self.personaldetails[1].values()) [0] ) )
            self.ui.Password.setText(str( list(self.personaldetails[2].values()) [0] ) )
            if str(list(self.personaldetails[3].values())[0] )  == 'sir':
                self.ui.MaleRadioBtn.setChecked(True)
            else:
                self.ui.FemaleRadioBtn.setChecked(True)


        self.ui.stackedWidget.setCurrentWidget(self.ui.UsusalTitle)
        self.ui.NextButton.clicked.connect(self.nextStep)
        self.ui.CloseButton.clicked.connect(self.closebtn)
        self.email = self.ui.Email.text()
        self.name = self.ui.Name.text()
        self.password = self.ui.Password.text()



    def closebtn(self):
        self.close()
        sys.exit()

    def maxi(self):
        if self.isMaximized():
            self.resize(700, 530)
        else:
            self.showMaximized()

    def mini(self):
        self.showMinimized()

    def closeAlert(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.UsusalTitle)


    def nextStep(self):
        print('Name',self.ui.Name.text().isalnum())
        print('Email',self.ui.Email.text().endswith('@gmail.com',-10))
        print('Password',self.ui.Password.text().lstrip().rstrip()!= '')
        print('Gender',(self.ui.MaleRadioBtn.isChecked() or self.ui.FemaleRadioBtn.isChecked() ) )
        self.emailCheck = self.ui.Email.text().endswith('@gmail.com',-10)
        print("emailCheck",self.emailCheck)
        # if self.ui.Email.text().endswith('@gmail.com',-10) == True:
        #     self.emailCheck = True
        # else:
        #     False https://meet.google.com/mhi-vnrs-phz

        if globals()['ChangeEmailAndPassword'] == True:
            if self.ui.Name.text().lstrip().rstrip() != "" and self.ui.Email.text().endswith('@gmail.com',
                                                                                             -10) and self.ui.Password.text().lstrip().rstrip() != '' and (
                    self.ui.MaleRadioBtn.isChecked() or self.ui.FemaleRadioBtn.isChecked()):
                self.close()
                male = self.ui.MaleRadioBtn.isChecked()
                self.gender = None
                female = self.ui.FemaleRadioBtn.isChecked()
                if male == True:
                    self.gender = 'sir'
                elif female == True:
                    self.gender = "ma'am"

                print('Male', male)
                personaldetailsdb.truncate()
                personaldetailsdb.insert({"Name": self.ui.Name.text()})
                personaldetailsdb.insert({"Email": self.ui.Email.text()})
                personaldetailsdb.insert({"Password": self.ui.Password.text()})
                personaldetailsdb.insert({"Gender": self.gender})
                print(personaldetailsdb.all())

                print("Saved Data is ", personaldetailsdb.all())
                self.main = Ui_regularWidow()
                self.close()
                self.main.show()
            else:
                self.ui.stackedWidget.setCurrentWidget(self.ui.EmailError)
                self.ui.NotFilledClose.clicked.connect(self.closeAlert)

        else:
            if self.ui.Name.text().lstrip().rstrip()!="" and self.ui.Email.text().endswith('@gmail.com',-10) and self.ui.Password.text().lstrip().rstrip()!= '' and (self.ui.MaleRadioBtn.isChecked() or self.ui.FemaleRadioBtn.isChecked()):
                self.close()
                male = self.ui.MaleRadioBtn.isChecked()
                self.gender = None
                female = self.ui.FemaleRadioBtn.isChecked()
                if male == True:
                    self.gender = 'sir'
                elif female == True:
                    self.gender = "ma'am"

                print('Male', male)
                personaldetailsdb.truncate()
                personaldetailsdb.insert({"Name": self.ui.Name.text()})
                personaldetailsdb.insert({"Email": self.ui.Email.text()})
                personaldetailsdb.insert({"Password": self.ui.Password.text()})
                personaldetailsdb.insert({"Gender": self.gender})
                print(personaldetailsdb.all())
                self.main.show()
            else:
                self.ui.stackedWidget.setCurrentWidget(self.ui.EmailError)
                self.ui.NotFilledClose.clicked.connect(self.closeAlert)


class Ui_regularWidow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_RegularWindow()
        self.ui.setupUi(self)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.ui.stackedWidget.setCurrentWidget(self.ui.MainContent1Stacked)

        self.current_time = str(time.asctime(time.localtime()))
        self.current_time = self.current_time.split(" ")
        self.currenttime = self.current_time[3].split(":")
        if int(self.currenttime[0])>12:
            self.currenttime[0] = str(int(self.currenttime[0])-12)

        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.CloseButton.clicked.connect(self.closer)

        self.ui.Maximizebtn.clicked.connect(self.maxi)
        self.ui.Minimizebtn.clicked.connect(self.mini)

        self.ui.StartButtonMain.clicked.connect(self.startprocess)
        self.ui.StartButtonsecond.clicked.connect(self.startprocess)
        self.ui.UrgentMeetingStartBtn.clicked.connect(self.urgentMeetingStart)

        self.ui.ContactDeveloper.clicked.connect(self.urlopen)
        self.ui.ClearSavedData.clicked.connect(self.deleteAllData)
        self.ui.ChangeEmailPass.clicked.connect(self.changeEmailAndPassword)

        print(personaldetailsdb.all())
        if personaldetailsdb.all() != []:
            self.name = personaldetailsdb.all()[0]["Name"]
            self.email = personaldetailsdb.all()[1]["Email"]
            self.password = personaldetailsdb.all()[2]["Password"]
            self.gender = personaldetailsdb.all()[3]["Gender"]

            print("from UI regular window")
            print(self.name)
            print(self.email)
            print(self.password)
            print(self.gender)
            print("---------------------------------------")

    def closefunc(self):
        self.close()

    def maxi(self):
        if self.isMaximized():
            self.resize(700, 530)
        else:
            self.showMaximized()

    def mini(self):
        self.showMinimized()

    def deleteAllData(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.DeleteMessagePage)
        self.ui.YesDelete.clicked.connect(self.yesDelete)
        self.ui.NoDelete.clicked.connect(self.noDelete)

    def noDelete(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.MainContent1Stacked)

    def yesDelete(self):
        clearall()
        self.ui.DeleteMessage.setText("All The Saved Data Has Been Cleared..."
                                      "Restart the App.")
        self.ui.YesDelete.hide()
        self.ui.NoDelete.hide()

    def changeEmailAndPassword(self):
        globals() ['ChangeEmailAndPassword'] = True
        self.close()
        self.main = Login()
        self.main.show()


    def closer(self):
        self.close()

    def urlopen(self):
        self.url = 'https://kaladhargopal.wixsite.com/home'
        webbrowser.open(self.url)

# ------------------------------------------Creating Class Runner Program---------------------------------------------

    def class_finder(self,timew,linkdic,sublist):
        link_dic = linkdic
        sub_lst = sublist
        times = timew

        now = str(time.asctime(time.localtime()))
        separator = now.split(' ')
        Day = separator[0]
        Month = separator[2]
        Date = separator[2]
        Time = str(separator[3]).split(':')  # s
        Hour, Minute = Time[0], Time[1]
# --------------------------------------------------------------------------------------------------
        def list_sorter(list):
            ret_lst = []

            for i in range(len(list)):
                ret_lst.append(min(list))
                del list[list.index(min(list))]
            return ret_lst

        def class_time_wise_sorter():
            ret_list = {}
            for i in day_sub_lst:
                ret_list.update({i: float(times[i][0])})

            sorted_list = list_sorter(list(ret_list.values()))
            return_list = []
            for i in sorted_list:
                return_list.append(__get_key__(ret_list, i))
            return return_list

        def __get_key__(dic, value):
            for i in dic.keys():
                if dic[i] == value:
                    return i

        def time_adder(Time, min_to_add):
            Time = str(Time).split('.')
            hour, minute = int(Time[0]), int(Time[1])
            min_to_add = int(min_to_add)
            if min_to_add + minute > 60:
                hour += 1
                minute += min_to_add - 60
                return float(f'{hour}.{minute}')
            else:
                minute += min_to_add
                return float(f'{hour}.{minute}')

        def none_clear(iter):
            count = 0
            for i in iter:
                if i == None:
                    del iter[count]
                count += 1
            if iter.count(None) != 0:
                return none_clear(iter)
            else:
                return iter

        def collector(x):
            for i in x.keys():
                if Day in x[i]:
                    return i

        day_sub_lst = list(map(collector,sub_lst))
        print("before time wise",day_sub_lst)
        day_sub_lst = class_time_wise_sorter()
        print('After time wise ',day_sub_lst)

        if day_sub_lst == []:
            audio("Your don't have any meeting today; Just relax")
            notify(title="You Don't have any meeting today", message="No meetings Today...")


        def linkreturner(nameofclassToreturnLink):
            return link_dic[nameofclassToreturnLink]

        def nextclassfinder(nameofclass):
            index = day_sub_lst.index(nameofclass)
            if day_sub_lst[index] == day_sub_lst[-1]:
                audio(f"This was your Last Class ")
                return None
            else:
                return day_sub_lst[index+1]


        for i in day_sub_lst:
            current_time = f"{Hour}.{Minute}"
            current_time = float(current_time)

            lastimeforclass = float(times[day_sub_lst[-1]][1])
            print(f"last time for the class {float(times[day_sub_lst[-1]][1])}")
# ------------------------------All The Classes Over event--------------------------------------------------
            if current_time>lastimeforclass:
                notify(app_icon=None, title="All the Classes are over now ...",
                       message="Classes Over...", timeout=4)
                audio("All the classes are over now ")
                print(day_sub_lst)
                audio(f", Today You had {day_sub_lst[0:len(day_sub_lst) - 1]} and the last class ;{day_sub_lst[-1]};"
                      f"from {(times[day_sub_lst[-1]][0]).split('.')[0]} {(times[day_sub_lst[-1]][0]).split('.')[1]} to  "
                      f"{(times[day_sub_lst[-1]][1]).split('.')[0]} {(times[day_sub_lst[-1]][1]).split('.')[1]}. Have a good day")

                break

            if float(times[str(i)][0]) <= current_time and current_time < float(times[str(i)][1]):
                print("start time = ", float(times[str(i)][0]))
                print("end time   =", float(times[str(i)][1]))
                notify(title=f"It is your {i} class {self.name} ...", message="Attend your class now", timeout=5)
                audio(f"At your service  ;It is your {i} class. Attend your class now. "
                      f"I'm setting up everything for you, wait for sometime")
                print(i)
                print(day_sub_lst)
                print(f"Now you have {i} class....")
                print("CLass link : ",linkreturner(i))
                class_link = linkreturner(i)
                self.showMinimized()
                a = main_runner(class_link,self.email,self.password,name=self.name,gender=self.gender)
                if a == 'cancel':
                    self.showMaximized()
                    self.resize(700,530)


            elif float(times[str(i)][0]) >= current_time and current_time < float(times[str(i)][1]):
                audio(f"{i} class has not started yet , waiting for it to start. It will start at "
                      f"{(times[i][0]).split('.')[0]} {(times[i][0]).split('.')[1]} ")

                if day_sub_lst.index(i) !=0:
                    print(f";The last class you had, was, {day_sub_lst[day_sub_lst.index(str(i)) - 1]}")


    def urgentMeetingStart(self):
        urgentLink = str(self.ui.UrgentMeeting.text())
        self.ui.UrgentMeeting.setText("")
        print('urgentlink',urgentLink)
        print("PartCheck",urgentLink[0:24])
        urgentLink = urgentLink[0:24]              #'https://meet.google.com/'

        if urgentLink[0:24] == 'https://meet.google.com/':
            link_check = True
        else:
            link_check = False

        print("linkcheck",link_check)

        if link_check == True:
            self.showMinimized()
            a = main_runner(self.ui.UrgentMeeting.text(),self.email,self.password,name=self.name,gender=self.gender)
            if a == 'cancel':
                self.showMaximized()
                self.resize(700,530)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.InvalidLinkPage)
            self.ui.UrgentLinkClose.clicked.connect(self.closeLinkAlert)

    def closeLinkAlert(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.MainContent1Stacked)

    def startprocess(self):
        self.rawtimes = timesdb.all()
        self.times = {}
        for items in self.rawtimes:
            for name, timing in items.items():
                self.times[name] = timing

        self.sub_lst = db.all()

        self.rawlinkdic = linkdicdb.all()
        self.linkdic = {}
        for items in self.rawlinkdic:
            for name, link in items.items():
                self.linkdic[name] = link

        print('linkdicfromdb',self.linkdic)
        print('timesfromdb',self.times)
        print('sublstfromdb',self.sub_lst)
        times = self.times
        linkdic = self.linkdic
        sublst = self.sub_lst

        self.now_class = self.class_finder(times,linkdic,sublst)



class Afterlogin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_AfterLogin()
        self.ui.setupUi(self)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.CloseButton.clicked.connect(self.closer)
        self.ui.NextButton.clicked.connect(self.nextStep)

        self.ui.Maximizebtn.clicked.connect(self.maxi)
        self.ui.Minimizebtn.clicked.connect(self.mini)

        print("personaldb", personaldetailsdb.all())
        if personaldetailsdb.all() != []:
            self.name = personaldetailsdb.all()[0]["Name"]
            self.email = personaldetailsdb.all()[1]["Email"]
            self.password = personaldetailsdb.all()[2]["Password"]
            self.gender = personaldetailsdb.all()[3]["Gender"]

            print("from After Login")
            print(self.name)
            print(self.email)
            print(self.password)
            print(self.gender)
            print("---------------------------------------")

        # --------------------------------------------------------------------------------------------
        # Defining functions and logic to show days frame when days button for each corresponding subject is clicked
        self.Subject1Days = [self.ui.Subject1Sunday,
                             self.ui.Subject1Monday,
                             self.ui.Subject1Tuesday,
                             self.ui.Subject1Wednesday,
                             self.ui.Subject1Thursday,
                             self.ui.Subject1Friday,
                             self.ui.Subject1Saturday]

        self.Subject2Days = [self.ui.Subject2Sunday,
                             self.ui.Subject2Monday,
                             self.ui.Subject2Tuesday,
                             self.ui.Subject2Wednesday,
                             self.ui.Subject2Thursday,
                             self.ui.Subject2Friday,
                             self.ui.Subject2Saturday]

        self.Subject3Days = [self.ui.Subject3Sunday,
                             self.ui.Subject3Monday,
                             self.ui.Subject3Tuesday,
                             self.ui.Subject3Wednesday,
                             self.ui.Subject3Thursday,
                             self.ui.Subject3Friday,
                             self.ui.Subject3Saturday]

        self.Subject4Days = [self.ui.Subject4Sunday,
                             self.ui.Subject4Monday,
                             self.ui.Subject4Tuesday,
                             self.ui.Subject4Wednesday,
                             self.ui.Subject4Thursday,
                             self.ui.Subject4Friday,
                             self.ui.Subject4Saturday]

        self.Subject5Days = [self.ui.Subject5Sunday,
                             self.ui.Subject5Monday,
                             self.ui.Subjcet5Tuesday,
                             self.ui.Subject5Wednesday,
                             self.ui.Subject2Thursday,
                             self.ui.Subject2Friday,
                             self.ui.Subject2Saturday]

        self.Subject6Days = [self.ui.Subject6Sunday,
                             self.ui.Subject6Monday,
                             self.ui.Subject6Tuesday,
                             self.ui.Subject6Wednesday,
                             self.ui.Subject6Thursday,
                             self.ui.Subject6Friday,
                             self.ui.Subject6Saturday]

        self.Subject7Days = [self.ui.Subject7Sunday,
                             self.ui.Subject7Monday,
                             self.ui.Subject7Tuesday,
                             self.ui.Subject7Wednesday,
                             self.ui.Subject7Thursday,
                             self.ui.Subject7Friday,
                             self.ui.Subject7Saturday]

        self.Subject8Days = [self.ui.Subject8Sunday,
                             self.ui.Subject8Monday,
                             self.ui.Subject8Tuesday,
                             self.ui.Subject8Wednesday,
                             self.ui.Subject8Thursday,
                             self.ui.Subject8Friday,
                             self.ui.Subject8Saturday]

        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------------------------------------------

        self.subjectdayslist = [self.ui.SubjectDays,
                                self.ui.SubjectDays_2,
                                self.ui.SubjectDays_3,
                                self.ui.SubjectDays_4,
                                self.ui.SubjectDays_5,
                                self.ui.SubjectDays_6,
                                self.ui.SubjectDays_7,
                                self.ui.SubjectDays_8]

        self.DaysButtons = [self.ui.SubjectsDaysBtn,
                            self.ui.SubjectsDaysBtn_2,
                            self.ui.SubjectsDaysBtn_3,
                            self.ui.SubjectsDaysBtn_4,
                            self.ui.SubjectsDaysBtn_5,
                            self.ui.SubjectsDaysBtn_6,
                            self.ui.SubjectsDaysBtn_7,
                            self.ui.SubjectsDaysBtn_8]

        self.daysAndsubjectRelation = {self.ui.SubjectsDaysBtn: self.ui.SubjectDays,
                                       self.ui.SubjectsDaysBtn_2: self.ui.SubjectDays_2,
                                       self.ui.SubjectsDaysBtn_3: self.ui.SubjectDays_3,
                                       self.ui.SubjectsDaysBtn_4: self.ui.SubjectDays_4,
                                       self.ui.SubjectsDaysBtn_5: self.ui.SubjectDays_5,
                                       self.ui.SubjectsDaysBtn_6: self.ui.SubjectDays_6,
                                       self.ui.SubjectsDaysBtn_7: self.ui.SubjectDays_7,
                                       self.ui.SubjectsDaysBtn_8: self.ui.SubjectDays_8}

        
        self.ui.Subject1DaysHeading.setText(self.ui.Subject_1.text())
        self.ui.Subject2DaysHeading.setText(self.ui.Subject_2.text())
        self.ui.Subject3DaysHeading.setText(self.ui.Subject_3.text())
        self.ui.Subject4DaysHeading.setText(self.ui.Subject_4.text())
        self.ui.Subject5DaysHeading.setText(self.ui.Subject_5.text())
        self.ui.Subject6DaysHeading.setText(self.ui.Subject_6.text())
        self.ui.Subject7DaysHeading.setText(self.ui.Subject_7.text())
        self.ui.Subject8DaysHeading.setText(self.ui.Subject_8.text())

        self.ui.GoBackButton.clicked.connect(self.previousButtonClicked)
        self.ui.SubjectsDaysBtn.clicked.connect(self.btn1)
        self.ui.SubjectsDaysBtn_2.clicked.connect(self.btn2)
        self.ui.SubjectsDaysBtn_3.clicked.connect(self.btn3)
        self.ui.SubjectsDaysBtn_4.clicked.connect(self.btn4)
        self.ui.SubjectsDaysBtn_5.clicked.connect(self.btn5)
        self.ui.SubjectsDaysBtn_6.clicked.connect(self.btn6)
        self.ui.SubjectsDaysBtn_7.clicked.connect(self.btn7)
        self.ui.SubjectsDaysBtn_8.clicked.connect(self.btn8)

    def viewchng(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Day1)

    def closefunc(self):
        self.close()

    def maxi(self):
        if self.isMaximized():
            self.resize(700,530)
        else:self.showMaximized()

    def mini(self):
        self.showMinimized()

    def insertSubjectandTime(self, subject, timefrm, timeto):
        dbinsert(subject, (str(timefrm), str(timeto)))

    def btn1(self):
        print("pressed the 1st button")
        self.ui.stackedWidget.setCurrentWidget(self.ui.Day1)

        if self.ui.Subject1DaysHeading.text().rstrip().lstrip() == "":
            self.ui.Subject1DaysHeading.setText("Day1")

        else:
            self.ui.Subject1DaysHeading.setText(self.ui.Subject_1.text())

    def btn2(self):
        print("pressed the 2 button")
        self.ui.stackedWidget.setCurrentWidget(self.ui.Day2)
        if self.ui.Subject2DaysHeading.text() == "":
            self.ui.Subject2DaysHeading.setText("Day2")

        else:
            self.ui.Subject2DaysHeading.setText(self.ui.Subject_2.text())

    def btn3(self):
        print("pressed the 3 button")
        self.ui.stackedWidget.setCurrentWidget(self.ui.Day3)
        if self.ui.Subject3DaysHeading.text() == "":
            self.ui.Subject3DaysHeading.setText("Day3")

        else:
            self.ui.Subject3DaysHeading.setText(self.ui.Subject_3.text())

    def btn4(self):
        print("pressed the 4 button")
        self.ui.stackedWidget.setCurrentWidget(self.ui.Day4)
        if self.ui.Subject4DaysHeading.text() == "":
            self.ui.Subject4DaysHeading.setText("Day4")

        else:
            self.ui.Subject4DaysHeading.setText(self.ui.Subject_4.text())

    def btn5(self):
        print("pressed the 5 button")
        self.ui.stackedWidget.setCurrentWidget(self.ui.Day5)
        if self.ui.Subject5DaysHeading.text() == "":
            self.ui.Subject5DaysHeading.setText("Day5")

        else:
            self.ui.Subject5DaysHeading.setText(self.ui.Subject_5.text())

    def btn6(self):
        print("pressed the 6 button")
        self.ui.stackedWidget.setCurrentWidget(self.ui.Day6)
        if self.ui.Subject6DaysHeading.text() == "":
            self.ui.Subject6DaysHeading.setText("Day6")

        else:
            self.ui.Subject6DaysHeading.setText(self.ui.Subject_6.text())

    def btn7(self):
        print("pressed the 7 button")
        self.ui.stackedWidget.setCurrentWidget(self.ui.Day7)
        if self.ui.Subject7DaysHeading.text() == "":
            self.ui.Subject7DaysHeading.setText("Day7")

        else:
            self.ui.Subject7DaysHeading.setText(self.ui.Subject_7.text())

    def btn8(self):
        print("pressed the 8 button")
        self.ui.stackedWidget.setCurrentWidget(self.ui.Day8)
        if self.ui.Subject8DaysHeading.text() == "":
            self.ui.Subject8DaysHeading.setText("Day8")

        else:
            self.ui.Subject8DaysHeading.setText(self.ui.Subject_8.text())

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------

    def nextStep(self):
        # clearall() #-----VVVIMP Line------------------------------------
        # -----------------------Getting Days for Subject1 in the form of a list---------------------------------------------------------------------------------------------------------
        if str(self.ui.Subject_1.text()).rstrip().lstrip() != '':
            self.Subject1Days = {str(self.ui.Subject_1.text()): list(map(self.dayreturn, self.Subject1Days))}
            self.Subject1Days = list(filter(lambda x: x != False, self.Subject1Days[str(self.ui.Subject_1.text())]))
            self.Subject1Days = list(filter(lambda x: x != None, self.Subject1Days))
            print(self.ui.Subject_1.text(), "=", self.Subject1Days)

            # --------------------------- Getting Times From and To ------------------------------------------------------------
            self.Subject1From = self.ui.Subject_1From.time().toString()
            self.Subject1To = self.ui.Subject_1To.time().toString()
            print("from", self.Subject1From, "to", self.Subject1To)
        else:
            self.Subject1Days = None

        # ----------------------Getting Days for Subject2 in the form of a list-------------------------------------------------------------------------------------------------------------
        if str(self.ui.Subject_2.text()).rstrip().lstrip() != '':
            self.Subject2Days = {str(self.ui.Subject_2.text()): list(map(self.dayreturn, self.Subject2Days))}
            self.Subject2Days = list(filter(lambda x: x != False, self.Subject2Days[str(self.ui.Subject_2.text())]))
            self.Subject2Days = list(filter(lambda x: x != None, self.Subject2Days))
            print(self.ui.Subject_2.text(), "=", self.Subject2Days)
            # ---------------------------Getting Times From and To------------------------------------------------------------
            self.Subject2From = self.ui.Subject_2From.time().toString()
            self.Subject2To = self.ui.Subject_2To.time().toString()
            print("from", self.Subject2From, "to", self.Subject2To)
        else:
            self.Subject2Days = None

        # -----------------------Getting Days for Subject3 in the form of a list---------------------------------------------------------------------------------------------------------
        if str(self.ui.Subject_3.text()).rstrip().lstrip() != '':
            self.Subject3Days = {str(self.ui.Subject_3.text()): list(map(self.dayreturn, self.Subject3Days))}
            self.Subject3Days = list(filter(lambda x: x != False, self.Subject3Days[str(self.ui.Subject_3.text())]))
            self.Subject3Days = list(filter(lambda x: x != None, self.Subject3Days))
            print(self.ui.Subject_3.text(), "=", self.Subject3Days)
            # ---------------------------Getting Times From and To------------------------------------------------------------
            self.Subject3From = self.ui.Subject_3From.time().toString()
            self.Subject3To = self.ui.Subject_3To.time().toString()
            print("from", self.Subject3From, "to", self.Subject3To)
        else:
            self.Subject3Days = None
        # -----------------------------------------------------------------------------------------------------------------------------------
        # -----------------------Getting Days for Subject4 in the form of a list---------------------------------------------------------------------------------------------------------
        if str(self.ui.Subject_4.text()).rstrip().lstrip() != '':
            self.Subject4Days = {str(self.ui.Subject_4.text()): list(map(self.dayreturn, self.Subject4Days))}
            self.Subject4Days = list(filter(lambda x: x != False, self.Subject4Days[str(self.ui.Subject_4.text())]))
            self.Subject4Days = list(filter(lambda x: x != None, self.Subject4Days))
            print(self.ui.Subject_4.text(), "=", self.Subject4Days)
            # ---------------------------Getting Times From and To------------------------------------------------------------
            self.Subject4From = self.ui.Subject_4From.time().toString()
            self.Subject4To = self.ui.Subject_4To.time().toString()
            print("from", self.Subject4From, "to", self.Subject4To)
        else:
            self.Subject4Days = None
        # -----------------------------------------------------------------------------------------------------------------------------------
        # -----------------------Getting Days for Subject5 in the form of a list---------------------------------------------------------------------------------------------------------
        if str(self.ui.Subject_5.text()).rstrip().lstrip() != '':
            self.Subject5Days = {str(self.ui.Subject_5.text()): list(map(self.dayreturn, self.Subject5Days))}
            self.Subject5Days = list(filter(lambda x: x != False, self.Subject5Days[str(self.ui.Subject_5.text())]))
            self.Subject5Days = list(filter(lambda x: x != None, self.Subject5Days))
            print(self.ui.Subject_5.text(), "=", self.Subject5Days)
            # ---------------------------Getting Times From and To------------------------------------------------------------
            self.Subject5From = self.ui.Subject_5From.time().toString()
            self.Subject5To = self.ui.Subject_5To.time().toString()
            print("from", self.Subject5From, "to", self.Subject5To)
        else:
            self.Subject5Days = None
        # -----------------------------------------------------------------------------------------------------------------------------------
        # -----------------------Getting Days for Subject6 in the form of a list---------------------------------------------------------------------------------------------------------
        if str(self.ui.Subject_6.text()).rstrip().lstrip() != '':
            self.Subject6Days = {str(self.ui.Subject_6.text()): list(map(self.dayreturn, self.Subject6Days))}
            self.Subject6Days = list(filter(lambda x: x != False, self.Subject6Days[str(self.ui.Subject_6.text())]))
            self.Subject6Days = list(filter(lambda x: x != None, self.Subject6Days))
            print(self.ui.Subject_6.text(), "=", self.Subject6Days)
            # ---------------------------Getting Times From and To------------------------------------------------------------
            self.Subject6From = self.ui.Subject_6From.time().toString()
            self.Subject6To = self.ui.Subject_6To.time().toString()
            print("from", self.Subject6From, "to", self.Subject6To)
        else:
            self.Subject6Days = None
        # -----------------------------------------------------------------------------------------------------------------------------------
        # -----------------------Getting Days for Subject7 in the form of a list---------------------------------------------------------------------------------------------------------
        if str(self.ui.Subject_7.text()).rstrip().lstrip() != '':
            self.Subject7Days = {str(self.ui.Subject_7.text()): list(map(self.dayreturn, self.Subject7Days))}
            self.Subject7Days = list(filter(lambda x: x != False, self.Subject7Days[str(self.ui.Subject_7.text())]))
            self.Subject7Days = list(filter(lambda x: x != None, self.Subject7Days))
            print(self.ui.Subject_7.text(), "=", self.Subject7Days)
            # ---------------------------Getting Times From and To------------------------------------------------------------
            self.Subject7From = self.ui.Subject_7From.time().toString()
            self.Subject7To = self.ui.Subject_7To.time().toString()
            print("from", self.Subject7From, "to", self.Subject7To)
        else:
            self.Subject7Days = None
        # -----------------------------------------------------------------------------------------------------------------------------------

        # -----------------------Getting Days for Subject8 in the form of a list---------------------------------------------------------------------------------------------------------
        if str(self.ui.Subject_8.text()).rstrip().lstrip() != '':
            self.Subject8Days = {str(self.ui.Subject_8.text()): list(map(self.dayreturn, self.Subject8Days))}
            self.Subject8Days = list(filter(lambda x: x != False, self.Subject8Days[str(self.ui.Subject_8.text())]))
            self.Subject8Days = list(filter(lambda x: x != None, self.Subject8Days))
            print(self.ui.Subject_8.text(), "=", self.Subject8Days)
            # ---------------------------Getting Times From and To------------------------------------------------------------
            self.Subject8From = self.ui.Subject_8From.time().toString()
            self.Subject8To = self.ui.Subject_8To.time().toString()
            print("from", self.Subject8From, "to", self.Subject8To)
        else:
            self.Subject8Days = None
        # -----------------------------------Making licdic------------------------------------------------------------------------------------------------
        self.linkdic = {self.ui.Subject_1.text(): self.ui.Subject_Link_1.text(),
                        self.ui.Subject_2.text(): self.ui.Subject_Link_2.text(),
                        self.ui.Subject_3.text(): self.ui.Subject_Link_3.text(),
                        self.ui.Subject_4.text(): self.ui.Subject_Link_4.text(),
                        self.ui.Subject_5.text(): self.ui.Subject_Link_5.text(),
                        self.ui.Subject_6.text(): self.ui.Subject_Link_6.text(),
                        self.ui.Subject_7.text(): self.ui.Subject_Link_7.text(),
                        self.ui.Subject_8.text(): self.ui.Subject_Link_8.text()}

        # ------------------------------------Removing Subjects with No Subject Name----------------------------------------------------------
        self.rawDaysAndSubjectList = [(self.Subject1Days, self.ui.Subject_1.text()),
                                      (self.Subject2Days, self.ui.Subject_2.text()),
                                      (self.Subject3Days, self.ui.Subject_3.text()),
                                      (self.Subject4Days, self.ui.Subject_4.text()),
                                      (self.Subject5Days, self.ui.Subject_5.text()),
                                      (self.Subject6Days, self.ui.Subject_6.text()),
                                      (self.Subject7Days, self.ui.Subject_7.text()),
                                      (self.Subject8Days, self.ui.Subject_8.text())]

        self.finalDaysAndSubjectList = []  # Final list with subjects which have days and Names
        for days, nameofsubject in self.rawDaysAndSubjectList:
            if days != None:
                self.finalDaysAndSubjectList.append((nameofsubject, days))
            else:
                continue
        # ------------------------------Subject list Subject And Days Dictionary------------------------------------------------------------------------------------------------------------------
        for x, y in self.finalDaysAndSubjectList:
            if x == []:
                del self.finalDaysAndSubjectList[self.finalDaysAndSubjectList.index((x, y))]
        self.DaysAndSubjectDictionary = {}

        for name_of_sbjt, days_of_sjbt in self.finalDaysAndSubjectList:
            self.DaysAndSubjectDictionary[name_of_sbjt] = days_of_sjbt

        print("finalDaysAndSubjectList", self.finalDaysAndSubjectList)
        print("finalDaysAndSubjectDictionary", self.DaysAndSubjectDictionary)
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------

        # -----------------------------------------Subject and Times Dictiondary----------------------------------------------------------------------------------------
        self.rawSubjectsAndTimes = {self.ui.Subject_1.text(): (
        f'{self.ui.Subject_1From.time().toString().split(":")[0]}.{self.ui.Subject_1From.time().toString().split(":")[1]}',
        f'{self.ui.Subject_1To.time().toString().split(":")[0]}.{self.ui.Subject_1To.time().toString().split(":")[1]}'),
                                    self.ui.Subject_2.text(): (
                                    f'{self.ui.Subject_2From.time().toString().split(":")[0]}.{self.ui.Subject_2From.time().toString().split(":")[1]}',
                                    f'{self.ui.Subject_2To.time().toString().split(":")[0]}.{self.ui.Subject_2To.time().toString().split(":")[1]}'),
                                    self.ui.Subject_3.text(): (
                                    f'{self.ui.Subject_3From.time().toString().split(":")[0]}.{self.ui.Subject_3From.time().toString().split(":")[1]}',
                                    f'{self.ui.Subject_3To.time().toString().split(":")[0]}.{self.ui.Subject_3To.time().toString().split(":")[1]}'),
                                    self.ui.Subject_4.text(): (
                                    f'{self.ui.Subject_4From.time().toString().split(":")[0]}.{self.ui.Subject_4From.time().toString().split(":")[1]}',
                                    f'{self.ui.Subject_4To.time().toString().split(":")[0]}.{self.ui.Subject_4To.time().toString().split(":")[1]}'),
                                    self.ui.Subject_5.text(): (
                                    f'{self.ui.Subject_5From.time().toString().split(":")[0]}.{self.ui.Subject_5From.time().toString().split(":")[1]}',
                                    f'{self.ui.Subject_5To.time().toString().split(":")[0]}.{self.ui.Subject_5To.time().toString().split(":")[1]}'),
                                    self.ui.Subject_6.text(): (
                                    f'{self.ui.Subject_6From.time().toString().split(":")[0]}.{self.ui.Subject_6From.time().toString().split(":")[1]}',
                                    f'{self.ui.Subject_6To.time().toString().split(":")[0]}.{self.ui.Subject_6To.time().toString().split(":")[1]}'),
                                    self.ui.Subject_7.text(): (
                                    f'{self.ui.Subject_7From.time().toString().split(":")[0]}.{self.ui.Subject_7From.time().toString().split(":")[1]}',
                                    f'{self.ui.Subject_7To.time().toString().split(":")[0]}.{self.ui.Subject_7To.time().toString().split(":")[1]}'),
                                    self.ui.Subject_8.text(): (
                                    f'{self.ui.Subject_8From.time().toString().split(":")[0]}.{self.ui.Subject_8From.time().toString().split(":")[1]}',
                                    f'{self.ui.Subject_8To_2.time().toString().split(":")[0]}.{self.ui.Subject_8To_2.time().toString().split(":")[1]}')}
        self.empty = ""
        self.finalSubjectsAndTimes = {}
        for i in self.rawSubjectsAndTimes:
            if i != self.empty:
                self.finalSubjectsAndTimes[i] = self.rawSubjectsAndTimes[i]

        print("finalSubjectAndTimes", self.finalSubjectsAndTimes)
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # -------------------------Creating sublist for the TimeTabel Module and Storing in DataBase--------------------------------------------------------------------------------------
        self.sub_lst = []
        for name, dayss in self.DaysAndSubjectDictionary.items():
            self.sub_lst.append({name: dayss})
        print(self.sub_lst)
        sublistdb.insert({"sub_list": self.sub_lst})

        # ----------------------Writing the Days and Subject Name to Database file-------------------------------------
        db.truncate()
        for subject_name, days_lst in self.finalDaysAndSubjectList:
            db.insert({subject_name: days_lst})
        # --------------------------------------------------------------------------
        # --------------------------Writing LinkDict to Database file -------------------------
        linkdicdb.truncate()
        print(self.linkdic)
        for subjectname, link in self.linkdic.items():
            if subjectname != "":
                linkdicdb.insert({subjectname: link})
        # ---------------------Writing times dictionary of finalSubjectAndTimes in Database-----------------------------------------
        timesdb.truncate()
        for subjt, times in self.finalSubjectsAndTimes.items():
            timesdb.insert({subjt: times})
        # ---------------------------------------------------------------------------------------------------------------------------

        # ---------------------------------------------------------------------------------------------------------------

        self.close()
        self.main = Ui_regularWidow()
        self.main.show()

    # ----------------------------------------------------------------------------------------------------------------------------
    def dayreturn(self, a):
        if a.isChecked() == True:
            return str(a.text())

    def noneclear(self, iter):
        a = iter
        for i in a:
            if i == False:
                del a[i.index()]
        return a

    def ShowFrame(self, nameofFrame):
        
        return nameofFrame.show()


    def previousButtonClicked(self):
        self.close()
        self.main = Login()
        self.main.show()

    def closer(self):
        self.close()


class CircularSplashScreen(QMainWindow):
    def __init__(self):
        super(CircularSplashScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ProgressBarValue(2)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Progresser)
        self.timer.start(35)

        self.show()

    def Progresser(self):
        global count
        from random import choice

        processingmsg = ["Searching Files","Connecting Database"]
        self.loadinHTML = f"""<html><head/><body><p align="center"><span style=" font-size:8pt;">
        {choice([choice(processingmsg),choice(processingmsg),choice(processingmsg),choice(processingmsg)] )}....
        </span></p></body></html>"""
        self.ui.LoadingLabel.setText(self.loadinHTML)

        self.ProgressBarValue(count)
        self.html = ''' <html><head/><body><p align="center"><span style=" font-size:72pt;
         font-weight:600;">{VALUE}</span><span style=" font-size:24pt; vertical-align:super;">%</span></p></body></html> '''
        self.html = self.html.replace('{VALUE}',str(count) )

        self.ui.PercentLabel.setText(self.html)

        if count>=100:
            self.timer.stop()
            self.ProgressBarValue(100)
            self.ui.PercentLabel.setText(''' <html><head/><body><p align="center"><span style=" font-size:72pt;
         font-weight:600;">100</span><span style=" font-size:24pt; vertical-align:super;">%</span></p></body></html> ''')

            self.ui.LoadingLabel.setText('<html><head/><body><p align="center"><span style=" font-size:8pt;">Done!</span></p></body></html>')
            # count = 0
            self.close()
            self.timer.stop()

            if OpenLoginScreen == True:
                self.main = Login()
            else:
                self.main = Ui_regularWidow()

            self.main.show()


        count+= 1

    def ProgressBarValue(self,value):

        stylesheet = """
    QLabel{
border-radius:150px;
	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 53, 53, 0), stop:{STOP_2} rgba(255, 245, 53, 255));
}"""
        progress = (100 - value) / 100.00
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = stylesheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.ProgressBar.setStyleSheet(newStylesheet)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircularSplashScreen()
    sys.exit(app.exec_())
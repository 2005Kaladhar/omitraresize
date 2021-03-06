import time
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)


def class_finder(link_dic, sub_lst, times):
    def audio(text):
        engine.say(text)
        engine.runAndWait()

    from plyer import notification

    def notify(title, message, timeout=3, app_icon=None):
        notification.notify(title=title, message=message, timeout=timeout, app_icon=app_icon)

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

    def none_clear(day_sub_lst):
        count = 0
        for i in day_sub_lst:
            if i == None:
                del day_sub_lst[count]
            count += 1
        if day_sub_lst.count(None) != 0:
            return none_clear(day_sub_lst)
        else:
            return day_sub_lst

    def collector(x):
        for i in x.keys():
            if Day in x[i]:
                return i

    now = str(time.asctime(time.localtime()))
    separator = now.split(' ')
    Day = separator[0]
    Month = separator[2]
    Date = separator[2]
    print(separator)
    Time = str(separator[3]).split(':')  # s
    Hour, Minute = Time[0], Time[1]


    day_sub_lst = list(map(collector, sub_list))
    if day_sub_lst == []:
        audio("Your don't have any meeting today; Just relax")
        notify(title="You Don't have any meeting today", message="No meetings Today...")
        exit()

    day_sub_lst = none_clear(day_sub_lst)

    current_time = f"{Hour}.{Minute}"

    def __get_item__(dict, value_of_the_key):
        for x, y in dict.items():
            if y == value_of_the_key:
                return x
            else:
                continue

    def link_returner(key_word=None):
        print(key_word)
        return link_dic[key_word]

    # s
    def list_sorter(list):
        ret_lst = []

        for i in range(len(list)):
            ret_lst.append(min(list))
            del list[list.index(min(list))]
        return ret_lst

    def value_time():
        hr = int(Hour)
        diction = {13: 12.50, 10: 9.45, 11: 10.30, 12: 11.15}
        for i in diction.keys():
            if hr == i:
                return diction[i]
            else:
                continue

    def next_class_finder():
        global times
        lst = {}
        for i in day_sub_lst:
            lst.update({str(i): float(times[str(i)][0])})
        time_list = list_sorter(list(lst.values()))
        for i in time_list:
            if i > float(current_time):
                return __get_key__(lst, i)

    def class_time_wise_sorter():
        ret_list = {}
        for i in day_sub_lst:
            ret_list.update({i: float(times[i][0])})

        sorted_list = list_sorter(list(ret_list.values()))
        return_list = []
        for i in sorted_list:
            return_list.append(__get_key__(ret_list, i))
        return return_list

    day_sub_lst = class_time_wise_sorter()

    current_time = f"{Hour}.{Minute}"
    current_time = float(current_time)
    # current_time = 9.50

    for i in day_sub_lst:
        # if float(times[i][0])>=current_time and float(times[i][0])<time_adder(str(current_time),40):
        print(f"last time for the class {float(times[day_sub_lst[-1]][1])}")
        if current_time >= float(times[day_sub_lst[-1]][1]):
            notify(app_icon=None, title="All the Classes are over now ...",
                   message="Classes Over...", timeout=4)
            audio("All the classes are over now ")
            print(day_sub_lst)

            # Conversion of time greater than 12 into 1,2,3....
            # if int(times[day_sub_lst[-1]][0]) >12:
            #     times[day_sub_lst[-1]][0] = str(int(times[day_sub_lst[-1]][0])-12)
            # elif int(times[day_sub_lst[-1]][1]).split('.')[0] >12:
            #     times[day_sub_lst[-1]][1].split('.')[0] = str(int(times[day_sub_lst[-1]][1]).split('.')[0] -12)

            audio(f", Today You had {day_sub_lst[0:len(day_sub_lst) - 1]} and the last class ;{day_sub_lst[-1]};"
                  f"from {(times[day_sub_lst[-1]][0]).split('.')[0]} {(times[day_sub_lst[-1]][0]).split('.')[1]} to  "
                  f"{(times[day_sub_lst[-1]][1]).split('.')[0]} {(times[day_sub_lst[-1]][1]).split('.')[1]}. Have a good day")
            quit()
            break
        # ss
        # if float(times[str(i)][0]) < current_time and current_time<time_adder(times[i][0],40) :
        if float(times[str(i)][0]) < current_time and current_time < float(times[str(i)][1]):
            print("start time = ", float(times[str(i)][0]))
            print("end time   =", float(times[str(i)][1]))
            notify(title=f"It is your {i} class Kaladhar ...", message="Attend your class now", timeout=5)
            audio(f"At your service  ;It is your {i} class. Attend your class now. "
                  f"I'm setting up everything for you, wait for sometime")
            print(i)
            print(day_sub_lst)
            return link_returner(i)

        else:
            continue

    def finalCkecker(func):
        class_link = func()
        if Day == "Sun":
            audio("Today is holiday , no class is there ")
            quit()

        if class_link == None and float(current_time) < 13.45 and float(current_time) < float(
                times[next_class_finder()][0]):
            audio(f"{next_class_finder()} class has not started yet , waiting for it to start. It will start at "
                  f"{(times[next_class_finder()][0]).split('.')[0]} {(times[next_class_finder()][0]).split('.')[1]} "
                  f";The last class you had, was, {day_sub_lst[day_sub_lst.index(str(next_class_finder())) - 1]}")

        # while class_link == None and float(current_time) < 13.45 and float(current_time) < float(times[next_class_finder()][0]):
        #     time.sleep(2)

        # if class_link == None and float(current_time)<13.45 and float(current_time)>9.05:
        if class_link == None and float(current_time) < float(day_sub_lst[-1][-1]) and float(current_time) > float(
                day_sub_lst[1][1]):
            # print(class_link)
            print(float(times[next_class_finder()][0]))
            audio(f"One class has just finished  ,"
                  f" waiting for the other class to start. The next class that you are going to have ,"
                  f"is, {next_class_finder()}, be ready ")

        else:
            print(class_link)
            return class_link























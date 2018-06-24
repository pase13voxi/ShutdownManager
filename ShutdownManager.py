# import the library
import os
from threading import Timer
from appJar import gui

# 1 = 30min
time_spans = []
it = 0


def read_config():
    # read file
    with open("intervals.txt", "r") as ins:
        file = []
        for line in ins:
            file.append(line)
    # check if exist and add timespans
    global time_spans
    if len(file) < 2:
        time_spans = time_spans + [4,2,1]
    else:
        intervals = file[1].split(",")
        for interval in intervals:
            time_spans.append(int(interval))


def quit_program():
    os._exit(0)


def shutdown():
    print("SHUTDOWN!")
    os.system('shutdown -s')
    quit_program()


def question_dialog():
    global it
    print(str(time_spans[it]) + " secs are over!")
    if it < len(time_spans) - 1:
        it += 1
    app.showSubWindow("Question")
    timer_shutdown()


def timer_normal(btn):
    if btn == "OK":
        app.hide()
    else:
        print("Stoppe Shutdown Timer")
        t_shutdown.cancel()
        app.hideSubWindow("Question")
    print("Start")
    # ? half hours until next question
    t = Timer(time_spans[it]*60*30, question_dialog)
    t.start()


# global timer
t_shutdown = Timer(1, shutdown)


def timer_shutdown():
    print("Start Shutdown Timer")
    global t_shutdown
    # 5 minutes until shutdown
    t_shutdown = Timer(5*60, shutdown)
    t_shutdown.start()


# main

read_config()

with gui("Shutdown", "300x100", font={'size': 18}, showIcon=False) as app:
    app.setIcon("icon.ico")
    app.label("sh_start", "Shutdown starten?")
    app.setLabelFg("sh_start", "Green")
    app.addButton("OK", timer_normal)

    with app.subWindow("Question", "Shutdown", size="300x100"):
        app.label("sh_trigger", "Bist du noch wach?")
        app.setLabelFg("sh_trigger", "Red")
        app.addButton("JA", timer_normal)
        app.enableEnter(timer_normal)
        app.setStopFunction(quit_program)

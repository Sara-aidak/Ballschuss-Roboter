import math
import time
from lib.camera import *
from lib.controller import *
from lib.display import *
from lib.lib_move_sync import *

pos_green = None
v = None
pos_red = None
startbereit = None
cmd = None
sr = None
sg = None
pos_load = None
sy = None
pos_f = None
pos_yellow = None
ts = None
pos = None
b = None
speed_slow = None
number_targets = None
i = None
speed_fast = None
ts_diff = None
d = None
fwd_d_min = None
fwd_d_max = None
pos_n = None
yellow_downed = None
ts_last = None
red_downed = None
green_downed = None
red_main = None
d_yellow = None
green_main = None
d_red = None
d_green = None
yellow_main = None
run2 = None


def ball_callback(event):
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    if startbereit:
        if not yellow_downed and sy:
            ts = (time.time() * 1000)
            ts_diff = ts - ts_last
            ts_last = ts
            pos_yellow = event.value.x
            d_yellow = event.value.diameter
            cmd = '-'
            if math.fabs(pos_yellow) < math.fabs(pos_green) and math.fabs(pos_yellow) < math.fabs(pos_red):
                yellow_main = True
                green_main = False
                red_main = False
                pos = pos_yellow
                d = d_yellow
                moveStep()
                print('yellow: pos:{} d:{} cmd:{} tdiff:{}'.format(pos_yellow, d_yellow, cmd, ts_diff))
            time.sleep(0.05)


def moveStep():
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    if pos >= -b and pos <= b:
        if d < fwd_d_min:
            moveFwdDist(speed_slow, 10)
            cmd = 'fwd'
        elif d > fwd_d_max:
            moveBwdDist(speed_slow, 10)
            cmd = 'bwd'
        else:
            stop()
            fire()
            if red_main:
                red_downed = True
                pos_red = 100
                cmd = 'fire red'
            if green_main:
                green_downed = True
                pos_green = 100
                cmd = 'fire green'
            if yellow_main:
                yellow_downed = True
                pos_yellow = 100
                cmd = 'fire yellow'
            number_targets = (number_targets if isinstance(number_targets, (int, float)) else 0) + -1
            if number_targets <= 0:
                run2 = False
                cmd = 'end'
    elif pos > b:
        cmd = 'sr'
        moveSR(speed_slow, 10)
    elif pos < -b:
        moveSL(speed_slow, 10)
        cmd = 'sl'
    elif pos < -70 and pos > 70:
        stop()
        cmd = 'stop out of bounds'
    else:
        stop()
        cmd = 'stop else'


def ball_callback2(event):
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    if startbereit:
        if not red_downed and sr:
            ts = (time.time() * 1000)
            ts_diff = ts - ts_last
            ts_last = ts
            pos_red = event.value.x
            d_red = event.value.diameter
            cmd = '-'
            if math.fabs(pos_red) < math.fabs(pos_green) and math.fabs(pos_red) < math.fabs(pos_yellow):
                red_main = True
                green_main = False
                yellow_main = False
                pos = pos_red
                d = d_red
                moveStep()
                print('red: pos:{} d:{} cmd:{} tdiff:{}'.format(pos_red, d_red, cmd, ts_diff))
            time.sleep(0.05)


def ball_callback3(event):
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    if startbereit:
        if not green_downed and sg:
            ts = (time.time() * 1000)
            ts_diff = ts - ts_last
            ts_last = ts
            pos_green = event.value.x
            d_green = event.value.diameter
            cmd = '-'
            if math.fabs(pos_green) < math.fabs(pos_red) and math.fabs(pos_green) < math.fabs(pos_yellow):
                green_main = True
                red_main = False
                yellow_main = False
                pos = pos_green
                d = d_green
                moveStep()
                print('green: pos:{} d:{} cmd:{} tdiff:{}'.format(pos_green, d_green, cmd, ts_diff))
            time.sleep(0.05)


def testMoveRotate():
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    v = 512
    moveRotL(v, 256)
    moveRotR(v, 256)


def on_txt_button_clicked(event):
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    if number_targets > 0:
        startbereit = True


def testMoveTranslate():
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    v = 512
    moveFwdDist(v, 200)
    moveSL(v, 350)
    moveBwdDist(v, 200)
    moveSR(v, 350)


def on_txt_switch_red_toggled(event):
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    if display.get_attr("txt_switch_red.checked"):
        sr = True
        display.set_attr("txt_status_indicator_red.active", str(True).lower())
        number_targets = (number_targets if isinstance(number_targets, (int, float)) else 0) + 1
    elif not (display.get_attr("txt_switch_red.checked")):
        sr = False
        display.set_attr("txt_status_indicator_red.active", str(False).lower())
        number_targets = (number_targets if isinstance(number_targets, (int, float)) else 0) + -1


def testServo():
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    TXT_M_S1_servomotor.set_position(int(240))
    time.sleep(1)
    TXT_M_S1_servomotor.set_position(int(120))
    time.sleep(1)
    TXT_M_S1_servomotor.set_position(int(240))


def on_txt_switch_green_toggled(event):
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    if display.get_attr("txt_switch_green.checked"):
        sg = True
        display.set_attr("txt_status_indicator_green.active", str(True).lower())
        number_targets = (number_targets if isinstance(number_targets, (int, float)) else 0) + 1
    elif not (display.get_attr("txt_switch_green.checked")):
        sg = False
        display.set_attr("txt_status_indicator_green.active", str(False).lower())
        number_targets = (number_targets if isinstance(number_targets, (int, float)) else 0) + -1


def load():
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    TXT_M_S1_servomotor.set_position(int(pos_load))
    time.sleep(0.3)
    for i in (pos_load <= pos_n) and upRange(pos_load, pos_n, 5) or downRange(pos_load, pos_n, 5):
        TXT_M_S1_servomotor.set_position(int(i))
        time.sleep(0.005)


def on_txt_switch_yellow_toggled(event):
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    if display.get_attr("txt_switch_yellow.checked"):
        sy = True
        display.set_attr("txt_status_indicator_yellow.active", str(True).lower())
        number_targets = (number_targets if isinstance(number_targets, (int, float)) else 0) + 1
    elif not (display.get_attr("txt_switch_yellow.checked")):
        sy = False
        display.set_attr("txt_status_indicator_yellow.active", str(False).lower())
        number_targets = (number_targets if isinstance(number_targets, (int, float)) else 0) + -1


def fire():
    global pos_green, v, pos_red, startbereit, cmd, sr, sg, pos_load, sy, pos_f, pos_yellow, ts, pos, b, speed_slow, number_targets, i, speed_fast, ts_diff, d, fwd_d_min, fwd_d_max, pos_n, yellow_downed, ts_last, red_downed, green_downed, red_main, d_yellow, green_main, d_red, d_green, yellow_main, run2
    TXT_M_S1_servomotor.set_position(int(pos_f))
    time.sleep(0.2)
    TXT_M_S1_servomotor.set_position(int(pos_load))
    time.sleep(0.3)
    TXT_M_S1_servomotor.set_position(int(pos_n))
    time.sleep(0.3)


ball_detector_yellow.add_detection_listener(ball_callback)
ball_detector_red.add_detection_listener(ball_callback2)
ball_detector_green.add_detection_listener(ball_callback3)

display.button_clicked("txt_button", on_txt_button_clicked)
display.switch_toggled("txt_switch_red", on_txt_switch_red_toggled)
display.switch_toggled("txt_switch_green", on_txt_switch_green_toggled)
display.switch_toggled("txt_switch_yellow", on_txt_switch_yellow_toggled)

def upRange(start, stop, step):
    while start <= stop:
        yield start
        start += abs(step)
def downRange(start, stop, step):
    while start >= stop:
        yield start
        start -= abs(step)

pos_green = 100
pos_red = 100
pos_yellow = 100
speed_fast = 512
speed_slow = 250
b = 7
fwd_d_min = 40
fwd_d_max = 55
pos_load = 110
pos_n = pos_load + 120
pos_f = pos_load + 270
load()
ts = (time.time() * 1000)
ts_last = (time.time() * 1000)
ts_diff = 0
run2 = True
while True:
    if run2 == False:
        break

# BICYCLE REAR LIGHT by Darryl Sloan
# Tutorial on Youtube https://www.youtube.com/watch?v=S95W_gbjBNs&list=PLsoYifahFi50gKtSOX23HI6sgw9k8UGZb&index=2

from microbit import *

status = 1
blink_rate = 100
while True:
    if status > 0:
        display.show(Image("99999:99999:99999:99999:99999"))
    sleep(blink_rate)
    if status < 2:
        display.clear()
    sleep(blink_rate)
    if button_a.was_pressed():
        status += 1
    if status == 3:
        status = 0
    if button_b.was_pressed():
        blink_rate -= 50
    if blink_rate == 0:
        blink_rate = 250

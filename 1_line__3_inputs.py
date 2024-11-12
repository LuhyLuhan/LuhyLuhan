from microbit import*
t = 1000
l1 = pin12
l2 = pin14
l3 = pin16
while True:
    sens = pin0
    val = sens.read_analog()
    if 400 < val < 600:
        print('Load 1: True:')
        l1.write_digital(1)
        l2.write_digital(0)
        l3.write_digital(0)
        sleep(t)
    if 5 < val < 10:
        print('Load 2: True:')
        l2.write_digital(1)
        l1.write_digital(0)
        l3.write_digital(0)
        sleep(t)
    if 700 < val < 900:
        print('Load 3: True:')
        l3.write_digital(1)
        l2.write_digital(0)
        l1.write_digital(0)
        sleep(t)
    else:
        l1.write_digital(0)
        l2.write_digital(0)
        l3.write_digital(0)
import rotatescreen
import time

screen = rotatescreen.get_primary_display()
rs=int(input("How many times you want to rotate:") or 10)
for i in range(rs):
    screen.rotate_to(i*90 % 360)
    time.sleep(1.5)

screen.rotate_to(0)

from sense_hat import SenseHat
import time
sense = SenseHat()

#x and y coords
x = 0 
y = 0

while(1)
  #Dont know the function to grab the stuff
  getAngleOfX
  getAngleOfY
  clamp(x,-89,89)
  clamp(y,-89,89)
  #maps x,y to nearest int between 0,8
  x = int(x/11.25)
  y = int(y/11.25)
  sense.set_pixel(x,y,0,0,255)
  time.sleep(0.1)

#restrains value between minn and maxn
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

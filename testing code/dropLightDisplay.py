from sense_hat import SenseHat
import time
sense = SenseHat()

#x and y coords
x = 0 
y = 0
lastx = 0
lasty = 0

sense.clear()


#restrains value between minn and maxn
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def getDegree(plain)
  #gets accelerometer values 
  orientation = sense.get_orientation()
  values = ("{pitch} {roll} {yaw}".format(**orientation))
  #splits them from string and determines if x or y, and lastly changes to float
  values = values.split()
  if plain == "x":
    values = values[0]
  elif plain == "y":
    values = values[1]
  values = float(values)
  if values > 180:
    values = values - 360
  return values

while(1)
  #Dont know the function to grab the stuff
  x = getDegree("x")
  y = getDegree("y")
  clamp(x,-89,89)
  clamp(y,-89,89)
  #maps x,y to nearest int between 0,8
  x = abs(int(x/22.5+4)-7)
  y = int(y/22.5+4)
  sense.set_pixel(lastx,lasty,0,0,0)
  sense.set_pixel(x,y,0,0,255)
  lastx = x
  lasty = y 

import datetime
import time

class Clock:	
	def getTime(self):
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		time_now = current_time.split(":")
				
		return time_now

	def keepThiking(self, number):
		result = ""
		if number % 2:
			result = "Tic!"
		else:
			result = "Tac!"
			
		return result
	
	
class Alarm(Clock):
	def __init__(self,alarm_h, alarm_m, alarm_s):
		self.alarm_h = alarm_h
		self.alarm_m = alarm_m
		self.alarm_s = alarm_s

	def getAlarm(self):
		return print(self.alarm_h, self.alarm_m, self.alarm_s)

	def triggerAlarm(self):
		result = "Wakie Wakies!!!"
		return result

def main():
	myTime = Clock()
	myAlarm = Alarm(23, 26, 10)
	myAlarm.getTime()

	while((myAlarm.alarm_h != int(myTime.getTime()[0])) or (myAlarm.alarm_m != int(myTime.getTime()[1])) or (myAlarm.alarm_s >= int(myTime.getTime()[2]))):
		hours = int(myTime.getTime()[0])
		minutes = int(myTime.getTime()[1])
		seconds = int(myTime.getTime()[2])
		tiking = myTime.keepThiking(seconds)
		print(tiking)
		print(f"Time is: {hours}:{minutes}:{seconds}")
		time.sleep(1)

	print(myAlarm.triggerAlarm())
	print("Thanks for playing!!")

if __name__ == "__main__":
	main()
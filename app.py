import psutil
import threading

class battery_indicator:
    def __init__(self):
        self.battery = psutil.sensors_battery()
        self.is_charging = self.battery.power_plugged
        self.percent = self.battery.percent
        self.status = False

    @property
    def is_plugged(self):
        return self.is_plugged

    def update(self):
        self.percent = self.battery.percent
        self.is_charging = self.battery.power_plugged

        if self.is_charging and self.percent == 100:
            self.status = True

    
    
    def get_status(self):
        return self.status


def loop():
    bat_indicator = battery_indicator()
    while not bat_indicator.get_status():
        bat_indicator.update() 

if __name__ == "__main__":
    #avail = threading.Event()
    thread = threading.Thread(target = loop)
    thread.start()
    
    thread.join()

    print('UNPLUG ')
#print('Current Battery Perecentage: {}\n Plugged in status: {}'.format(str(percent), str(is_plugged)))
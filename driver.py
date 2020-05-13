import psutil
import threading
import ctypes
import requests, json
import time
#import Tkinter
#import tkMessageBox


def display_message(status, lock):
    lock.acquire()
    if status == 'unplugged':
        msg = 'Unplugged your laptop'
        ctypes.windll.user32.MessageBoxW(0, msg, "Battery Indicator", 1)
    elif status == 'charged':
        msg = 'You\'re battery is charged! time to unplug!'
        ctypes.windll.user32.MessageBoxW(0, msg, "Battery Indicator", 1)
    elif status == 'started':
         ctypes.windll.user32.MessageBoxW(0, 'Script Started', "Battery Indicator", 1)
    lock.release()


if __name__ == "__main__":

    url = 'http://127.0.0.1:5000/script/status'
    lock = threading.Lock()
 
    is_charging = False
    while True:
        battery = psutil.sensors_battery()
        #is_charging = battery.power_plugged
        #percent = battery.percent
        
        if is_charging == True and battery.power_plugged == False:
            #msg = 'Unplugged your laptop'
            #ctypes.windll.user32.MessageBoxW(0, msg, "Battery Indicator", 1)
            thread1 = threading.Thread(target=display_message, args=('unplugged',lock))
            thread1.daemon = True                            # Daemonize thread
            thread1.start()                                  # Start the execution
            data = {'Status': 'unplugged', 'Precentage': percent}
            data_json = json.dumps(data)
            r = requests.post(url, json=data)
            print(r.content)
            continue
        
        percent = battery.percent
        is_charging = battery.power_plugged
        
        if is_charging == True and percent >= 99:
            #msg = 'You\'re battery is charged! time to unplug!'
            #ctypes.windll.user32.MessageBoxW(0, msg, "Battery Indicator", 1)
            thread2 = threading.Thread(target=display_message, args=('charged',lock))
            thread2.daemon = True                            # Daemonize thread
            thread2.start()   
            data = {'Status': 'charged', 'Precentage': percent}
            data_json = json.dumps(data)
            r = requests.post(url, json=data)
            print(r.content.decode("utf-8"))

        elif is_charging == False:
            data = {'Status': 'unplugged', 'Precentage': percent}
            data_json = json.dumps(data)
            r = requests.post(url, json=data)
            print(r.content.decode("utf-8"))

        else:
            data = {'Status': 'charging', 'Precentage': percent}
            data_json = json.dumps(data)
            r = requests.post(url, json=data)
            print(r.content.decode("utf-8"))

        
        # DEBUGGING
        time.sleep(1)

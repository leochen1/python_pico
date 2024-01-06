import network
import time
from machine import WDT, Timer, ADC, RTC
import urequests as requests

def connect(): 
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.connect('NULL', '78787878')

    max_wait = 10
    while max_wait > 0:
        max_wait -= 1
        status = nic.status()
        print("status : ", status)
        if status < 0 or status >= 3:
            break
        print("wait...")
        time.sleep(1)


    # 沒有 wifi 的處理
    if nic.status() != 3:
        # 連線失敗
        # wdt = WDT(timeout=2000)
        # wdt.feed()
        raise RuntimeError('連線失敗')
    else:
        print("OK")
        print(nic.ifconfig())


def alert(t:flaot):
    print('要爆炸了!')
    rtc = RTC()
    date_tuple = rtc.datetime()
    year = date_tuple[0]
    month = date_tuple[1]
    day = date_tuple[2]
    hour = date_tuple[4]
    minites = date_tuple[5]
    second = date_tuple[6]
    date_str = f'{year}-{month}-{day} {hour}:{minites}:{second}'
    response = requests.get(f'https://hook.us1.make.com/idfhmwhq5xdzpjq6aw7153j1a1ejr53g?name=Leo_Pico&date={date_str}&temperature={t}')
    print(help(response))
    response.close()
    
    
def callback1(t:Timer):
    global start
    sensor = ADC(4)    
    vol = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f'溫度:{temperature}')    
    delta = time.ticks_diff(time.ticks_ms(), start)
    print(delta)
    #溫度超過24度,並且發送alert()的時間已經大於60秒
    if temperature >= 24 and delta >= 60 * 1000:        
        alert(temperature)
        start = time.ticks_ms()#重新設定計時的時間
        

connect()       

start = time.ticks_ms() - 60 * 1000 #應用程式啟動時,計時時間,先減60秒    
time1 = Timer()
time1.init(period=1000,callback=callback1)

# https://hook.us1.make.com/idfhmwhq5xdzpjq6aw7153j1a1ejr53g?name=test&date=2024-01-06-14:30:30&temperature=22




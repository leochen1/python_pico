import network
import time
from machine import WDT


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

connect()



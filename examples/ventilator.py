import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mite import Ventilator
import time

ventilator = Ventilator()
counter = 1
while True:
    data = {"foo": "bar", "counter": counter}
    ventilator.send(data)
    print("send", data)
    time.sleep(0.5)
    counter += 1
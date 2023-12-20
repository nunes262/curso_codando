from threading import Thread
from time import sleep

def pato(palavra: str, tempo: int):
    while True:
        print(palavra)
        sleep(1)

Thread(target=pato, args=["pato", 1]).start()
Thread(target=pato, args=["pato", 0.5]).start()

while True:
    res = input("coloque um dado ->")
    print(res)
    sleep(3)
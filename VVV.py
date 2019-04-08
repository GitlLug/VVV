from gpiozero import LED
from time import sleep

seg1 = LED(21)
seg2 = LED(20)
seg4 = LED(26)
seg5 = LED(16)
seg6 = LED(19)
seg7 = LED(13)
seg9 = LED(12)
seg10 = LED(6)

seg1b = LED(5)
seg2b = LED(1)
seg4b = LED(0)
seg5b = LED(7)
seg6b = LED(8)
seg7b = LED(11)
seg9b = LED(25)
seg10b = LED(9)


#seg1.on()()
#seg2.on()()
#seg4.on()
#seg5.on()()
#seg6.on()
#seg7.on()()
#seg9.on()()
#seg10.on()()

def display1b():
    seg6b.on()
    seg4b.on()
def display2b():
    seg7b.on()
    seg6b.on()
    seg10b.on()
    seg1b.on()
    seg2b.on()
    return
def display3b():
    seg7b.on()
    seg4b.on()
    seg10b.on()
    seg6b.on()
    seg2b.on()
    return
def display4b():
    seg9b.on()
    seg10b.on()
    seg6b.on()
    seg4b.on()
    return
def display5b():
    seg7b.on()
    seg9b.on()
    seg10b.on()
    seg4b.on()
    seg2b.on()
    return
    
def display6b():
    seg7b.on()
    seg9b.on()
    seg10b.on()
    seg1b.on()
    seg2b.on()
    seg4b.on()
    return
def display7b():
    seg7b.on()
    seg6b.on()
    seg4b.on()
    return
def display8b():
    seg7b.on()
    seg9b.on()
    seg10b.on()
    seg6b.on()
    seg1b.on()
    seg2b.on()
    seg4b.on()
    return
def display9b():
    seg7b.on()
    seg9b.on()
    seg10b.on()
    seg6b.on()
    seg4b.on()
    return

def display1():
    seg4.on()
    seg6.on()
    return
def display2():
    seg7.on()
    seg6.on()
    seg10.on()
    seg1.on()
    seg2.on()
    return
def display3():
    seg7.on()
    seg6.on()
    seg10.on()
    seg4.on()
    seg2.on()
    return
def display4():
    seg9.on()
    seg10.on()
    seg6.on()
    seg4.on()
    return
def display5():
    seg7.on()
    seg9.on()
    seg10.on()
    seg4.on()
    seg2.on()
    return
def display6():
    seg7.on()
    seg9.on()
    seg1.on()
    seg2.on()
    seg4.on()
    seg10.on()
    return
def display7():
    seg7.on()
    seg6.on()
    seg4.on()
    return
def display8():
    seg7.on()
    seg6.on()
    seg9.on()
    seg10.on()
    seg1.on()
    seg2.on()
    seg4.on()
    return
def display9():
    seg9.on()
    seg7.on()
    seg6.on()
    seg10.on()
    seg4.on()
    return
def displaya():
    seg7.on()
    seg6.on()
    seg10.on()
    seg1.on()
    seg4.on()
    seg9.on()
    return
def displayb():
    seg1.on()
    seg2.on()
    seg4.on()
    seg5.on()
    seg6.on()
    seg7.on()
    seg9.on()
    seg10.on()
    return
def displayc():
    seg7.on()
    seg9.on()
    seg1.on()
    seg2.on()
    return
def displayd():
    seg7.on()
    seg9.on()
    seg1.on()
    seg2.on()
    seg4.on()
    seg6.on()
    return
def displaye():
    seg7.on()
    seg9.on()
    seg10.on()
    seg1.on()
    seg2.on()
    return

def displayf():
    seg1.on()
    seg10.on()
    seg9.on()
    seg7.on()
    return
def displayg():
    seg7.on()
    seg9.on()
    seg10.on()
    seg6.on()
    seg4.on()
    seg2.on()
    return
def displayh():
    seg9.on()
    seg10.on()
    seg1.on()
    seg4.on()
    return
def displayH():
    seg1.on()
    seg10.on()
    seg4.on()
    seg6.on()
    seg9.on()
    return
def alloff():
    seg1.off()
    seg2.off()
    seg4.off()
    seg5.off()
    seg6.off()
    seg7.off()
    seg9.off()
    seg10.off()
    return

def alloffb():
    seg1b.off()
    seg2b.off()
    seg4b.off()
    seg5b.off()
    seg6b.off()
    seg7b.off()
    seg9b.off()
    seg10b.off()
    return

alloff()
display1()
sleep(.5)
alloff()
display2()
sleep(.5)
alloff()
display3()
sleep(.5)
alloff()
display4()
sleep(.5)
alloff()
display5()
sleep(.5)
alloff()
display6()
sleep(.5)
alloff()
display7()
sleep(.5)
alloff()
display8()
sleep(.5)
alloff()
display9()
sleep(.5)
alloff()
displaya()
sleep(.5)
alloff()
displayb()
sleep(.5)
alloff()
displayc()
sleep(.5)
alloff()
displayd()
sleep(.5)
alloff()
displaye()
sleep(.5)
alloff()
displayf()
sleep(.5)
alloff()
displayg()
sleep(.5)
alloff()
displayh()
sleep(.5)
alloff()
displayH()
sleep(.5)

#2nd LED
display1b()
sleep(.5)
alloffb()
display2b()
sleep(.5)
alloffb()
display3b()
sleep(.5)
alloffb()
display4b()
sleep(.5)
alloffb()
display5b()
sleep(.5)
alloffb()
display6b()
sleep(.5)
alloffb()
display7b()
sleep(.5)
alloffb()
display8b()
sleep(.5)
alloffb()
display9b()
sleep(.5)
alloffb()

while True:
    x=input("what number do you want me to display?")
    alloff()
    alloffb()
    
    if x=="1":
        display1()
    elif x=="2":
        display2()
    elif x=="3":
        display3()
    elif x=="4":
        display4()
    elif x=="5":
        display5()
    elif x=="6":
        display6()
    elif x=="7":
        display7()
    elif x=="8":
        display8()
    elif x=="9":
        display9()
    elif x=="a":
        displaya()
    elif x=="b":
        displayb()
    elif x=="c":
        displayc()
    elif x=="d":
        displayd()
    elif x=="e":
        displaye()
    elif x=="f":
        displayf()
    elif x=="g":
        displayg()
    elif x=="h":
        displayh()
    elif x=="H":
        displayH()
    elif x=="1b":
        display1b()
    elif x=="2b":
        display2b()
    elif x=="3b":
        display3b()
    elif x=="4b":
        display4b()
    elif x=="5b":
        display5b()
    elif x=="6b":
        display6b()
    elif x=="7b":
        display7b()
    elif x=="8b":
        display8b()
    elif x=="9b":
        display9b()
    else:
        print("not available")









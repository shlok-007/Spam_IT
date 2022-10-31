import pyautogui as pg
import time as t
print("It is recommended to have Whatsapp Web or Whatsapp Application opened in your device before starting the execution")
spam=input("Enter the text you want to spam:- ")
sc=int(input("How many times do you want to spam ?:- "))
print("Now, you have around a minute to put your cursor to the Whatsapp text field of the contact/group\nwhom you want to spam.")
print("Please don't change tabs during the process.\n To stop the execution in between, CLOSE the app executing the code.")
t.sleep(60)
pg.write("Spam Begins :-E")
pg.press("enter")
while(sc):
    pg.write(spam)
    pg.press("enter")
    sc-=1
print("Job Done ;-)")

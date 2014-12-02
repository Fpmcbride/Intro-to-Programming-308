from tkinter import *
from tkinter.scrolledtext import *
import tkinter.scrolledtext as tkst


alch = []
drinks = []
errors = []

class application(object):
    
    def user_name():
        ans = e1.get()
        return ans
    alch = []
    def get_alchohol():
        ans = e4.get()
        alch.append(ans)
        
    def get_drinks():
        ans = int(e5.get())
        drinks.append(ans)
            
    
    def get_alchohol_list():
        application.get_alchohol()
        application.get_drinks()

    def get_weight():
        ans = e2.get()
        return ans

    def get_gender():
        ans = e3.get()
        if (ans == 'Male'):
            ans = .68
        elif (ans == 'Female'):
            ans = .55
        else:
            ans = 1
        return ans

    def time_since_last_drink():
        ans = e6.get()
        return ans

    

    def advice(bac):
        if bac>=.08:
            print("DON'T DRIVE! You will receive a DUI and endanger the public")
        if bac>=.10:
            print("You're on the road to sloppiness.")
        if bac>=.20:
            print("You're most likely blacked out right now.")
        if bac>=.25:
            print("You are at a high risk of choking on your own vomit.")
        if bac>=.35:
            print("Coma is possible. Stop drinking.")
        if bac>=.4:
            print("You are about become a vegetable and may die due to respiratory arrest.")
    
    def receipt(name,bac,talchohol):
        ans = ("Hello ", name,"Your Blood alchohol is:",bac,"and you have consumed ",talchohol,"drinks")
        return ans

    def quit():
        global root
        root.destroy()

    def check(weight, gender_val, hours,drinks):
        a = sum(drinks)
        b = abs(a)
        if (weight < 0):
            errors.append("Please Enter a Valid weight!")
        if (gender_val == 1):
            errors.append("Please Enter a Valid Gender!")
        if (hours < 0):
            errors.append("Please Enter a Valid Amount of hours!")
        if (a < b):
            errors.append("Please Enter All Positive Numbers for the Amount of Drinks you have had of each Alchohol")
    def main():
        name = application.user_name()
        weight = float(application.get_weight())
        gender_val = float(application.get_gender())
        hours = float(application.time_since_last_drink())
        b = sum(drinks)
        check_errors = application.check(weight, gender_val, hours,drinks)
        if (len(errors) > 0):
            for i in range(len(errors)):
                print(errors[i])
            print("Please Exit the program and Try Again!")
        else:
            bac=(((b*.06*100*1.055)/(weight*gender_val))-(.015*hours))
            print("--------------------------------------------------")
            print("Hello", name,"Your Blood alchohol is:",bac)
            for i in range(len(alch)):
                print("You have had",drinks[i],"drinks of",alch[i])
            print(b,"drinks in total")
            advice = application.advice(bac)
            print("--------------------------------------------------")


        
root = Tk()


Label_title = Label(root, text="---------------------------------------------------------\nWelcome to the Regis Blood Alchohol Percentage Calculator\n---------------------------------------------------------")
label1 = Label( root, text=" Please Enter your Name")
label2 = Label( root, text="  Please Enter your Weight")
label3 = Label( root, text="  Please Enter your 'Male' or 'Female'")
label4 = Label( root, text="*********************************************************")
label5 = Label( root, text="Please add the type of alchohol you've had and how many drinks for each type\n1 drink = 1 shot(1.5oz) or 1 beer(12oz) or 1 glass(5oz) of wine")
label6 = Label( root, text="Please enter the Type of Alchohol")
label7 = Label( root, text="Please enter the Number of Drinks")
label8 = Label( root, text="Please enter how many hours ago you drank")

Label_title.grid(row= 0,column= 0)
label1.grid(row= 1, column = 0)
label2.grid(row= 2, column = 0)
label3.grid(row= 3, column = 0)
label4.grid(row= 5, column = 0)
label5.grid(row= 6, column = 0)
label6.grid(row= 7, column = 0)
label7.grid(row= 8, column = 0)
label8.grid(row= 9, column = 0)

e1 = Entry(root, bd =5)
e2 = Entry(root, bd =5)
e3 = Entry(root, bd =5)
e4 = Entry(root, bd =5)
e5 = Entry(root, bd =5)
e6 = Entry(root, bd =5)

e1.grid(row= 1, column = 1)
e2.grid(row= 2, column = 1)
e3.grid(row= 3, column = 1)
e4.grid(row= 7, column = 1)
e5.grid(row= 8, column = 1)
e6.grid(row= 9, column = 1)






add = Button(root, text = "Add", command= application.get_alchohol_list)
add.grid(row= 8, column = 2)

submit = Button(root, text ="Submit", command= application.main)
submit.grid(row= 10, column = 1)
x = Button(root, text = "Exit", command=application.quit)
x.grid(row= 12, column = 1)







root.mainloop()


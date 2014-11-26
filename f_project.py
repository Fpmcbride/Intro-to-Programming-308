
#number of drinks 
def user_name():
    name=input("What is your name? ")
    return name

# % alcohol 
def get_content():
    a=True
    drink_info=[] 
    while (a):
        type_alc=input("What kind of alcohol are you drinking?: ")
        if (type_alc=="done"):
            a=False
            return a
        print("1 drink = 1 shot(1.5oz) or 1 beer(12oz) or 1 glass(5oz) of wine")
        drinks=int(input("How many drinks have you had?: "))
        print("When done entering drinks type 'done' in alcohol type prompt")
        nest_drink=[type_alc,drinks]
        drink_info.append(nest_drink)
    return drink_info

    
def total_drinks(drink_info):
    l=len(drink_info)
    tot_drinks=0
    for i in range(l):
        tot_drinks=tot_drinks+float(drink_info[i][1])
    return tot_drinks
        

def get_weight():
    mass=(input("How much do you weigh in pounds?: "))
    weight=float(mass)
    if(weight<0):
        print("Invalid input! Weight must be greater than zero.")
        weight=get_weight()
    return weight

def get_gender(): 
    gender_input=str(input("What is your gender? (male or female)"))
    if(gender_input=="male"):
        gender=0
    elif(gender_input=="female"):
        gender=1
    else:
        print("")
        print("Invalid input! Please input 'male' or 'female'")
        print("")
        gender=get_gender()
    return gender

def get_time():
    hours=(input("How many hours has it been since your first drink?: "))
    try:
        time=float(hours)
        if(time<0):
            print("")
            print("Invalid input! Hours must be a positive number.")
            print("")
            get_time()
    except:
        print("")
        print("Invalid input! Hours must be a positive integer.")
        print("")
        get_time()
    return time

def widmark_formula(tot_drinks,weight,gender,hours):
    if gender==1:
        gender_val=.55
    else:
        gender_val=.68
    bac=(((tot_drinks*.06*100*1.055)/(weight*gender_val))-(.015*hours))
    return bac
def advice(bac):
    slut=2

def receipt(drink_info,widmark_formula,name):
    print("Hello,",name,"you have consumed:")
    for i in range(len(drink_info)):
        alch=drink_info[i][0]
        amount=drink_info[i][1]
        msg=str(amount,"drinks of",alch)
        print(msg)
    print("Your Blood Alcohol Content is:",bac)
    

def main():
    a=user_name()
    b=get_content()
    c=total_drinks(b[:])
    d=get_weight()
    e=get_gender()
    f=get_time()
    g=windmark_formula(c,d,e,f)
    h=receipt(b,g,a)
    print(h)
    
main()
          
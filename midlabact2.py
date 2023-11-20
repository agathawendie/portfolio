mensclist = []
womensclist = []

while True:
    mensc = (float(input("")))
    mensclist.append(mensc)
    if mensc != 0:
        womensc = (float(input("")))
        womensclist.append(womensc)
    else:
        mensclist.remove(0)
        break
print("")
print("Lowest Men's Score: ", format(min(mensclist), '.2f'))
print("Highest Women's Score: ", format(max(womensclist), '.2f'))

 

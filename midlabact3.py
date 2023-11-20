def main():
    def drawers():
        global subdrawer
        ndrawers = int(input("No. of Drawers: "))
        subdrawer = ndrawers * 30
    drawers()

    def woodtype():
        global woodt
        print("Wood Type: ", '\n', "'P' for Pine", '\n', "'O' for Oak", '\n', "'Q' for Other Woods")
        woodt = str(input("Input Wood Type: "))
        if woodt == "P" or woodt == "p":
            woodt = 100
        elif woodt == "O" or woodt == "o":
            woodt = 140
        elif woodt == "Q" or woodt == "q":
            woodt = 180
        else:
            pass
    woodtype()

    def cdesk():
        global price
        price = subdrawer + woodt
        return price
    cdesk()

    def total():
        print("Total Price: ", price)
    total()
main()

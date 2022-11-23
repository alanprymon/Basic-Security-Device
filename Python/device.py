if __name__ == "__main__":
    idx = 0
    unlocked = False

    # Where main code starts
    while True:
        get = input()



        if not get.isdecimal():
            # remove every character that is not a decimal (0-9)
            checked = get
            delete = set()
            for x in get:
                if not x.isdecimal():
                    delete.add(x)
            for x in delete:
                checked = checked.replace(x, "")
            delete.clear()
            get = checked

        for x in get:
            # handle the input string into individual characters
            if x == "1" and idx == 5:
                if not unlocked:
                    unlocked = True
                    print("unlocked")
                    idx = 0
            elif x == "4" and idx == 5:
                if unlocked:
                    unlocked = False
                    print("locked")
                    idx = 0
            elif x == "8" and idx == 0 or idx == 3:
                idx += 1
            elif x == "3" and idx == 1 or idx == 4:
                idx += 1
            elif x == "9" and idx == 2:
                idx += 1
            elif x == "8" and idx > 3 or idx < 3:
                idx = 1
            elif x == "9" and idx == 5:
                idx = 3
            else:
                idx = 0

import data

# Variables
accessCode = 839831
lockingCode = 839834

def enterKey(key):
        if not len(key) == 0:
            for x in key:
                if x == "8" and data.idx == 0 or data.idx == 3:
                    data.idx += 1


def unlock():
        if not data.unlocked:
            data.unlocked = True
            print("Unlocked")


# Where main code starts
while True:
    get = input()

    if not get.isdecimal():
        # remove every character that is not a decimal (0-9)
        pass

    enterKey(get)

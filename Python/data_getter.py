if __name__ == "__main__":
    rawdata = open("raw_data.txt", "r")
    data = open("data.txt", "w")
    raw = rawdata.readlines()
    rawdata.close()
    for x in range(len(raw)):
        raw[x] = int(raw[x])
    average = sum(raw) / len(raw)
    data.write("Average: " + str(average) + "\n")
    data.write("Min: " + str(min(raw)) + "\n")
    data.write("Max: " + str(max(raw)) + "\n")
    data.write("Total number of tests: " + str(len(raw)))
    data.close()
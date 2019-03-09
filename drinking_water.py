# drinking_water.py
# Raunak Anand 
# function that reads population file and builds dictionary

def canBeInt(s):
    try:
        int(s)
    except:
        return False
    return True

def makePopDictionary():
    infile = open("world_population_2017.tsv") # opening data file
    popdict={}
    for line in infile:
        line = line.strip() # remove whitespace
        data = line.split('\t') # split line at the tab
        data[2] = data[2].replace(",","") # replace commas with no space 
        data.pop(0)
        country = data.pop(1)
        for code in data:
            if(int(country) > 500000): # line wil only print if country's population is more than 500000
                # access, if population is big enough.
                popdict[code] = country

    return popdict

def readDWdata(popDict):

    infile = open("drinkingWater.csv") # opening data file
    year_1990 = [] # list of values for year 1990
    year_2010 = [] # list of values for year 2010
    country = [] # list of countries
    for i in range(3): 
       infile.readline() # ignore first three lines
    for line in infile:
        line = line.strip() # remove whitespace
        code = line.split(",") # split line at the comma

        code[21] = code[21].strip()
        code[1] = code[1].strip()
        if canBeInt(code[1]) and canBeInt(code[21]): # if following strings are integers
            year_1990.append(code[1])
            country.append(code[0])
            year_2010.append(code[21])
            # adding variables to a list

    for i in range(len(country)):
        if country[i] in popDict:
            sub = int(year_2010[i]) - int(year_1990[i])
            print(country[i]+" "+year_1990[i]+"  "+year_2010[i]+ " "+str(sub)) # function that reads drinking water file and prints out


def main():
    print("Country         1990    2010   Change")
    # create dictionary mapping drinking water filtered to country
    popDict = makePopDictionary()
    # readDWdata
    readDWdata(popDict)

main()


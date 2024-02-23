'''def weather(rain,snow):
    if (rain=="Yes" or snow=="Yes"):
        return "True"
rain = input("Is it raining ?")
snow = input("Is it Snowing ?")
print(weather(rain,snow))'''

'''isRain = input("Is it Raining or Not").lower()
isSnow = input("is it snowing or not").lower()

print(f"{isRain},{isSnow}")

if(isSnow=="yes"or isRain=="yes"):
    print("True")'''

def getInput(weather):
    while True:
        data = input(f"Enter yes or no {weather}")
        if data == "yes" or data == "no":
            return data
rain = getInput("raining")
snow = getInput("snowing")

if snow == "yes" or rain == "yes":
    print("True")
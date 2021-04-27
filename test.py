from naverWeather import *

print("<오늘의 날씨>")
print(naverWeather('서울').getWeather())

while True:  
    print("날씨를 알고 싶은 도시명을 입력하세요(ex: 서울, 제주) : ", end="")

    city = input()
    if city == "stop":
        break
    if city not in naverWeather.map_cityNum:
        print("잘못된 도시명입니다.")
        continue
    naverWeather(city).getWeather()

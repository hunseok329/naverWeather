from naverWeather import *
# l = naverWeather.map_cityNum.keys()


print("날씨를 알고 싶은 도시명을 입력하세요(ex: 서울, 제주) : ", end="")
city = input()
print(naverWeather(city).getWeather())
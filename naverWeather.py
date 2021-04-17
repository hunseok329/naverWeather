import requests
from bs4 import BeautifulSoup
import re

class naverWeather():
    session = requests.Session() 
    # 예전 url 주소
    # addr = "http://weather.naver.com/rgn/cityWetrCity.nhn?cityRgnCd=CT"
    addr = "https://weather.naver.com/today/"
    map_cityNum = {     # 지역 번호 매핑
            '가평':"02820250", '강화':"11710250", '고양':"02281621", '과천':'02290107','광명':"02210610" , 
            '광주':"02610103", '구리':"02310541", '군포':"02410510", '김포':"02570106", '남양주':"02360103",
            '동두천':"02250510", '문산':"02480250", '부천':"02190108", '서울':"09140550", '성남':'02133101',
            '수원':"02133101", '시흥':"02390630", '안산':"02273107", '안성':'02550510',
            '안양':"02171101", '양주':"02630510", '양평':"02830250", '여주':"02670510", '연천':"02800250", 
            '오산':"02370510", '용인':"02463102", '의왕':"02430101", '의정부':"0215020", '이천':"02500103", 
            '인천':"11200510", '파주':"02480510", '평택':"02220630", '포천':"02650510", '하남':"02450530", '화성':"02590262",

            '백령도':"11720330", '연평도':"11720380",

            '양구':"01800250", '영월':"01750250", '원주':"01130115", '인제':"01810250", '정선':"01770250", 
            '철원':"01780256", '춘천':"01110580", '평창':"01760250", '홍천':"01720250", '화천':"01790250", 
            '횡성':"01730250",
            
            '강릉':"01150101", '강원':"01810350", '고성':"01820250", '대관령':"01760380", 
            '동해':"01170101", '삼척':"01230106", '속초':"01210103", '양양':"01830250", 
            '태백':"01190540",

            '괴산':"16760250", '남이':"15710360", '단양':"16800250", '보은':"16720250", '영동':"16740250", 
            '옥천':"16730250", '음성':"16770250", '제천':"16150547", '증평':"16745250", '진천':"16750250", 
            '청원':"16114101", '청주':"16111102", '추풍령':"16740335", '충주':"16130625",

            '계룡':"15250101", '공주':"15150102", '금산':"15710250", '논산':"15230109", '당진':"15270510", 
            '대전':"07170630", '보령':"15180545", '부여':"15760250", '서산':"15210510", '서천':"15770253", 
            '세종':"17110250", '아산':"15200600", '예산':"15810250", '천안':"15133253", '청양':"15790250", 
            '태안':"15825250", '홍성':"15800250",

            '경산':"04290520", '경주':"04130126", '고령':"04830253", '구미':"04190110", '군위':"04720250", 
            '김천':"04150575", '대구':"06110517", '문경':"04280610", '봉화':"04920250", '상주':"04250520", 
            '성주':"04840250", '안동':"04170104", '영덕':"04770250", '영양':"04760250", '영주':"04210600", 
            '영천':"04230520", '예천':"04900250", '울진':"04960250", '의성':"04730250", '청도':"04820250", 
            '청송':"04750250", '칠곡':"04850250", '포항':"04113119",

            '거제':"03310109", '거창':"03880250", '고성':"03820250", '김해':"03250103", '남해':"03840250", 
            '밀양':"03270103", '부산':"08470690", '사천':"03240330", '산청':"03860250", '서상':"03250102", 
            '양산':"03330510", '울산':"10140510", '의령':"03720250", '진주':"03710119", '창녕':"03740250", 
            '창원':"03129144", '통영':"03220111", '하동':"03850250", '함안':"03730250", 
            '함양':"03870250", '합천':"03890250",

            '독도':"04940250", '울릉도':"04940250",

            '고창':"13790250", '군산':"13130134", '김제':"13210107", '남원':"13190116", '무주':"13730250", 
            '부안':"13800250", '순창':"13770250", '완주':"13710360", '익산':"13140113", '임실':"13750250", 
            '장수':"13740250", '전주':"13113102", '정읍':"13180101", '진안':"13720250",

            '강진':"12810250", '고흥':"12770250", '곡성':"12720250", '광양':"12230530", '광주':"05140120", 
            '구례':"12730250", '나주':"12170102", '담양':"12710250", '목포':"12110510", '무안':"12840250", 
            '보성':"12780250", '순천':"12150119", '신안':"12910253", '여수':"12130780", '영광':"12870250", 
            '영암':"12830250", '완도':"12890250", '장성':"12880250", '장흥':"12800250", '진도':"12900250", 
            '함평':"12860250", '해남':"12820250", '화순':"12790250", '흑산도':"12910360",

            '서귀포':"14130590", '제주':"14110104"
            }

    def __init__(self, area):
        self.area = area
        self.addr = None
        self.result = None

        # 잘못된 도시명을 입력한 경우
        # if self.area not in naverWeather.map_cityNum: 
        #     return
        cityNum = naverWeather.map_cityNum[area]
        # if not cityNum:
        #     print("도시명 잘못")
        #     # 잘못된 도시명을 입력한 경우
        #     return
        self.addr = naverWeather.addr + cityNum
        
        self.search()

    def search(self):
        naverWeather.session.encoding = 'utf-8'

        req = naverWeather.session.get(self.addr)
        print(self.addr)
        soup = BeautifulSoup(req.text, "html.parser")
        location = soup.find(class_='location_name')
        table = soup.find(class_="week_list")
        print(location)
        # print(list(table.stripped_strings))
        t_ary = list(table.stripped_strings)

        self.result = ("[" + self.area + " 날씨 검색 결과]\n"
                    + "- 오늘(" + t_ary[1] +")\n"
                    + " \t 오전 - " + t_ary[11][:-1] + "℃ (" + t_ary[5] + ", 강수확률 : " + t_ary[4] + ")\n"
                    + " \t 오후 - " + t_ary[14][:-1] + "℃ (" + t_ary[9] + ", 강수확률 : " + t_ary[8] + ")\n"
                    + "- 내일(" + t_ary[16] + ")\n"
                    + " \t 오전 - " + t_ary[26][:-1] + "℃ (" + t_ary[20] + ", 강수확률 : " + t_ary[19] + ")\n"
                    + " \t 오후 - " + t_ary[29][:-1] + "℃ (" + t_ary[24] + ", 강수확률 : " + t_ary[23] + ")\n")


    def getWeather(self):
        if not self.result:
            # 도시명을 잘못 입력한 경우 결과가 나오지 않는다.
            return "잘못된 도시명입니다"
        return self.result

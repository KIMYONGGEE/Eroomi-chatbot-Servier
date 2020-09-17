from bs4 import BeautifulSoup
import requests
from flask import Flask, request, jsonify
import sys
app = Flask(__name__)

@app.route('/test/')
def test():
    return "data"

@app.route('/message', methods=['POST'])
def Message():
   
    main_url = "https://software.cbnu.ac.kr/bbs/bbs.php?db=notice"
    res = requests.get(main_url)
    soup = BeautifulSoup(res.content,'html.parser')
    size = len(soup.find_all('b'))
    tag_list = soup.find_all('b')
   
#url 출력부분
    #for a in range(size):
    """
    print(soup.find_all('b')[0])
    print("===========")
    print(soup.find_all('b')[0].parent)
    print("===========")
    print(soup.find_all('b')[0].parent.parent)
    print("===========")
    print(soup.find_all('b')[0].parent.parent.get('href'))
    """
   
    url_result0 = 'https://software.cbnu.ac.kr/' + soup.find_all('b')[0].parent.parent.get('href')
    first_list0 = soup.find_all('b')[0].text.strip();
    #text_result = soup
   
    """print("===========")
    print(url_result0)
    print("===========")
    print(first_list0)
    """
   
    url_result1 = 'https://software.cbnu.ac.kr/' + soup.find_all('b')[1].parent.parent.get('href')
    first_list1 = soup.find_all('b')[1].text.strip();
   
    url_result2 = 'https://software.cbnu.ac.kr/' + soup.find_all('b')[2].parent.parent.get('href')
    first_list2 = soup.find_all('b')[2].text.strip();

    url_result3 = 'https://software.cbnu.ac.kr/' + soup.find_all('b')[3].parent.parent.get('href')
    first_list3 = soup.find_all('b')[3].text.strip();
   
    url_result4 = 'https://software.cbnu.ac.kr/' + soup.find_all('b')[4].parent.parent.get('href')
    first_list4 = soup.find_all('b')[4].text.strip();
   

    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']
   
    if content == u"공지사항" or content == u"공지사항 보여줘" or content == u"공지사항 말해봐" or content == u"공지사항 알려줘":
        print("공지사항 동작")
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "첫번째 공지사항입니다. \n\n" + first_list0 +"\n\n"+ url_result0 + "\n\n==================\n\n" + "두번째 공지사항입니다. \n\n" + first_list1 +"\n\n"+ url_result1 + "\n\n==================\n\n" + "세번째 공지사항입니다. \n\n" + first_list2 +"\n\n"+ url_result2 + "\n\n==================\n\n" + "네번째 공지사항입니다. \n\n" + first_list3 +"\n\n"+ url_result3 + "\n\n==================\n\n" + "다섯번째 공지사항입니다. \n\n" + first_list4 +"\n\n"+ url_result4 + "\n\n==================\n\n"
                        }
                    }
                ]
            }
        }
    elif content == u"이루미란?":
        print("이루미란? 동작")
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "충북대학교 소프트웨어학과의 공지사항을 빠르게 알려주는 채팅봇입니다. \n\n'공지사항'이라고 말해주세요."
                        }
                    }
                ]
            }
        }   
       
    elif content == u"어떻게 사용하나요?":
        print("how to use? 동작")
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "충북대학교 소프트웨어학과의 최근 공지사항 5개를 빠르게 검색하여 보여줍니다. \n\n '공지사항' 이라고 말해주세요."
                        }
                    }
                ]
            }
        }
    elif content == u"안녕" or content == u"누구야" or content == u"안녕하세요" or content == u"누구세요" or content == u"하이":
        print("인사 동작")
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "안녕하세요! 이루미입니다~~"
                        }
                    }
                ]
            }
        }
    elif content == u"야" or content == u"오":
        print("농담 동작")
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "ㅇuㅇ?"
                        }
                    }
                ]
            }
        }
       
       
    else :
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "'공지사항'이라고 말해주세요"
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)



if __name__ == "__main__":
    app.run(host='0.0.0.0')
'''
2. 다음 연습문제에서는 파이썬의 calendar 모듈을 활용한다.

    a) 파이썬 문서화 웹사이트( http://docs.python.org/2.7/py-modindex.html, 2.7 버젼 ) 을 방문해 calendar 모듈에 관한 내용을 찾아보라.

    b) Calendar 모듈을 가져오라

    c) isleap 함수의 설명을 읽어 보고, 이 함수를 사용해 내년이 윤년인지 확인하라.

    d) calendar 모듈에 있는 함수를 이용해 2000년에서 2050년 사이에 윤년이 얼마나 있는지 확인하라.

    e) calendar 모듈에 있는 함수를 이용해 2016년 7월 29일이 무슨 요일인지 확인하라.
'''
import calendar

calendar.isleap(2023)

calendar.leapdays(2000, 2050)

calendar.weekday(2016, 7, 29)

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("실수로 변환 성공")
    finally:
        print("문자열은 실수 변환이 불가능합니다!")

movie_data = {
    "1917": [15, 'A'],
    "무간도": [12, 'B'],
    "타짜": [18, 'A'],
    "스폰지밥 극장판": [0, 'B'],
}

people_data = [0, 0, 0]

menu_string = (
    "=============================================\n"
    "1. 영화 예매\n"
    "2. 프로그램 종료\n"
    "=============================================\n"
    "원하시는 메뉴를 선택해 주세요: "
)

movie_string = (
    "=============================================\n"
    "1.    1917    /  15세 관람가   / A관\n"
    "2.    무간도     /  12세 관람가   / B관\n"
    "3.     타짜     /  18세 관람가   / A관\n"
    "4.  스폰지밥 극장판  /   전체 이용가   / B관\n"
    "=============================================\n"
    "관람하실 영화를 선택해 주세요: "
)

time_string = (
    "===========================================\n"
    "1.   9:50    0 / 140\n"
    "2.  18:00    0 / 140\n"
    "3.  21:15    0 / 140\n"
    "=============================================\n"
    "관람하실 시간을 선택해 주세요: "
)

# the app logic begins here

menu = int(input(menu_string))

if menu == 1:
    movie = int(input(movie_string))

    time = int(input(time_string))

    ages = []
    count = int(input("몇 분이 오셨습니까?"))
    if count <= 10: people_data[0] = people_data[0] + 1

    for i in range(count):
        ages.append(int(input('나이는?')))

    print('    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 ')
    column = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    for alphabet in range(len(column)):
        print(column[alphabet], end='   ')

        for seat in range(1, 21):
            print('.', end='  ')

        print()

    seats = []
    for ages in range(len(ages)):
        seatHorizontal = input("{0}번째 관객분의 행을 선택해 주세요 (알파벳): ".format(ages + 1))
        seatVertical = input("{0}번째 관객분의 좌석번호를 선택해 주세요 (숫자): ".format(ages + 1))

        seats.append("{0}{1}".format(seatHorizontal[ages], seatVertical[ages]))
        print('지정했습니다.')

    print(
        "=============================================\n"
        "총 인원 : {0}명, (어린이 {1}명, 청소년 {2}명, 성인 {3}명)".format(
            len(seats), people_data[0], people_data[1], people_data[2]
        )
    )
    print()
    print(
        "총 금액 : {0}원                 \n"
        "=============================================\n"
        "{1}\n"
        "=============================================\n".format(
            (5000 * people_data[0])
            + (9000 * people_data[1])
            + (11000 * people_data[2]),
            seats[0]
        )
    )

    print_receipt = input("예매표를 출력하시겠습니까? (Y/N)")
    if print_receipt == 'y' or print_receipt == 'Y':
        print('예매표가 receipt.txt에 저장되었습니다.')
        print('사용해 주셔서 감사합니다.')

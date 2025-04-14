if __name__=='__main__':
  
    ### 사용자 입력
    print('\n첫번째 숫자를 입력하세요.')
    input1 = (input('입력: '))

    print('\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /)')
    act = input('기호: ')

    print('\n두번째 숫자를 입력하세요.')
    input2 = (input('입력: '))

    ### 숫자 변환
    try:
        input1 = float(input1)
        input2 = float(input2)
    except ValueError:
        print('\n잘못된 숫자입니다.')
        exit()

    ### 사칙연산 기호 확인
    if act not in ['+', '-', '*', '/']:
        print('\n잘못된 기호입니다.')
        exit()

    ###연산 수행
    if act == '+':
        result = (input1 + input2)
    elif act == '-':
        result = (input1 - input2)
    elif act == '*':
        result = (input1 * input2)
    elif act == '/':
        try:
            result = (input1 / input2)
        except ZeroDivisionError:
            print('\n0으로 나눌 수 없습니다.')
            exit()
    print(f'\n\n사칙연산 결과는 {result}입니다.')
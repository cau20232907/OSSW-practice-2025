if __name__=='__main__':
  
  ### 사용자 입력
  print('\n첫번째 숫자를 입력하세요.')
  input1 = int(input('입력: '))
  
  print('\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /)')
  act = input('기호: ')
  
  print('\n두번째 숫자를 입력하세요.')
  input2 = int(input('입력: '))
  

  ###연산 수행
  if act == '+':
    result = (input1 + input2)
  elif act == '-':
    result = (input1 - input2)
  elif act == '*':
    result = (input1 * input2)
  elif act == '/':
    result = (input1 / input2)
  print(f'사칙연산 결과는 {result}입니다.')

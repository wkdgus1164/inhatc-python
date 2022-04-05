# age = int(input('나이는?'))
# price = 0
#
# if age < 8:
#     price = 5000
# elif age < 19:
#     price = 9000
# elif age >= 19:
#     price = 11000
# else:
#     print('정확한 나이를 입력해주세요!')
#
# print('요금은' + str(price) + '원 입니다.')

#############################

# options = ['콜라', '치즈토핑', '버섯', '치즈크러스터']
#
# if '버섯' in options:
#     print('버섯을 추가합니다')
# if '페퍼로니' in options:
#     print('페퍼로니를 추가합니다')
# if '치즈토핑' in options:
#     print('치즈토핑을 추가합니다')
#
# print('\n피자 주문이 완료 됐습니다~')

# 버섯을 추가합니다
# 치즈토핑을 추가합니다
#
# 피자 주문이 완료 됐습니다~

#################################

# for i in range(5):  # 인수가 하나일 때는 시간 값은 0부터, 시작 5전까지
#     print(i, end=' ')
# print()
# for j in range(2, 5):  # 2는 시작 값, 5는 끝값 + 1
#     print(j, end=' ')
# for k in range(1, 6, 2):  # 1은 시작 값, 6은 끝값 + 1, 증감 step
#     print(k, end=' ')

# 0 1 2 3 4
# 2 3 4 1 3 5

######################################

# for n in range(5, 11):
#     print(n)

# 5
# 6
# 7
# 8
# 9
# 10

####################################

# for n in range(2, 11, 2):
#     print(n)

# 2
# 4
# 6
# 8
# 10

##################################

# for n in range(1, 11):
#     if n % 2 == 0:
#         print(n)

# 2
# 4
# 6
# 8
# 10

#################################

# for n in range(10, 1, -1):
#     print(n)

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2

#################################

# words = 'I love python'
# for word in words:
#     print(word)

# I
#
# l
# o
# v
# e
#
# p
# y
# t
# h
# o
# n

####################################

# words = ['I', 'love', 'python']
# for word in words:
#     print(word)

# I
# love
# python

#####################################

# words = ['I', 'love', 'python']
# for i in range(3):
#     print(words[i])

# I
# love
# python

#################################

# words = ['I', 'love', 'python']
# for word in words:
#     print(word, end=' ')

# I love python

#################################

# words = ['I', 'love', 'python']
# for i in range(len(words)):
#     print(words[i], end=' ')

# I love python

# numbers = []
# for k in range(0, 10, 2):
#     numbers.append(k * k)
# print(numbers)

# [0, 4, 16, 36, 64]

#######################################

# numbers = [k * k for k in range(0, 10, 2)]
# print(numbers)

# [0, 4, 16, 36, 64]

###########################################

# n = []
# for x in range(1, 11):
#     if x % 3 == 0:
#         n.append(x)
# print(n)

# [3, 6, 9]

##############################################

# artists = ['악뮤', '빅뱅', '볼사', '릴러말즈']
# copy_artists = [artist for artist in artists if artist != '빅뱅']
# print(artists)
# print(copy_artists)

# ['악뮤', '빅뱅', '볼사', '릴러말즈']
# ['악뮤', '볼사', '릴러말즈']

###############################################

# import random

# dice = random.randint(1, 6)
# print(dice)

# 5

##################################################

# import random
#
# lotto = []
# while (len(lotto) < 6):
#     lotto.append(random.randint(1, 45))
#     lotto = list(set(lotto))
# print(lotto)

# [1, 37, 13, 14, 18, 24]

#################################################

# fruits = {'apple': '사과', 'watermelon': '수박'}
# print(fruits['watermelon'])
# print(fruits)
# fruits['kiwi'] = '키위'
# print(fruits)

# 수박
# {'apple': '사과', 'watermelon': '수박'}
# {'apple': '사과', 'watermelon': '수박', 'kiwi': '키위'}

######################################################
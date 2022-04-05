# subjects = ['english', 'python', 'java']

# 리스트 인덱스 삭제
# print(subjects.remove('python')) # None

# 리스트 인덱스 삭제할 것 출력
# print(subjects.pop(1)) # python
# print(subjects) # ['english', 'java']

# 리스트 항목 인덱스 반환
# print(subjects.index('java')) # 2

# 리스트에 항목 추가
# subjects.append('java') # ['english', 'python', 'java', 'java']

# 배열 길이
# print(len(subjects)) # 3

# 리스트에 특정 인덱스에 항목 추가
# subjects.insert(0, 'python')  # ['python', 'english', 'python', 'java']

# 리스트를 문자열로 변환 [구분자]
# subjects_string = '/'.join(subjects) # english/python/java

# 문자열을 리스트로 변환
# subjects_lists = subjects_string.split('/') # ['english', 'python', 'java']

# 리스트 원소 정렬 (오름차순 사전순)
# subjects.sort() # ['english', 'java', 'python']

# 리스트 원소 정렬 (내림차순 사전순)
# subjects.sort(reverse=True) # ['python', 'java', 'english']

# 배열의 원소 정렬
# list_a = [2, 3, 1] # [2, 3, 1]
# list_copy = sorted(list_a) # [1, 2, 3]

####################################

# my_utube = ['약뮤', '볼사', '코노', '언더독', '홍길동', '아이유', '소녀시대', '씨스타']

# 리스트 0~5 인덱스 찾기
# ur_utube = my_utube[0:5]  # ['약뮤', '볼사', '코노', '언더독', '홍길동']
# ur_utube = my_utube[-4:-1] # ['홍길동', '아이유', '소녀시대']

# 리스트 뒤에서 첫 번째 삭제
# del my_utube[-1] # ['약뮤', '볼사', '코노', '언더독', '홍길동', '아이유', '소녀시대']

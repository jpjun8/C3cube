import csv

f = open("accident.csv", encoding = "cp949")
data = csv.reader(f)

next(data)
i, j = 0, 0
days = []
days_sum = [0] * 7

"""요일별 총 '사고건수' 구하기"""
for row in data:
  # row[2:]를 정수로 변환 후 저장하기
  row[2:] = map(int, row[2:])

  # '사고건수'의 누적합을 해당하는 요일의 인덱스에 저장하기
  print(days_sum[i % 7], i % 7, row[2])
  days_sum[i % 7] += row[2]

  i += 1

  # days 리스트에 요일 저장하기
  if j < 7:
    days.append(row[1])
    j += 1

mx = days_sum[0]
mx_day = ''

"""교통사고가 가장 많이 나는 날 찾기"""
for i in range(1, len(days_sum)):
  # days_sum 리스트의 요소 중 최댓값 찾기
  if mx < days_sum[i]:
    mx = days_sum[i]
    mx_day = days[i]

for i in range(7):
  print(days[i], ':', days_sum[i])

print("교통사고가 가장 많이 나는 날은 " + mx_day + "요일입니다.")
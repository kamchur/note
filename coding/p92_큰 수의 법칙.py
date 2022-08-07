'''큰 수의 법칙

최대값 구하기
n번 더하고, m번까지 연속된 수를 더할 수 있음
'''

# n, m = map(int, input().split())
n, m = 8, 3

arr = [2, 4, 5, 4, 6]
arr.sort()

arr1 = arr[-1]
arr2 = arr[-2]

sum = ((n//m) * m * arr1) + ((n%m) * arr2)

print(sum)
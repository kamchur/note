n = 5
m = 'RRRUDD'

# 지도 5x5 : 지도가 필요없네?
# map = [[x, y] for x in range(1,6) for y in range(1,6)]

man = [1, 1]

d = list('LRUD')
mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

for i in m:
    move = d.index(i)

    m_x = man[0] + mx[move]
    m_y = man[1] + my[move]

    if m_x < 1 or m_x > 5 and m_y < 1 or m_y > 5:
        continue

    man = [m_x, m_y]

# x, y좌표 처럼 생각하여 풀이
print(man[1], man[0])
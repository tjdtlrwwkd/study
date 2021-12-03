# 6051
a, b = map(int, input().split())

if a != b:
    print(True)
else:
    print(False)

# 6052
n = int(input())

if n:
    print(True)
else:
    print(False)

# 6053
n = int(input())
if bool(n):
    print(False)
else:
    print(True)

# 6054
a, b = map(int, input().split())

if a and b:
    print(True)
else:
    print(False)

# 6055
a, b = map(int, input().split())

if a or b:
    print(True)
else:
    print(False)

# 6056
a, b = map(int, input().split())

if bool(a) != bool(b):
    print(True)
else:
    print(False)

# 6057
a, b = map(int, input().split())

if bool(a) and bool(b):
    print(True)
else:
    print(False)

# 6058
a, b = map(int, input().split())

if (bool(a) == False) and (bool(b) == False): 
    print(True)
else:
    print(False)

# 6059
n = int(input())
print(~n)

# 6060
a, b = map(int, input().split())

print(a & b)

# 6061
a, b = map(int, input().split())

print(a | b)

# 6062
a, b = map(int, input().split())

print(a ^ b)

# 6063
a, b = map(int, input().split())

li = [a, b]
print(max(li))

# 6064
li = list(map(int, input().split()))

print(min(li))

# 6065
li = list(map(int, input().split()))
for n in li:
    if n % 2 == 0:
        print(n)

# 6066
li = list(map(int, input().split()))
for n in li:
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

# 6067
n = int(input())

if n < 0 and n % 2 == 0:
    print('A')
elif n < 0 and n % 2:
    print('B')
elif n > 0 and n % 2 == 0:
    print('C')
elif n > 0 and n % 2:
    print('D')

# 6068
n = int(input())

if n >= 90:
    print('A')
elif n >= 70:
    print('B')
elif n >= 40:
    print('C')
else:
    print('D')

# 6069
c = input()

if c == 'A':
    print("best!!!")
elif c == 'B':
    print("good!!")
elif c == 'C':
    print("run!")
elif c == 'D':
    print("slowly~")
else:
    print("what?")

# 6070
n = int(input())

if n // 3 == 1:
    print("spring")
elif n // 3 == 2:
    print("summer")
elif n // 3 == 3:
    print("fall")
else:
    print("winter")

# 6071
while True:
    n = int(input())
    if n == 0:
        break
    print(n)

# 6072
n = int(input())

for i in reversed(range(1, n+1)):
    print(i)

# 6073
n = int(input())

for i in reversed(range(n)):
    print(i)

# 6074
c = input()

for i in range(ord('a'), ord(c)+1):
    print(chr(i), end=" ")

# pass
# 6075
# 6076

# 6077
n = int(input())
sum_num = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum_num += i
print(sum_num)

# 6078
while True:
    c = input()
    print(c)
    if c == 'q':
        break

# 6079
n = int(input())
sum_num = 0
cnt = 1
while True:
    sum_num += cnt
    if sum_num >= n:
        break
    cnt += 1
print(cnt)

# 6080
n, m = map(int, input().split())
for i in range(1, n):
    for j in range(1, m):
        print(i, j)

# 6081
h = input()
for i in range(15):
    print(f'{h}*{hex(i+1).replace("0x", "").upper()}=', end="")
    print(hex(int(h, 16) * (i + 1)).replace("0x", "").upper())

# 6082
n = int(input())

check_cnt = 0
sog = ('3', '6', '9')
for i in range(1, n + 1):
    for c in str(i):
        if c in sog:
            check_cnt += 1
    if check_cnt >= 1:
        print('X' * check_cnt, end=" ")
    else:
        print(i, end=" ")
    check_cnt = 0

# 6083
r, g, b = map(int, input().split())
cnt = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
                print(i, j, k)
                cnt += 1

print(cnt)

# 6084
h, b, c, s = map(int, input().split())
file_size = h * b * c * s / 8 / 1024 / 1024
file_size = round(file_size, 1)
print(f"{file_size} MB")

# 6085
w, h, b = map(int, input().split())
file_size = w * h * b / 8 / 1024 / 1024
file_size = format(round(file_size, 2), ".2f")
print(f'{file_size} MB')

# 6086
n = int(input())
num = 1
sum_num = 0
while True:
    sum_num += num
    if sum_num >= n:
        break
    num += 1

print(sum_num)

# 6087
n = int(input())

for i in range(1, n+1):
    if i % 3:
        print(i, end=" ")

# 6088
a, d, n = map(int, input().split())

for i in range(n-1):
    a += d

print(a)

# 6089
a, r, n = map(int, input().split())

for i in range(n-1):
    a *= r

print(a)

# 6090
a, m, d, n = map(int, input().split())

for i in range(n-1):
    a *= m
    a += d

print(a)

# 6091
a, b, c = map(int, input().split())

d = 1

while True:
    if d % a == 0 and d % b == 0 and d % c == 0:
        break
    d += 1

print(d)

# 6092
n = int(input())
num_list = list(map(int, input().split()))
student_list = [0 for x in range(23)]

for i in num_list:
    student_list[i-1] += 1

str_student_list = list(map(str, student_list))
print(" ".join(str_student_list))

# 6093
n = int(input())
num_list = list(map(int, input().split()))

print(" ".join(list(map(str, list(reversed(num_list))))))

# 6094
n = int(input())
num_list = list(map(int, input().split()))

print(min(num_list))

# 6095
n = 19
board = [[0]*n for _ in range(n)]

loop_cnt = int(input())
for i in range(loop_cnt):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1

for i in range(len(board)):
    board[i] = list(map(str, board[i]))
    print(" ".join(board[i]))

# 6096
def matrix2x2(size):
    arr = []
    for i in range(size):
        arr.append(list(map(int, input().split())))

    return arr

def reversed_matrix(board, coordinate_list):
    for i in range(len(coordinate_list)):
        row = coordinate_list[i][0]
        for j in range(len(board)):
            if board[row-1][j] == 1:
                board[row-1][j] = 0
            else:
                board[row-1][j] = 1

        col = coordinate_list[i][1]
        for k in range(len(board[row-1])):
            if board[k][col-1] == 1:
                board[k][col-1] = 0
            else:
                board[k][col-1] = 1
    return board

n = 19

board = matrix2x2(n)
input_cnt = int(input())
coordinate_list = matrix2x2(input_cnt)
reversed_board = reversed_matrix(board, coordinate_list)

for i in range(len(reversed_board)):
    for j in range(len(reversed_board[i])):
        print(reversed_board[i][j], end=" ")
    print()

# 6097
def board_make(n, m):
    board = [[0] * m for _ in range(n)]

    return board

def matrix_make(loop_cnt):
    arr = []
    for i in range(loop_cnt):
        arr.append(list(map(int, input().split())))
    
    return arr

def matrix_convert(board, block_list, loop_cnt):
    for i in range(loop_cnt):
        block_size = block_list[i][0]
        dir = block_list[i][1]
        row = block_list[i][2] - 1
        col = block_list[i][3] - 1

        for i in range(block_size):
            if dir:
                board[row+i][col] = 1
            else:
                board[row][col+i] = 1
    
    return board

def matrix_print(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()

n, m = map(int, input().split())
board = board_make(n, m)
loop_cnt = int(input())
block_list = matrix_make(loop_cnt)
res = matrix_convert(board, block_list, loop_cnt)
matrix_print(res)

# 6098
def make_world(size):
    world = []
    for i in range(size):
        world.append(list(map(int, input().split())))

    return world

def matrix_print(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()

map_size = 10

world = make_world(10)
pose_x, pose_y = 1, 1
feed = 2

while True:
    # print(pose_x, pose_y)
    if pose_x >= map_size-1 or pose_y >= map_size-1:
        # print("away from the map")
        break
    
    elif world[pose_y][pose_x] == feed:
        world[pose_y][pose_x] = 9
        # print("find feed")
        break
    
    else:
        if world[pose_y][pose_x + 1] == 0 or world[pose_y][pose_x + 1] == 2:
            world[pose_y][pose_x] = 9
            pose_x += 1

        else:
            world[pose_y][pose_x] = 9
            pose_y += 1
            
matrix_print(world)
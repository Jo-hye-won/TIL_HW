import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'E0001_1053713'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 5  # 5개의 공
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for _ in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:
    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been corrupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    # Calculate angle and power
    white_ball_x, white_ball_y = balls[0][0], balls[0][1]
    target_ball_x, target_ball_y = balls[1][0], balls[1][1]
    fourth_ball_x, fourth_ball_y = balls[3][0], balls[3][1]

    # Calculate the angle and power for the fourth ball
    if order == 1:
        target_ball_x, target_ball_y = fourth_ball_x, fourth_ball_y

    width = abs(target_ball_x - white_ball_x)
    height = abs(target_ball_y - white_ball_y)
    radian = math.atan(width / height) if height > 0 else 0
    angle = 180 / math.pi * radian

    if white_ball_x == target_ball_x:
        if white_ball_y < target_ball_y:
            angle = 0
        else:
            angle = 180
    elif white_ball_y == target_ball_y:
        if white_ball_x < target_ball_x:
            angle = 90
        else:
            angle = 270

    if white_ball_x < target_ball_x and white_ball_y < target_ball_y:
        radian = math.atan(height / width)
        angle = (90 - (180 / math.pi * radian))
        if white_ball_x > fourth_ball_x and white_ball_y < fourth_ball_y:
            radian = math.atan(width / height)
            angle = (90 - (180 / math.pi * radian)) + 270
        elif white_ball_x < fourth_ball_x and white_ball_y < fourth_ball_y:
            radian = math.atan(width / height)
            angle = (90 - (180 / math.pi * radian))
    elif white_ball_x > target_ball_x and white_ball_y < target_ball_y:
        radian = math.atan(width / height)
        angle = (90 - (180 / math.pi * radian)) + 270
    elif white_ball_x > target_ball_x and white_ball_y > target_ball_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 180
    elif white_ball_x < target_ball_x and white_ball_y > target_ball_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 90

    distance = math.sqrt(width ** 2 + height ** 2)
    power = min(distance * 0.5, 100)  # Ensure power is not greater than 100

    # Send angle and power
    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')
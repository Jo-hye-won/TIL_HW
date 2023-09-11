import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'E0001_1052364'

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
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

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
        print("Received Data has been currupted, Resend Requested.")
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

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.
    # 선순위 일때, 후순위 일 때
    # 흰공
    start = balls[0]

    diameter = 5.73

    # 선공 선택
    if order == 1:  # 홀수 번째
        ball_1 = 1
    else:  # 짝수 번째
        ball_1 = 2

    # 가까운 목적구 선택
    ball = None
    distance_b = int(1e9)
    for i in range(ball_1, 5, 2):
        if balls[i][0] == -1:  # 이미 친 공일 때
            continue
        d_goal = [balls[i][0] - start[0], balls[i][1] - start[1]]
        dis_g = (d_goal[0] ** 2 + d_goal[1] ** 2) ** 0.5
        if dis_g < distance_b:
            distance_b = dis_g
            ball = balls[i]  # 목적구 선택

    # 목적구를 다 쳤을 때 8번공[5] 지정
    if ball is None:
        ball = balls[5]

    # print(ball)

    # 목적구와 가까운 홀 지정
    end = None
    distance_h = int(1e9)
    for j in range(6):
        d_hole = [HOLES[j][0] - ball[0], HOLES[j][1] - ball[1]]
        dis_h = (d_hole[0] ** 2 + d_hole[1] ** 2) ** 0.5
        if dis_h < distance_h:
            distance_h = dis_h
            end = HOLES[j]

    # a, b, c 지정
    a = [end[0] - start[0], end[1] - start[1]]  # 흰공에서 홀까지 좌표
    b = [end[0] - ball[0], end[1] - ball[1]]  # 목적구에서 홀까지 좌표
    c = [ball[0] - start[0], ball[1] - start[1]]  # 흰공에서 목적구까지 좌표

    # b를 충돌지점으로 설정
    b = [b[0] + (b[0] * diameter / (b[0] ** 2 + b[1] ** 2) ** 0.5),
         b[1] + (b[1] * diameter / (b[0] ** 2 + b[1] ** 2) ** 0.5)]

    # c를 충돌지점으로 설정(c = a - b)
    c = [a[0] - b[0], a[1] - b[1]]

    # theta 구하기(math.atan() 사용)
    theta = math.atan(c[1] / c[0])

    # degrees
    theta = math.degrees(theta)

    # angle 구하기(90 - theta)
    angle = 90 - theta

    # 2, 3 사분면일 때(angle에 180 더해줌)
    if c[0] < 0:
        angle += 180

    # 흰공과 목적공의 거리 구하기
    distance_c = math.sqrt(c[0] ** 2 + c[1] ** 2)

    # power 지정
    power = distance_c * 0.5

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    #
    # 이 때 주의할 점은 power 는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')

import select, socket, sys, Queue
import motion
from naoqi import ALProxy
import socket
import select

robotIP = "192.168.1.14" 
#"192.168.1.14" --> nao IP
robotPort = 9559
motion = ALProxy("ALMotion", robotIP, robotPort)
posture = ALProxy("ALRobotPosture", robotIP, robotPort)
#tts = ALProxy("ALTextToSpeech", robotIP, robotPort)

if (posture.getPosture() == "Stand"):
    posture.goToPosture("Sit", 1.0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('', 6666))
server.listen(5)
inputs = [server]
outputs = []
message_queues = {}
message = ''

while inputs:
    readable, writable, exceptional = select.select(
        inputs, outputs, inputs)
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()
        else:
            message = s.recv(1024).decode()
            if message:
                message_queues[s].put(message)
                if s not in outputs:
                    outputs.append(s)
            else:
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    # for s in writable:
    #     try:
    #         next_msg = message_queues[s].get_nowait()
    #     except Queue.Empty:
    #         outputs.remove(s)
    #     else:
    #         s.send(next_msg)

    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]

    
    rightTurn = [0.0, 0.0, 0.40]
    leftTurn = [0.0, 0.0,  -0.40]
    walkForward = [0.8, 0.0, 0.0]
    standing = False

    if (message == "StandIsGo" and not standing):
        posture.goToPosture("StandInit", 1.0)
        standing = True
    elif (message == "WalkIsGo"):
        motion.move(walkForward[0], walkForward[1], walkForward[2])
    elif (message == "WalkIsStop"):
        motion.move(0, 0, 0.0)
    elif (message == "TurnRight"):
        print(message)
        motion.post.moveTo(rightTurn[0], rightTurn[1], rightTurn[2])
    elif (message == "TurnLeft"):
        print(message)
        motion.post.moveTo(leftTurn[0], leftTurn[1], leftTurn[2])
    elif (message == "Sit"):
        posture.goToPosture("Sit", 1.0)
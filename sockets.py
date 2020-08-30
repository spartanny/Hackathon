import socket
import cv2


def socketCall(gray, delta_frame, times):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 3000
    s.bind(("0.0.0.0", port))
    s.listen(5)
    c, addr = s.accept()
    t = "Alert actions required"
    c.send(t.encode())

    s.close()

    times.append(datetime.now())

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)

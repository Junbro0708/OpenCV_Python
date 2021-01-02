import cv2

capture = cv2.VideoCapture("video/star.mp4")

print(capture.get(cv2.CAP_PROP_FRAME_WIDTH), capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    # 현재 프레임 개수와 총 프레임 개수 비교
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.open("video/star.mp4")

    # 들여쓰기 매우 조심!
    ret, frame = capture.read()
    cv2.imshow("star", frame)

    if cv2.waitKey(33) > 0:
        break

capture.release()
cv2.destroyAllWindows()

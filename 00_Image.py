import cv2

# 이미지 읽기
img = cv2.imread('images/test.jpg', cv2.IMREAD_COLOR)

# 이미지 속성 확인
height, width, channel = img.shape
print(height, width, channel)

# 이미지 띄우기
cv2.imshow('Test Image', img)
cv2.waitKey(0)  # 키값을 주지 않으면 바로 켜졌다 꺼짐



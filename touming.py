import os
import cv2
import  numpy as np
# from find_light_mask import find_light_mask



def find_mask(frame, color):
    print(" def find_light_mask(frame, color): >>>")
    blackLower01 = np.array([0, 0, 0])  # 黑的阈值 标准H：0:180 S:0:255 V:0:46:220
    blackUpper01 = np.array([180, 255, 90])
    blackLower02 = np.array([0, 0, 46])  # 灰的阈值 标准H：0:180 S:0:43 V:0:46:220
    blackUpper02 = np.array([180, 43, 45])  # 灰色基本没用

    redLower01 = np.array([0, 43, 46])  # 红色的阈值 标准H：0-10 and 160-179 S:43:255 V:46:255
    redUpper01 = np.array([10, 255, 255])
    redLower02 = np.array([156, 43, 46])  # 125 to 156
    redUpper02 = np.array([180, 255, 255])

    greenLower = np.array([50, 43, 46])  # 绿色的阈值 标准H：35:77 S:43:255 V:46:255
    greenUpper = np.array([95, 255, 255])  # V 60 调整到了150

    blueLower = np.array([105, 120, 46])  # 蓝H:100:124 紫色H:125:155
    blueUpper = np.array([130, 255, 255])

    yellowLower = np.array([26, 43, 146])  # 黄色的阈值 标准H：26:34 S:43:255 V:46:255
    yellowUpper = np.array([34, 255, 255])  # 有的图 黄色变成红色的了
    try:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        red1_mask = cv2.inRange(hsv, redLower01, redUpper01)  # 根据阈值构建掩膜, 红色的两个区域
        red2_mask = cv2.inRange(hsv, redLower02, redUpper02)
        red_mask = red1_mask + red2_mask

        black01_mask = cv2.inRange(hsv, blackLower01, blackUpper01)  # 根据阈值构建掩膜,黑色的区域
        black02_mask = cv2.inRange(hsv, blackLower02, blackUpper02)  # 根据阈值构建掩膜,黑色的区域
        black_mask = black01_mask + black02_mask

        yellow_mask = cv2.inRange(hsv, yellowLower, yellowUpper)  # 根据阈值构建掩膜, 黄色的区域
        green_mask = cv2.inRange(hsv, greenLower, greenUpper)  # 根据阈值构建掩膜, 绿色的区域

        blue_mask = cv2.inRange(hsv, blueLower, blueUpper)
        if color == "black":
            mask = black_mask
        elif color == "yellow":
            mask = yellow_mask
        elif color == "red":
            mask = red_mask
        elif color == "green":
            mask = green_mask
        elif color == "blue":
            mask = blue_mask
        elif color == "red+blue":
            mask = red_mask + blue_mask
        elif color == "green+yellow":
            mask = green_mask + yellow_mask
        return mask
    except:
        return ""



work_dir = "C:\\Users\\young\\Desktop\\test1109\\before"

img_dir = "other"
save_dir = img_dir + "-after"


img_dir = os.path.join(work_dir, img_dir)
save_dir = os.path.join(work_dir, save_dir)

img_list = os.listdir(img_dir)
number = 0
for img in img_list:
    try:
        img_path = os.path.join(img_dir, img)
        frame = cv2.imread(img_path)
        # for color in ["yellow", ]:
        #     mask = find_light_mask(frame, color)
        #     BinColors = cv2.bitwise_and(frame, frame, mask=mask)  # 提取感兴趣的颜色区域  背景黑色+彩色的图像
        #

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        # cv2.imshow("image", image)
        # cv2.waitKey(0)
        cv2.imwrite(img_path, image)
    except:
        ""



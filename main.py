import cv2
import numpy as np

def apply_color_grading(image, grayscale):
    colored_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    colored_image = cv2.cvtColor(colored_image, cv2.COLOR_GRAY2RGB)
    colored_image = cv2.addWeighted(image, grayscale/255, colored_image, 1 - grayscale/255, 0)
    return colored_image

def draw_shape(image, shape_type, shape_color, shape_thickness):
    if shape_type == "矩形":
        cv2.rectangle(image, (100, 100), (200, 200), shape_color, shape_thickness)
    elif shape_type == "円":
        cv2.circle(image, (150, 150), 50, shape_color, shape_thickness)
    return image

def draw_with_pen(image, prev_x, prev_y, x, y, pen_color, pen_thickness):
    cv2.line(image, (prev_x, prev_y), (x, y), pen_color, pen_thickness)
    return image

def main():
    # 画像の読み込み
    image = cv2.imread("input_image.jpg")

    # カラーグレーディング
    grayscale = 100
    colored_image = apply_color_grading(image, grayscale)

    # 図形描画
    shape_type = "矩形"
    shape_color = (0, 0, 255)  # 赤色
    shape_thickness = 2
    colored_image = draw_shape(colored_image, shape_type, shape_color, shape_thickness)

    # ペンツール
    pen_color = (0, 255, 0)  # 緑色
    pen_thickness = 3
    drawing_mode = False
    prev_x, prev_y = -1, -1

    def draw(event, x, y, flags, param):
        nonlocal prev_x, prev_y, drawing_mode

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing_mode = True
            prev_x, prev_y = x, y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing_mode = False
        elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
            if drawing_mode:
                colored_image = draw_with_pen(colored_image, prev_x, prev_y, x, y, pen_color, pen_thickness)
                prev_x, prev_y = x, y

    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", draw)

    while True:
        cv2.imshow("Image", colored_image)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

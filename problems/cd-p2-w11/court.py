from tkinter import *

class Court :
  def __init__(self, window, width, height, img):
    # 캔버스 생성하기
    self.canvas = Canvas(window, width = width, height = height)

    # 경기장 이미지 생성하기
    self.img = PhotoImage(file = img)
    self.canvas.create_image(width/2, height/2, image = self.img)

    # 경기장의 가로, 세로 길이 초기화하기
    self.width = width
    self.height = height

    # 캔버스 배치하기
    self.canvas.pack()


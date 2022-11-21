from tkinter import *

class Ball:
  def __init__(self, court, x1, y1, x2, y2):
    # 공의 좌표 초기화하기
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2

    # 공의 이동 거리 초기화하기
    self.x_dist = 10
    self.y_dist = 10

    # 공의 가로, 세로 길이 초기화하기
    self.width = x2 - x1
    self.height = y2 - y1

    # Court 클래스 객체 저장하기
    self.court = court

    # Court 클래스 객체 저장하기
    self.canvas = court.canvas

    # 캔버스에 공 생성하기
    self.ball = 

  # 공 이동 메소드
  def move_ball(self):
    # x_dist만큼 x 좌표 변경하기 - 양수 : 오른쪽, 음수 : 왼쪽
    self.x1 +=
    # y_dist만큼 y 좌표 변경하기 - 양수 : 아래쪽, 음수 : 위쪽
    self.y1 +=

    # 위쪽 벽 충돌하면 방향 바꾸기
    if self.y1 <= 5:
      

    # 아래쪽 벽 충돌하면 방향 바꾸기
    if self.y1 >= (self.court.height - (self.height - 5)):
      

    # 왼쪽 벽 충돌하면 방향 바꾸기
    if self.x1 <= 5:
      

    # 오른쪽 벽 충돌하면 방향 바꾸기
    if self.x1 + self.width >= self.court.width - 5:
      

    # 공 이동 좌표 저장하기
    self.x1 = self.x1
    self.x2 = self.x1 + self.width
    self.y1 = self.y1
    self.y2 = self.y1 + self.height

    # 공 위치 변경하기
    self.canvas.coords(self.ball, self.x1, self.y1, self.x2, self.y2)
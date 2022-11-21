from tkinter import *
from court import *
from ball import *

# 윈도 창과 캔버스의 가로, 세로 길이 초기화하기
width, height = 745, 374

win = Tk()
win.title("Tennis Game")
win.geometry("745x374+150+150")
win.resizable(False, False)

# Court 클래스 생성하기
court = Court(win, width, height, "court.png")

# 공의 좌표를 캔버스의 중앙으로 저장하기
x1, y1 = 
x2, y2 = 

# Ball 클래스 생성하기
ball = Ball(court, x1, y1, x2, y2)

# 게임 진행 함수
def play_game():
  # ball 객체 움직이는 함수 호출하기
  ball.move_ball()

  # 1초에 50번 play_game() 함수 호출하기
  win.after(50, play_game)

# 게임 진행 함수 호출하기


win.mainloop()
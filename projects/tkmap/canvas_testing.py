import tkinter
import tkintermapview

class App(tkinter.Tk):
    
    APP_NAME = "TkinterMapView Testing"
    WIDTH = 800
    HEIGHT = 700
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + 'x' + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.map_widget = tkintermapview.TkinterMapView(self, width=App.WIDTH, height=App.HEIGHT-100, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        # Set default values
        self.map_widget.set_address("대한민국")
        self.map_widget.set_zoom(7)
        self.map_widget.grid(row=0, column=0, columnspan=2)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
        
        # Markers dictionary
        self.allCities = {}
        self.marker_list = []
        
        # Entry
        self.entry = tkinter.Entry(self, width=60)
        self.entry.grid(row=1, column=0)
        
        # Add a marker
        self.addBtn = tkinter.Button(self, text="Add Entry", command=self.addCities)
        self.addBtn.grid(row=1, column=1)
        
        # Info Label
        self.info_lbl = tkinter.Label(self, text="")
        self.info_lbl.grid(row=2, column=0, columnspan=2)
        
    def addCities(self):
        # 입력값을 ':'으로 구분하여 왼쪽은 도시/나라이름, 오른쪽은 랜드마크(들)
        city = self.entry.get().split(':')
        
        # 도시/나라이름
        name = city[0].strip()
        
        # 랜드마크(들)
        landmarks = city[1].strip().split(',')
        landmarks = [i.strip() for i in landmarks]
        # print(name, landmarks)
        
        # 지도 이동
        self.map_widget.set_address(name)
        
        # 현재 위치
        current = self.map_widget.get_position()
        
        # 마커 정보 Label
        info = self.info_lbl
        
        def clickMarker(self):
            # 클릭한 마커로 지도 이동
            self.map_widget.set_address(name)
            
            # 클릭한 마커 내용 Label에 출력
            info['text'] = landmarks
        
        # 마커 만들어서 찍고 지도 이동 + 마커 클릭 함수 연결
        ## Check
        self.map_widget.set_address(name)
        
        marker = self.map_widget.set_marker(current[0], current[1], text=name, command=clickMarker)
        self.marker_list.append(marker)
        
        # allCities 업데이트
        self.allCities.update({
            name: [landmarks, current]
        })
        
        print(self.allCities)
        
        # 엔트리 초기화
        self.entry.delete(0, 'end')
    
    def on_closing(self, event=0):
        self.destroy()
        
    def start(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()
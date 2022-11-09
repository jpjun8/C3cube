from tkinter import *
import tkintermapview
from geopy.geocoders import Nominatim

# Geocoding Setup
geolocator = Nominatim(user_agent = 'gmap')

win = Tk()
win.geometry(f"{800}x{600}")
win.title("Map View Example")

map_widget = tkintermapview.TkinterMapView(win, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

# map_widget.set_position(37, 127)
# map_widget.set_zoom(7)

allCities = {}

def updateAllCities():
    # 입력값
    city = entry.get().split(':')
    
    # 도시 이름
    name = city[0].strip()
    
    # 랜드마크들
    temp = city[1].strip().split(',')
    landmarks = [i.strip() for i in temp]
    
    # geolocator에서 찾을 수 없는 지명은 에러가 나므로 
    # allCities에 추가도 되지 않음
    loc = geolocator.geocode(name)
    lat = loc.latitude
    lon = loc.longitude
    print(lat, lon)
    
    # 마커 추가
    marker = map_widget.set_marker(lat, lon, text=name, command=clickMarker)
    
    # 모든 도시와 내용들 딕셔너리에 추가
    allCities.update({
        name: landmarks
    })
    print(allCities)
    
def clickMarker(marker):
    print("Marker clicked:", marker.text)
    map_widget.set_position(marker.x, marker.y)
    map_widget.set_zoom(10)

entry = Entry(win)
entry.pack()

updateBtn = Button(win, text = "Update", command=updateAllCities)
updateBtn.pack()

win.mainloop()
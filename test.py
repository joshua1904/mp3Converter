import PySimpleGUI as sg
from main import download

sg.theme('DarkBlue4')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Video URL      '), sg.InputText()],
            [sg.Text('Download path'), sg.InputText(), sg.FolderBrowse("Open Folder")],
            [sg.Button('Download')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    window.set_title("mp3 downloader")
    if event == sg.WIN_CLOSED:
        break
    if event == 'Download':
        download(values[0], values[1])
        sg.popup("Download Complete",auto_close=True, auto_close_duration=2)

window.close()
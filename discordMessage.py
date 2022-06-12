import PySimpleGUI as sg
import requests
    
authCode = "youtAuthorizationCode"
deafoultChannel = "deafoultChannel"
    
layout = [
    [sg.Text('Channel', size =(15, 1)), sg.InputText()],
    [sg.Text('Authorization', size =(15, 1)), sg.InputText()],
    [sg.Text('Message', size =(15, 1)), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')]
    ]

win = sg.Window("TEST", layout)

while True:
    event, values = win.read()
    
    channel = values[0].split("/")[6] if "/" in values[0] else (deafoultChannel if values[0] == "" else values[0])
    auth = authCode if values[1] == "" else values[1]
    message = values[2]    

    def send(channel=channel, message=message, auth=auth):
        payload = {
            "content": message
        }

        header = {
            "authorization": auth
        }
        URL = f"https://discord.com/api/v9/channels/{channel}/messages"
        requests.post(URL, data=payload, headers=header)
        
    if event == "Ok":
        send(channel, message, auth)
           
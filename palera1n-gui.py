import PySimpleGUI as sg
import os

sg.theme('Dark Grey 13')
sfont=('Arial', 15)

layout = [[sg.Text('Select your options', font=('Arial', 17, 'bold'))],
          [sg.Checkbox('Rootless', font=sfont, default=False, key="RL")],
          [sg.Checkbox('Semi-tethered', font=sfont, default=False, key="ST")], [sg.Checkbox('Wifi only iPad/iPod', font=sfont, default=False, key="NB")],
          [sg.Checkbox('Skip-FakeFS', font=sfont, default=False, key="SF")], [sg.Checkbox('Dont Murder Tips', font=sfont, default=False, key="NI")],
          [sg.Checkbox('Verbose Boot', font=sfont, default=False, key="VB")], [sg.Checkbox('Debug Script', font=sfont, default=False, key="DB")],
          [sg.T('Version', font=sfont), sg.Combo(['15.0','15.0.1','15.0.2','15.1','15.1.1','15.2','15.2.1','15.3','15.3.1','15.4','15.4.1','15.5','15.6','15.6.1','15.7','15.7.1'],key='version',size=(13))],
          [sg.Button('Jailbreak', size=(15), font=sfont)],
          [sg.Button('Clean', size=(15), font=sfont)],
          [sg.Button('Close', size=(15), font=sfont)]]

win = sg.Window('Palera1n GUI', layout, margins=(25, 10), element_justification='l')
event, values = win.read()

while True:
    if event in ('Jailbreak', None):
        if event == 'Jailbreak':
            ver = values['version']
            options = ""
            if values["RL"] == False:
                options = options + "--tweaks "
                if values["ST"] == True:
                    options = options + "--semi-tethered "
            if values["SF"] == True:
                options = options + "--skip-fakefs "
            if values["NB"] == True:
                options = options + "--no-baseband "
            if values["NI"] == True:
                options = options + "--no-install "
            if values["VB"] == True:
                options = options + "--verbose "
            if values["DB"] == True:
                options = options + "--debug "
 
            cmd = f"./palera1n.sh {options} {ver}"
            if ver == "":
                exit("Didn't input version")
            os.system(cmd)
            break
    if event in ('Clean', None):
        if event == 'Clean':
            os.system('./palera1n clean && rm -rf blobs')

win.close()

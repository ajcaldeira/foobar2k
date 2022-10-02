from tkinter import filedialog
from tkinter import *
from ad_timer import AdTimer

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    ctrForAd = int(inputtxt.get("1.0", "end-1c"))
    print(filename)
    print(ctrForAd)
    print('Now running ad timer: ')

    runner = AdTimer(counterForAd=ctrForAd,
                     pathToMusic=filename,
                     pathToAd='000.mp3',
                    )
    print(runner.path_to_music)
    runner.AddSongsToFoobar()
    runner.PlayMusic()

def toggleBrowseLogic():
    ## Logic
    try:
        if int(inputtxt.get("1.0", "end-1c")) < 1 or inputtxt.get("1.0", "end-1c") == '':
            print('bb')
            button1["state"] = DISABLED
            inputtxt["bg"] = "salmon"

        else:
            button1["state"] = ACTIVE
            inputtxt["bg"] = "light green"

    except Exception as e:
        print(e)
        button1["state"] = DISABLED
        inputtxt["bg"] = "salmon"


root = Tk()
root.geometry("500x500")
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)

button1 = Button(text="Click Here To Choose Your Music Folder", command=browse_button)
button1["state"] = DISABLED

button2 = Button(text="Confirm", command=toggleBrowseLogic)

l = Label(text = "Enter a number of songs to play inbetween the ad:", font=("Arial", 12))
inputtxt = Text(root, height = 1,
                width = 3,
                bg = "salmon",
                )
## positions
l.grid(row=1,column=3) # instruction enter number
inputtxt.grid(row=1,column=5) #input box
button1.grid(row=3, column=3) #browse
button2.grid(row=1, column=7) #confirm
button2.grid(pady=20) #confirm
lbl1.grid(row=5, column=3) # path



mainloop()
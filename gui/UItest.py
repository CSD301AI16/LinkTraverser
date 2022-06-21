import tkinter as tk
from gui.ux import ux

ux = ux()


def getSliderVal(event):
    return sliderVal.get()


window = tk.Tk()
window.title('CSD301')
window.geometry("500x240")
label = tk.Label(window, text="Smart web crawler", font=(
    "digital-7", 30, "bold"), foreground="green")
label.pack(pady=10)
valFrame = tk.Frame(window)

# Entry value
inputVal = tk.StringVar()
sliderVal = tk.IntVar()

# Input frame
inputFrame = tk.Frame(valFrame)
inputLabel = tk.Label(inputFrame, text="Input URL")
inputLabel.grid(row=0, column=0, padx=40)
inputEntry = tk.Entry(inputFrame, width=30,
                      textvariable=inputVal, font=("tahoma", 12))
inputEntry.grid(row=0, column=1, padx=0)
inputFrame.grid(row=0, column=0, padx=0, pady=0)

# Slider frame
sliderFrame = tk.Frame(valFrame)
sliderLabel = tk.Label(sliderFrame, text="Maximum link")
sliderLabel.grid(row=0, column=0, padx=27)
sliderVal = tk.IntVar()
slider = tk.Scale(sliderFrame, from_=0, to=500, orient=tk.HORIZONTAL,
                  variable=sliderVal, length=250, showvalue=0, width=20, command=getSliderVal)
slider.grid(row=0, column=1)
sliderEntry = tk.Entry(sliderFrame, width=3,
                       textvariable=sliderVal, text=sliderVal)
sliderEntry.grid(row=0, column=2)
sliderFrame.grid(row=1, column=0, padx=0, pady=10)
valFrame.pack(padx=0, pady=0)

# Button frame
buttonFrame = tk.Frame(window)
webCrawl = tk.Button(buttonFrame, text="Crawl web",
                     activebackground="green", command=lambda: ux.crawl(str(inputVal.get()), int(sliderVal.get()), webCrawl))
webCrawl.grid(row=0, column=0, padx=20, pady=10)
pageRank = tk.Button(buttonFrame, text="Ranking URLs",
                     activebackground='green', command=lambda: ux.ranking())
pageRank.grid(row=0, column=1, padx=20, pady=10)
exportFile = tk.Button(buttonFrame, text="Export to file",
                       activebackground='green', command=lambda: print('b'))
exportFile.grid(row=0, column=2, padx=20, pady=10)
buttonFrame.place(x=80, y=150)
window.mainloop()

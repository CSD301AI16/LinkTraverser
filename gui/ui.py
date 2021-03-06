import tkinter as tk

from gui.ux import ux

ux = ux()


class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("500x300")

        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth()//2) - (width//2)
        y = (self.winfo_screenheight()//2) - (height//2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        label = tk.Label(self, text="Smart web crawler", font=(
            "digital-7", 30, "bold"), foreground="green")
        label.pack(pady=10)
        valFrame = tk.Frame(self)

        # Entry value
        inputVal = tk.StringVar()
        sliderVal = tk.IntVar()

        def getSliderVal(event1):
            return sliderVal.get()

        def getMaxNodeSliderVal(event2):
            return maxNodeVal.get()

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
        sliderLabel.grid(row=0, column=0, padx=26)
        sliderVal = tk.IntVar()
        slider = tk.Scale(sliderFrame, from_=1, to=500, orient=tk.HORIZONTAL,
                          variable=sliderVal, length=250, showvalue=0, width=20, command=getSliderVal)
        slider.grid(row=0, column=1)
        sliderEntry = tk.Entry(sliderFrame, width=3,
                               textvariable=sliderVal, text=sliderVal)
        sliderEntry.grid(row=0, column=2)
        sliderFrame.grid(row=1, column=0, padx=0, pady=10)

        # Max node slider frame
        maxNodeFrame = tk.Frame(valFrame)
        maxNodeLabel = tk.Label(maxNodeFrame, text="Maximum node")
        maxNodeLabel.grid(row=0, column=0, padx=22)
        maxNodeVal = tk.IntVar()
        maxNodeSlider = tk.Scale(maxNodeFrame, from_=1, to=500, orient=tk.HORIZONTAL,
                                 variable=maxNodeVal, length=250, showvalue=0, width=20, command=getMaxNodeSliderVal)
        maxNodeSlider.grid(row=0, column=1)
        maxNodeEntry = tk.Entry(maxNodeFrame, width=3,
                                textvariable=maxNodeVal, text=maxNodeVal)
        maxNodeEntry.grid(row=0, column=2)
        maxNodeFrame.grid(row=2, column=0, padx=2, pady=0)
        valFrame.pack(padx=0, pady=0)

        # Button frame
        buttonFrame = tk.Frame(self)
        webCrawl = tk.Button(buttonFrame, text="Crawl web",
                             activebackground="green", command=lambda: ux.crawl(str(inputVal.get()), int(sliderVal.get()), int(maxNodeVal.get())))
        webCrawl.grid(row=0, column=0, padx=20, pady=10)
        pageRank = tk.Button(buttonFrame, text="Ranking URLs",
                             activebackground='green', command=lambda: ux.ranking())
        pageRank.grid(row=0, column=1, padx=20, pady=10)
        exportFile = tk.Button(buttonFrame, text="Export to file",
                               activebackground='green', command=lambda: ux.saveFile())
        exportFile.grid(row=0, column=2, padx=20, pady=10)
        buttonFrame.place(x=80, y=180)


if __name__ == "__main__":
    window = MyApp()
    window.title('CSD301')
    window.mainloop()

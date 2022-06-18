from cProfile import label
import tkinter as tk
from turtle import onclick
from requests import RequestException
from Graph import Graph
from Node import Node
from getlink import LinkTraverser
from tkinter import messagebox

traverse = Graph('', obL=[])


def getSliderVal(event):
    return sliderVal.get()


def crawl(url, max_hrefs):
    specSign = ['/', ' ']
    for i in specSign:
        for j in specSign:
            url = url.lstrip(i).rstrip(j)
    if 'https://' not in url:
        url = 'https://' + url + '//'
    global traverse
    if webCrawl is not onclick:
        traverse.empty()
        try:
            travser1 = LinkTraverser(rootURL=url, max_hrefs=max_hrefs)
            outboundlist = travser1.get_href_list()
            traverse = Graph(url, obL=outboundlist)
            print(traverse.summaryLinkList)
        except RequestException as e:
            messagebox.showerror("Error", "Invalid URL")


def Ranking():
    traverse.sort()
    messagebox.showinfo("Ranking", 'Ranking completed')


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
                     activebackground="green", command=lambda: crawl(str(inputVal.get()), int(sliderVal.get())))
webCrawl.grid(row=0, column=0, padx=20, pady=10)
pageRank = tk.Button(buttonFrame, text="Ranking URLs",
                     activebackground='green', command=lambda: Ranking())
pageRank.grid(row=0, column=1, padx=20, pady=10)
exportFile = tk.Button(buttonFrame, text="Export to file",
                       activebackground='green', command=lambda: print('b'))
exportFile.grid(row=0, column=2, padx=20, pady=10)
buttonFrame.place(x=80, y=150)
window.mainloop()

from tkinter import messagebox
from requests import RequestException
from graph.Graph import Graph
from graph.Grapher import Node
from graph.getlink import LinkTraverser
import tkinter as tk
from tkinter import filedialog


class ux:
    global traverse
    traverse = Graph("", obL=[])
    global travser1

    def __init__(self) -> None:
        pass

    def crawl(self, url, max_hrefs, webCrawl: tk.Button):
        if 'https://' not in url:
            url = 'https://' + url
        global traverse
        traverse.empty()
        try:
            travser1 = LinkTraverser(rootURL=url, max_hrefs=max_hrefs)
            outboundlist = travser1.get_href_list()
            print(outboundlist)
            traverse = Graph(url, obL=outboundlist)
            print(traverse.summaryLinkList)
        except RequestException as e:
            messagebox.showerror("Error", "Invalid URL")

    def ranking(self):
        if len(traverse.summaryLinkList) == 1:
            messagebox.showinfo("Error", "You need to crawl first")
        else:
            traverse.sort()
            messagebox.showinfo("Ranking", 'Ranking completed')
            traverse.print_sorted_list()

    def saveFile(self):
        if len(traverse.summaryLinkList) == 1:
            messagebox.showinfo("Error", "You need to crawl first")
        else:
            filename = filedialog.asksaveasfile(mode='w',
                                                filetypes=[('HTML file', '*.html')], defaultextension='.html')
            for i in traverse.get_sorted_elements():
                filename.write('<div><a href ='+str(i) +
                               '>'+str(i)+'</a></div>\n')
            filename.close()

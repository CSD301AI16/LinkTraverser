from tkinter import messagebox

from requests import RequestException
from graph.Graph import Graph
from graph.getlink import LinkTraverser
import tkinter as tk
from tkinter import filedialog


class ux:
    global traverse
    traverse = Graph('', obL=[])

    def __init__(self) -> None:
        pass

    def crawl(self, url, max_hrefs, webCrawl: tk.Button):
        global traverse
        if 'https://' not in url:
            url = 'https://' + url + '//'
        traverse.empty()
        try:
            travser1 = LinkTraverser(rootURL=url, max_hrefs=max_hrefs)
            outboundlist = travser1.get_href_list()
            traverse = Graph(url, obL=outboundlist)
            print(traverse.summaryLinkList)
        except RequestException:
            messagebox.showerror("Error", "Invalid URL")

    def ranking(self):
        if len(traverse.summaryLinkList) == 0:
            messagebox.showinfo("Error", "Crawl first")
        else:
            traverse.sort()
            messagebox.showinfo("Ranking", 'Ranking completed')
            traverse.print_sorted_list()

    def saveFile(self):
        filename = filedialog.asksaveasfile(mode='w',
                                            filetypes=[('HTML file', '*.html')], defaultextension='.html')
        for i in traverse.get_sorted_elements():
            filename.write('<div><a href ='+str(i)+'>'+str(i)+'</a></div>\n')
        filename.close()

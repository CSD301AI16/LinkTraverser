from tkinter import Toplevel, messagebox
from requests import RequestException
from graph.Graph import Graph
from graph.getlink import LinkTraverser
from turtle import onclick
import tkinter as tk
import os
from tkinter import filedialog


class ux:
    global traverse
    traverse = Graph('', obL=[])
    global sourcePath
    sourcePath = 'C:'

    def __init__(self) -> None:
        pass

    def crawl(self, url, max_hrefs, webCrawl: tk.Button):
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

    def ranking(self):
        traverse.sort()
        messagebox.showinfo("Ranking", 'Ranking completed')
        traverse.print_sorted_list()

    def chooseFolder(self):
        global source_path
        source_path = filedialog.askdirectory(
            title='Select the Directory')
        print(source_path)

    def saveFile(self):
        filename = filedialog.asksaveasfile(mode='w',
                                            filetypes=[('HTML file', '*.html')])
        for i in traverse.get_sorted_elements():
            filename.write('<div><a href ='+str(i)+'>'+str(i)+'</a></div>\n')
        filename.close()

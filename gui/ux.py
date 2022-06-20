from tkinter import messagebox
# from graph.Graph import Graph
# from graph.getlink import LinkTraverser
from turtle import onclick
import tkinter as tk
from tkinter import filedialog
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from graph.Grapher import Graph, Node


class ux:
    global traverse
    traverse = Graph('', summaryLinkList={})
    global sourcePath
    sourcePath = 'C:'

    def __init__(self) -> None:
        pass

    def crawl(self, url, max_hrefs, webCrawl: tk.Button):
        global traverse
        if 'https://' not in url:
            url = 'https://' + url + '//'
        validate = URLValidator()
        root = Node(link=url)
        try:
            validate(url)
            if webCrawl is not onclick:
                traverse.empty()
                # travser1 = LinkTraverser(rootURL=url, max_hrefs=max_hrefs)
                # outboundlist = travser1.get_href_list()
                traverse = Graph(root, summaryLinkList={url: root},
                                 max_href=max_hrefs, maxNode=max_hrefs)
                traverse.BFS()
                print(traverse.summaryLinkList)
        except ValidationError:
            messagebox.showerror("Error", "Invalid URL")

    def ranking(self):
        if len(traverse.summaryLinkList) == 1:
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

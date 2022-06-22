from tkinter import messagebox
# from graph.Graph import Graph
# from graph.getlink import LinkTraverser
import tkinter as tk
from tkinter import filedialog
from requests import RequestException
from graph.Grapher import Graph, Node


class ux:
    global traverse
    traverse = Graph('', summaryLinkList={})

    def __init__(self) -> None:
        pass

    def crawl(self, url, max_hrefs, maxNode):
        global traverse
        if url == '':
            messagebox.showinfo("Error", "Input URL")
        else:
            if 'https://' not in url:
                url = 'https://' + url
            root = Node(link=url)
            try:
                # travser1 = LinkTraverser(rootURL=url, max_hrefs=max_hrefs)
                # outboundlist = travser1.get_href_list()
                traverse = Graph(root, summaryLinkList={url: root},
                                 max_href=max_hrefs, maxNode=maxNode)
                traverse.BFS()
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
        if len(traverse.summaryLinkList) == 0:
            messagebox.showinfo("Error", "Crawl first")
        else:
            filename = filedialog.asksaveasfile(mode='w',
                                                filetypes=[('HTML file', '*.html')], defaultextension='.html')
            for i in traverse.get_sorted_elements():
                filename.write('<div><a href ='+str(i.link) +
                               '>'+str(i.link)+'</a></div>\n')
            filename.close()

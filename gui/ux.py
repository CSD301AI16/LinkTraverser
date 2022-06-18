from tkinter import messagebox
from requests import RequestException
from graph.Graph import Graph
from graph.getlink import LinkTraverser
from turtle import onclick
import tkinter as tk


class ux:
    global traverse
    traverse = Graph('', obL=[])

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
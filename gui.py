import tkinter as tk
import json
from api import functions

class window(tk.Tk):
	def __init__(self):
		super().__init__()
		self.geometry('767x445')
		self.title('Get daily news')
		self.funcs = functions()

	def main_window(self):
		# Creating required labels and frame
		title = tk.Label(self, text="Get news", font="monospace 20")
		frame = tk.Frame(self)
		
		# Creating required variables
		query = tk.StringVar()
		query.set('')
		
		# Creating entry boxes
		query_box = tk.Entry(frame, textvariable=query)
		
		# Creating label for entry box
		query_label = tk.Label(frame, text="Query: ")
		
		# Creating buttons
		submit = tk.Button(frame, text="Submit", command=lambda: (self.window_result(query.get())))
		
		# Packing everything
		query_label.grid(column=1, row=1)
		query_box.grid(column=2, row=1)
		submit.grid(column=1, row=2)
		
		title.pack()
		frame.pack()

	def show_json(self, json_data: str):
		# Creating required frame
		frame = tk.Frame(self.slave_window)

		# Creating required variables
		data = json.loads(json_data)
		articles = data.get('articles')
		titles = []
		selected_title = tk.StringVar()
		selected_title.set('Options')

		# Functions which will be used
		def find_selected_article(title: str, articles: list):
			for article in articles:
				if article.get('title') == title:
					return article
			return False
		
		def see_news(selected_article: dict):
			#self.slave_window.geometry('')
			frame.pack_forget()
			frame2 = tk.Frame(self.slave_window)

			title = tk.Label(frame2, text='Title: '+selected_article.get('title'))
			author = tk.Label(frame2, text='Author: '+selected_article.get('author'))
			source = tk.Label(frame2, text="Source: "+selected_article.get('source').get('name'))
			link = tk.Label(frame2, text='Link: '+selected_article.get('url'))
			date = tk.Label(frame2, text='Published At: '+selected_article.get('publishedAt'))
			content = tk.Label(frame2, text='Content: '+selected_article.get('content'))


			title.grid(column=1, row=1)
			author.grid(column=1, row=2)
			source.grid(column=1, row=3)
			link.grid(column=1, row=4)
			date.grid(column=1, row=5)
			content.grid(column=1, row=6)
			
			frame2.pack()
			
		
		for article in articles:
			titles.append(article.get('title'))

		# Creating label
		label_choose = tk.Label(frame, text="Choose News: ")

		# Creating option menu
		entry_box = tk.OptionMenu(frame, selected_title, *titles)

		# Creating buttons
		submit = tk.Button(frame, text="Submit", command=lambda: (frame.pack_forget(), see_news(find_selected_article(selected_title.get(), articles))))

		# Packing Everything
		label_choose.grid(column=1, row=1)
		entry_box.grid(column=2, row=1)
		submit.grid(column=1, row=2)
		frame.pack()
			
			
	def window_result(self, query: str):
		self.slave_window = tk.Toplevel(self)

		self.slave_window.title(f'GET {query} NEWS')
		self.slave_window.geometry('700x300')
		
		json_text = self.funcs.get(query)

		self.show_json(json_text)
		

if __name__=='__main__':
	windo = window()
	windo.main_window()
	windo.mainloop()

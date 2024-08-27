import tkinter as tk
from tkinter import ttk
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from phone_scraper.spiders.phone_spider import PhoneSpider

class ScrapyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Web Scraper")
        self.geometry("600x400")
        
        self.create_widgets()

    def create_widgets(self):
        self.url_label = tk.Label(self, text="Website URL:")
        self.url_label.pack(pady=5)

        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=5)

        self.names_label = tk.Label(self, text="Names (comma-separated):")
        self.names_label.pack(pady=5)

        self.names_entry = tk.Entry(self, width=50)
        self.names_entry.pack(pady=5)

        self.scrape_button = tk.Button(self, text="Scrape", command=self.start_scraping)
        self.scrape_button.pack(pady=20)

        self.result_text = tk.Text(self, width=70, height=15)
        self.result_text.pack(pady=5)

    def start_scraping(self):
        url = self.url_entry.get()
        names = self.names_entry.get()

        process = CrawlerProcess(get_project_settings())
        process.crawl(PhoneSpider, url=url, names=names)
        process.start()

        self.result_text.insert(tk.END, "Scraping complete!\n")

if __name__ == "__main__":
    app = ScrapyApp()
    app.mainloop()

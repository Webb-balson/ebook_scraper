import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"

    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("---- RESPONSE -----")
        print(response)

        print(response.css("h3 a::text").get())
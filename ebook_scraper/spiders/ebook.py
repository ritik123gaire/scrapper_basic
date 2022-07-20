import scrapy

class ebookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]
    

    def parse(self, response):
        print("[parse]")
        # print(response)

        ebooks = response.css("article")

        for ebook in ebooks:
            title = ebook.css("a::text").get()
            price = ebook.css("p.price_color::text").get()
            
            yield {
                "title" : title,
                "price" : price
            }
            
 
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["http://wolfgangtechnologies.cz/public/web-scraping/index-scrape.html"]

    def parse(self, response):
        # Extract the values from the webpage
        list1_values = response.css('#list1 .value::text').getall()
        list2_values = response.css('#list2 .value::text').getall()
        list3_values = response.css('#list3 .value::text').getall()

        # Process or store the scraped data as needed
        # In this example, we will print the values to the console

        

        print('List 1 values:')
        for value in list1_values:
            print(value)

        print('List 2 values:')
        for value in list2_values:
            print(value)

        print('List 3 values:')
        for value in list3_values:
            print(value)

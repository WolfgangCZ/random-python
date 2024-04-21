import scrapy


class ExampleSpider(scrapy.Spider):
    name = "spider1"
    start_urls = ["https://www.forexfactory.com"]

    def parse(self, response):
        # Extract the values from the webpage
        print("========================START=======================")
        list1_values = response.css('#calendar__cell .value::text').getall()
        # Process or store the scraped data as needed
        # In this example, we will print the values to the console
        
        print('List 1 values:')
        for value in list1_values:
            print(value)
        print("========================FINISH=======================")

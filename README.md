# Scrapy-Idealista
Scrap data from idealista website using Scrapy 1.4 Python

# How to: 
Inside the spiders folder, you'll find the available spiders that can scrap data from the Idealista website.

Start command:
```
scrapy crawl madrid-provincia -o file_name.csv -t csv
```

If you want to add new places, you can easily create a new spider, you just need to inherit from main class: Core.
Like so :

```
class MyOtherCitySpider(Core):
    name = "barcelona-provincia"

    def __init__(self):
        super(MyOtherCitySpider, self).__init__(self.name, "venta", "viviendas")
```

Inside each spider, you can also create many spiders to get houses, buildings, parking slots etc. 

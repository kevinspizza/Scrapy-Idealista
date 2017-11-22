from idealista.spiders.core import Core


#class BarcelonaEdificiosSpider(Core):
    #name = "barcelona-provincia"

    #def __init__(self):
        #super(BarcelonaEdificiosSpider, self).__init__(self.name, "venta", "edificios")


class BarcelonaViviendaSpider(Core):
    name = "barcelona-provincia"

    def __init__(self):
        super(BarcelonaViviendaSpider, self).__init__(self.name, "venta", "viviendas")

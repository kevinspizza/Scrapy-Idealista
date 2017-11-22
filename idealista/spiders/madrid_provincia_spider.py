from idealista.spiders.core import Core


#class MadridEdificiosSpider(Core):
    #name = "madrid-provincia"

    #def __init__(self):
        #super(MadridEdificiosSpider, self).__init__(self.name, "venta", "edificios")


class MadridViviendaSpider(Core):
    name = "madrid-provincia"

    def __init__(self):
        super(MadridViviendaSpider, self).__init__(self.name, "venta", "viviendas")

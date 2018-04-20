import scrapy

class IMDBSpider(scrapy.Spider):
    name = 'imdb_homepage'

    start_urls = ['http://www.imdb.com/']
    
    def parse(self, response):
        path = 'data/'
        filename = path + 'homepage.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        print('Saved file %s' % filename)


class BOISpider(scrapy.Spider):
    name = 'boxofficeindia'

    root_path = 'https://boxofficeindia.com/india-first-weekend.php?year='
    start_urls = []
    for i in range(2000, 2015):
        start_urls.append(root_path + str(i))
    
    def parse(self, response):
        path = 'data/boi/'
        page = response.url.split("/")[-1].split("=")[-1]
        filename = path + 'india-first-weekend_%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


class BOIMoviesSpider(scrapy.Spider):
    name = 'boi-movies'
    root_path = "https://www.boxofficeindia.com/movie.php?movieid="
    start_urls = []
    for i in range(3730):
        start_urls.append(root_path + str(i))
    
    def parse(self, response):
        path = 'data/boi_movies/'
        page = response.url.split("=")[-1]
        filename = path + 'movie_%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

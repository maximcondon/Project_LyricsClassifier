import scrapy
from scrapy.http import Request # an object that we need to convert any URL string into something
                                # we can go into


class LyricSpider(scrapy.Spider):
    name = 'lyric-spider'
    allowed_domains = ['lyrics.com']
    start_urls = ['https://www.lyrics.com/artist/Tame+Impala/1111074',
    'https://www.lyrics.com/artist/Frank+Ocean/2295304',
    'https://www.lyrics.com/artist/Kendrick+Lamar/2412704',
    'https://www.lyrics.com/artist/Arctic+Monkeys/744567']

    custom_settings = {
        'DEPTH_LIMIT': 10,
        'AUTOTHROTTLE_ENABLED':True, # Automatically adjusts the speed of the scraping for various reasons
        'AUTOTHROTTLE_START_DELAY': 1.0, #Mirrors humans as well, stops you getting booted from websites
        'AUTOTHROTTLE_TARGET_CONCURRENCY':0.5 #
        }

    def parse(self, response): # Don't worry too much about it, we always use these two

        urls = response.xpath('//td[@class="tal qx"]/strong/a/@href').getall()

        for u in urls:

            full_url = response.urljoin(u) #adding the prefic to each url
            full_url = Request(full_url) # making the URL 'gettable'
            yield full_url

        lyrics = response.xpath('//pre[@id="lyric-body-text"]//text()').getall()
        lyrics = ' '.join(lyrics)

        artist = response.xpath('//h3[@class="lyric-artist"]/a/text()').get()

        print(lyrics)
        print(artist)
        print('\n')

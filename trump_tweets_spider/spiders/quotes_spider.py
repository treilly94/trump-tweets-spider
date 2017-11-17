import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://twitter.com/realDonaldTrump',
    ]

    def parse(self, response):
        for tweet in response.css("div.tweet"):
            yield {
                'text': tweet.css('p.tweet-text::text').extract(),
            }

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://twitter.com/realDonaldTrump',
    ]

    def parse(self, response):
        for tweet in response.css("div.tweet"):
            yield {
                'tweet_id': tweet.css('div.tweet::attr(data-tweet-id)').extract(),
                'user_id': tweet.css('div.tweet::attr(data-user-id)').extract(),
                'timestamp': tweet.css('span._timestamp::attr(data-time-ms)').extract(),
                'permalink': tweet.css('div.tweet::attr(data-permalink-path)').extract(),
                'tweet_text': tweet.css('p.tweet-text::text').extract(),
            }

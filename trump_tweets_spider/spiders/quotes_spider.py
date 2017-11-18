import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://twitter.com/realDonaldTrump',
    ]

    def parse(self, response):
        for tweet in response.css("div.tweet"):
            yield {
                'tweet_id': tweet.css('div.tweet::attr(data-tweet-id)').extract_first(),
                'user_id': tweet.css('div.tweet::attr(data-user-id)').extract_first(),
                'timestamp': tweet.css('span._timestamp::attr(data-time-ms)').extract_first(),
                'permalink': tweet.css('div.tweet::attr(data-permalink-path)').extract_first(),
                # TODO make @ things appear in text
                'tweet_text': tweet.css('p.tweet-text::text').extract(),
                'mentions': tweet.css('a.twitter-atreply::attr(href)').extract(),
                'hashtags': tweet.css('a.twitter-hashtag::attr(href)').extract(),
            }

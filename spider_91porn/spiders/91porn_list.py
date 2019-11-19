import scrapy
from scrapy import Request
from urllib import parse


class Spider91PornList(scrapy.Spider):
    name = '91pornlist'

    allowed_domains = ['627.workarea7.live']

    def start_requests(self):
        yield Request(url="http://627.workarea7.live/v.php?next=watch", dont_filter=True)

        # for index in range(1, 312):
        #     yield Request(url="http://www.kaichecc.com/category/guochan/page/" + str(index), dont_filter=True)
        #

    def parse(self, response):
        listchannel = response.xpath("//div[@class='listchannel']")
        for channel in listchannel:
            url = channel.xpath("div[contains(@class, 'imagechannel')]/a/@href").extract_first()
            cover = channel.xpath("div[contains(@class, 'imagechannel')]/a/img/@src").extract()
            title = channel.xpath("a/span[@class='title']/text()").extract()
            print(url)
            print(cover)
            print(title)
            time = channel.xpath(".//span[contains(text(), 'Runtime')]/following-sibling::text()[1]")[0].extract().strip()
            added_time = channel.xpath(".//span[contains(text(), 'Added')]/following-sibling::text()[1]")[
                0].extract().strip()
            author = channel.xpath(".//span[contains(text(), 'From')]/following-sibling::text()[1]")[0].extract().strip()
            views = channel.xpath(".//span[contains(text(), 'Views')]/following-sibling::text()[1]")[0].extract().strip()
            comments = channel.xpath(".//span[contains(text(), 'Comments')]/following-sibling::text()[1]")[
                0].extract().strip()
            favorites = channel.xpath(".//span[contains(text(), 'Favorites')]/following-sibling::text()[1]")[
                0].extract().strip()
            point = channel.xpath(".//span[contains(text(), 'Point')]/following-sibling::text()[1]")[0].extract().strip()
            print(time)
            print(added_time)
            print(author)
            print(views)
            print(comments)
            print(favorites)
            print(point)

            rate = channel.xpath(".//div[@class='startratebox']/span[@class='info']/img[contains(@src, 'star_full')]")
            print(len(rate))

            result = parse.urlparse(url)
            viewkey = parse.parse_qs(result.query)['viewkey'][0]
            print(viewkey)

            yield Request(url=url, callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        #poster = response.xpath("//video[@class='video-js vjs-default-skin']/@poster")
        #print(poster)

        # added_time_standard = response.xpath("//div[@id='videodetails-content']/span[contains(text(), 'Added')]/following-sibling::span[1]")

        #加入日期
        added_time = response.xpath("//div[@id='videodetails-content']/span[@class='title']/text()")[0].extract()

        #信息
        description = response.xpath("//div[@id='videodetails-content']/span[@class='title']/text()")[1].extract()

        #个人信息
        uprofile = response.xpath("//div[@id='videodetails-content']/span[contains(text(), 'From')]/following-sibling::a[1]/@href").extract_first()

        # 上传的视频
        uvideos = response.xpath("//div[@id='videodetails-content']/span[@class='title']/a/@href")[0].extract()

        #关注的人
        ufollowwd = response.xpath("//div[@id='videodetails-content']/span[@class='title']/a/@href")[1].extract()

        print(added_time)
        print(description)
        print(uprofile)
        print(uvideos)
        print(ufollowwd)
        pass

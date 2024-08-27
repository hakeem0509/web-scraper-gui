import scrapy
import re

class PhoneSpider(scrapy.Spider):
    name = "phone_spider"

    def __init__(self, url=None, names=None, *args, **kwargs):
        super(PhoneSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]
        self.names = [name.strip() for name in names.split(',')] if names else []

    def parse(self, response):
        page_text = response.text
        phone_pattern = r'\b07\d{8}\b'
        phones = re.findall(phone_pattern, page_text)

        for name in self.names:
            name_pattern = re.compile(re.escape(name), re.IGNORECASE)
            name_positions = [(match.start(), match.end()) for match in name_pattern.finditer(page_text)]
            
            for name_start, name_end in name_positions:
                closest_phone = None
                min_distance = float('inf')
                for phone in phones:
                    phone_pos = page_text.find(phone, name_end)
                    if phone_pos != -1 and abs(phone_pos - name_end) < min_distance:
                        closest_phone = phone
                        min_distance = abs(phone_pos - name_end)
                if closest_phone:
                    yield {
                        'name': name,
                        'phone': closest_phone,
                        'url': response.url,
                    }

        for next_page in response.css('a::attr(href)').getall():
            yield response.follow(next_page, self.parse)

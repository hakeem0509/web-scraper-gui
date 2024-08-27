# settings.py

# Identify yourself on the user-agent
USER_AGENT = 'phone_scraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 2

# Enable AutoThrottle to adjust the delay based on server response times
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 60

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

"""Scrapy settings.

Crawling rules (see CLAUDE.md): respect robots.txt, identify clearly,
and rate-limit politely.
"""

BOT_NAME = "relocate_crawler"

SPIDER_MODULES = ["relocate_crawler.spiders"]
NEWSPIDER_MODULE = "relocate_crawler.spiders"

USER_AGENT = "RelocateRadarBot/0.1 (+https://github.com/poojan019/relocate-radar)"

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS_PER_DOMAIN = 2
DOWNLOAD_DELAY = 1.0

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1.0
AUTOTHROTTLE_MAX_DELAY = 30.0
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

HTTPCACHE_ENABLED = False

FEED_EXPORT_ENCODING = "utf-8"

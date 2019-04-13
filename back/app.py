import logging

import aiodns
from aiohttp import web
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

app = web.Application()
dns_resolver = aiodns.DNSResolver()

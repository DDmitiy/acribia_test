import aiodns
from aiohttp import web

app = web.Application()
dns_resolver = aiodns.DNSResolver()

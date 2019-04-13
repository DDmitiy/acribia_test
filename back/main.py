import json
import logging
from asyncio import as_completed

from aiohttp import web, WSMsgType, WSMessage
from aiohttp.web_request import Request
from aiohttp.web_ws import WebSocketResponse

from back.app import app
from back.resolver import domains_chunks, count_domains, CHUNK_LEN

logger = logging.getLogger(__name__)


async def message_handler(ws: WebSocketResponse, msg: WSMessage) -> None:
    data = json.loads(msg.data)
    domain = data['domain']
    deep = data.get('deep', 1)
    domains_count = count_domains(deep)
    logger.debug(f'Get request for {domain} and subdomains deep {deep}')
    for chunk_i, chunk in enumerate(domains_chunks(domain, deep), 1):
        for host in as_completed(chunk):
            resolved_host = await host
            if resolved_host:
                await ws.send_json({'action': 'add_host', 'domain': resolved_host})
        await ws.send_json({
            'action': 'update_progress',
            'percent': round(chunk_i * CHUNK_LEN / domains_count * 100, 2),
        })
    logger.info('Stop checking')
    await ws.send_json({'action': 'stop_checking'})


async def websocket_handler(request: Request) -> WebSocketResponse:
    """
    Main handler for websocket requests.

    :param request: websocket request
    :return: websocket response
    """
    logger.info('Get ws request')
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
                logger.info('Close ws connection')
            else:
                await message_handler(ws, msg)
        elif msg.type == WSMsgType.ERROR:
            logger.warning(f'ws connection closed with exception {ws.exception()}')
    logger.info('websocket connection closed')

    return ws

app.add_routes([web.get('/ws', websocket_handler)])
web.run_app(app, port=5632)
logger.info('Start app')

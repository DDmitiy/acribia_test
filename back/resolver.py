import itertools
from typing import Iterable, Awaitable, Optional

from aiodns.error import DNSError

from back.app import dns_resolver
from back.subdomains import most_popular_subdomains

CHUNK_LEN = 1000


async def check_domain(domain: str) -> Optional[str]:
    """
    Checking A record for domain.

    :param domain: domain for check
    :return: domain or None
    """
    try:
        await dns_resolver.query(domain, 'A')
    except (DNSError, UnicodeError):
        return None
    return domain


def count_domains(deep: int) -> int:
    """
    Count total domains combinations

    :param deep: deep of subdomains
    :return: total count of domains combinations
    """
    return sum([len(most_popular_subdomains)**i for i in range(1, deep+1)])


def domains_chunks(domain: str, deep: int = 1) -> Iterable[Awaitable[set]]:
    """
    Func for generate chunks of full domains.

    :param domain: main domain
    :param deep: deep of subdomains
    :return: generator of full domains chunks
    """
    for repeat_i in range(1, deep+1):
        subdomains_combos = itertools.product(most_popular_subdomains, repeat=deep)
        combos_len = len(most_popular_subdomains)**repeat_i
        for chunk_i in range(combos_len // CHUNK_LEN):
            chunk = set()
            for _ in range(chunk_i * CHUNK_LEN, min((chunk_i + 1) * CHUNK_LEN, combos_len)):
                full_domain = '.'.join(next(subdomains_combos))
                chunk.add(check_domain(f'{full_domain}.{domain}'))
            yield chunk

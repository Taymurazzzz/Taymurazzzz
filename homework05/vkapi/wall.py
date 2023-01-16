import time
import typing as tp

import pandas as pd  # type: ignore
import requests  # type: ignore
from pandas import json_normalize

from vkapi import config
from vkapi.session import Session


def get_posts_2500(
    owner_id: str = "",
    domain: str = "",
    offset: int = 0,
    count: int = 10,
    max_count: int = 2500,
    filter: str = "owner",
    extended: int = 0,
    fields: tp.Optional[tp.List[str]] = None,
) -> tp.Dict[str, tp.Any]:
    s = Session(base_url="")
    code = """return API.wall.get({
                '"owner_id": "owner_id"',
                '"domain": "domain"',
                '"offset": offset',
                '"count": "1"',
                '"filter": "filter"',
                '"extended": extended',
                '"fields": "fields"',
                '"v": "v"'
                });"""

    post = requests.post(
        "https://api.vk.com/method/execute",
        data={
            "code": f"{code}",
            "access_token": f"{config.VK_CONFIG['access_token']}",
            "v": f"{config.VK_CONFIG['version']}",
        },
    )

    return post.json()["response"]["items"]


def get_wall_execute(
    owner_id: str = "",
    domain: str = "",
    offset: int = 0,
    count: int = 10,
    max_count: int = 2500,
    filter: str = "owner",
    extended: int = 0,
    fields: tp.Optional[tp.List[str]] = None,
    progress=None,
) -> pd.DataFrame:
    result: tp.List[str] = []
    for i in range((count / 2500).__ceil__()):
        response = get_posts_2500(
            owner_id, domain, i * 2500, max_count, max_count, filter, extended, fields
        )
        result += response
        time.sleep(1)
    return json_normalize(result)

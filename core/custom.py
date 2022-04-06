#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   custom.py
@Time    :   2022/04/02 10:17:03
@Author  :   Viperorz
@Version :   1.0.0
@License :   (C)Copyright 2021-2022
@Desc    :   None
"""


from typing import List, Union
from pyrogram import filters
from pyrogram.types import Message
from tools.constants import STORE_TRACE_DATA
from tools.storage import SimpleStore


def command(command: Union[str, List[str]]):
    """匹配UserBot指令"""
    return filters.me & filters.text & filters.command(command, '-')


def is_traced():
    """正则匹配用户输入指令及参数"""
    async def func(flt, _, msg: Message):
        async with SimpleStore(auto_flush=False) as store:
            trace_data = store.get_data(STORE_TRACE_DATA)
            if not trace_data:
                return False
            elif not trace_data.get(msg.from_user.id):
                return False
            return True

    # "data" kwarg is accessed with "flt.data" above
    return filters.incoming & filters.create(func)

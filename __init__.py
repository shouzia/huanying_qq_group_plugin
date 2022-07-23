from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot import on_regex

__zx_plugin_name__ = "幻影"
__plugin_usage__ = """
usage：
    幻影群指令
    指令：
        下载/cdlinux/kali/破解
""".strip()
__plugin_des__ = "幻影群指令"
__plugin_cmd__ = ["下载/cdlinux/kali/破解"]
__plugin_version__ = 0.1
__plugin_author__ = 'Shouzi'
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["下载", "cdlinux", "破解", "kali"],
}

download = on_regex("^(下载)$", block=True, aliases={"下载", "官网"}, priority=5)


@download.handle()
async def download_escape():
    await download.send("通道h5ai:https://h5ai.108878.xyz/\n""通道官网:https://hypin.cn/download")

cdlinux = on_regex("^(cdlinux)$", block=True, aliases={"cdlinux"}, priority=5)


@cdlinux.handle()
async def cdlinux_escape():
    await cdlinux.send("CDlinux破解教程:\nhttps://blog.shouzi.xyz/cdlinux-wifi/")

kali = on_regex("^(kali)$", block=True, aliases={"kali"}, priority=5)


@kali.handle()
async def kali_escape():
    await kali.send("Kali破解教程:\nhttps://blog.shouzi.xyz/kali/")


pojie = on_regex("^(破解)$", block=True, aliases={
                 "电脑破解", "破解", "水滴"}, priority=5)


@pojie.handle()
async def pojie_escape():
    await pojie.send(
        "CDlinux破解教程:\nhttps://blog.shouzi.xyz/cdlinux-wifi/\n"
        "Kali破解教程:\nhttps://blog.shouzi.xyz/kali/")

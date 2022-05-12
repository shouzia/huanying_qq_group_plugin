from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.plugin import on_command

__zx_plugin_name__ = "幻影"
__plugin_usage__ = "用法： 无"
__plugin_version__ = 0.1
__plugin_author__ = 'Shouzi'

download = on_command("下载", block=True,aliases={"下载", "官网"},priority=5)


@download.handle()
async def download_escape():
    await download.send("通道h5ai:https://h5ai.108878.xyz/\n""通道官网:https://hypin.cn/download")
    
cdlinux = on_command("cdlinux", block=True,aliases={"cdlinux"},priority=5)


@cdlinux.handle()
async def cdlinux_escape():
    await cdlinux.send("CDlinux破解教程:\nhttps://blog.shouzi.xyz/cdlinux-wifi/")

kali = on_command("kali", block=True,aliases={"kali"},priority=5)


@kali.handle()
async def kali_escape():
    await kali.send("Kali破解教程:\nhttps://blog.shouzi.xyz/kali/")


pojie = on_command("破解", block=True,aliases={"电脑破解", "破解","水滴"},priority=5)


@pojie.handle()
async def pojie_escape():
    await pojie.send(
        "CDlinux破解教程:\nhttps://blog.shouzi.xyz/cdlinux-wifi/\n"
        "Kali破解教程:\nhttps://blog.shouzi.xyz/kali/")
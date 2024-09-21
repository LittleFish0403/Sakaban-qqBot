from melobot import MeloBot, BotPlugin, send, ForwardWsConn, msg_event
from melobot.models import image_msg, custom_type_msg

plugin = BotPlugin(__name__, "1.0.0")

#图片测试
@plugin.on_start_match(".image")
async def _():
    # 构造一个“图片”消息段，然后发送
    img = image_msg("https://i.pximg.net/img-original/img/2019/03/05/03/09/55/73518990_p0.png")
    await send(img)

#戳一戳测试
@plugin.on_start_match(".touch")
async def _():
    touch = custom_type_msg("touch", {"id": "1041365078"})
    await send(touch)

@plugin.on_start_match(".hello")
async def _(e = msg_event()):
    if e.sender.id != 1041365078:
        await send("滚，你不是我的主人！")
        return
    # 接下来是机器人主人的处理逻辑
    await send("Ciallo～(∠・ω＜)⌒☆,主人好!")

if __name__ == "__main__":
    bot = MeloBot(__name__)
    # 如果你的 OneBot 实现程序的服务的 host 和 port 不一致，请自行修改
    bot.init(ForwardWsConn("127.0.0.1", 3001))
    bot.load_plugin(plugin)
    bot.run()
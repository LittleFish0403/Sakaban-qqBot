from melobot import MeloBot, BotPlugin, send, ForwardWsConn, msg_event
from melobot.models import image_msg, custom_type_msg, poke_msg, reply_msg, at_msg, text_msg
from melobot.context import get_group_member_list, get_group_member_info, send_reply
import random
import datetime
from pixiv import downloadUser_urls,downloadKeyword_urls_r18,downloadKeyword_urls,downloadRanking_urls_r18
import badwords, save

plugin = BotPlugin(__name__, "1.0.0")

# 随机二次元图片，从收藏的p站画师中随机抽取一张输出
@plugin.on_start_match("/image")
async def _():
    # 构造一个“图片”消息段，然后发送
    urls = downloadUser_urls()
    url = random.choice(urls)
    img = image_msg(url)
    await send(img)

# 美图搜索，搜索方式为"/search xxx"
@plugin.on_start_match("/search")
async def _():
    # 构造一个“图片”消息段，然后发送
    e = msg_event()
    keyword = e.text[5:]
    urls = downloadKeyword_urls(keyword)
    url = random.choice(urls)
    img = image_msg(url)
    await send(img)



# R18图片获取，QQ会主动阻断涩图，现已禁用
"""
@plugin.on_start_match("/r18")
async def _():
    # 构造一个“图片”消息段，然后发送
    urls = downloadRanking_urls_r18()
    url = random.choice(urls)
    img = image_msg(url)
    await send(img)
"""
    
#戳一戳测试
@plugin.on_start_match("/touch")
async def _():
    e = msg_event()
    touch = poke_msg(qq=e.sender.id)
    await send(touch)

# xnn指令，每天抽取一个群友变成xnn
@plugin.on_start_match("/xnn")
async def _():
    event = msg_event()
    # 获取今天的日期
    today = datetime.datetime.now().date()
    
    # 读取上一次执行的日期
    last_executed_info = save.load_last_executed_info(filename=f"{event.group_id}_xnn_data.json")
    
    # 检查是否已经执行过
    if last_executed_info['date'] != today.strftime('%Y-%m-%d') :
        # 如果还没有执行过，则随机选择一个群成员
        xnn_id = 3646247300
        while xnn_id == 3646247300:
            member_list = (await get_group_member_list(event.group_id, noCache=False).resp).data
            xnn = random.choice(member_list)
            xnn_id = xnn["user_id"]

        # 保存本次执行的日期
        save.save_last_executed_info(today,xnn["user_id"],filename=f"{event.group_id}_xnn_data.json")
        
        # 发送消息到群聊
        await send([at_msg(xnn_id), text_msg(" 今天变成了香香软软的小南娘🤤🤤🤤")])
    else:
        # 如果已经执行过了，则通知用户
        await send([text_msg("今天已经抽过小南娘啦，今天抽中的群友是："),at_msg(last_executed_info['member'])])

# 早安指令
@plugin.on_start_match("/早安")
async def _(e = msg_event()):
    reply = reply_msg(e.sender.id)
    await send_reply([reply,text_msg("，早啊，早啊，早啊！")])


# 脏话提醒，被动开启，用于整治口吐芬芳或是鉴证群友
@plugin.on_contain_match(badwords.badwords)
async def _(e = msg_event()):
    at = at_msg(e.sender.id)
    await send_reply([at,text_msg("，小孩子不可以说脏话哦！😡")])


# 打招呼指令，用于测试bot是不是还活着
@plugin.on_start_match("/hello")
async def _(e = msg_event()):
    if e.sender.id != 1041365078:
        await send("Ciallo～(∠・ω＜)⌒☆，你好啊！")
        return
    # 接下来是机器人主人的处理逻辑
    await send("Ciallo～(∠・ω＜)⌒☆,主人好!")


if __name__ == "__main__":
    bot = MeloBot(__name__)
    # 如果你的 OneBot 实现程序的服务的 host 和 port 不一致，请自行修改
    bot.init(ForwardWsConn("127.0.0.1", 3001))
    bot.load_plugin(plugin)
    bot.run()

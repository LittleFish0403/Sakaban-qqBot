
from melobot import MeloBot, BotPlugin, send, ForwardWsConn, msg_event
from melobot.models import image_msg, poke_msg, reply_msg, at_msg, text_msg
import melobot
import random,datetime

import melobot.models
import badwords.badwords as badwords, utils.file as file, utils.pixiv as pixiv
from utils.handle import handle
import json
import os

plugin = BotPlugin(__name__, "1.0.0")

@plugin.on_start_match("/csd")
async def _():
    # 构造一个“图片”消息段，然后发送
    # 指定目录路径
    e = msg_event()
    print(e)
    directory = r'D:\software_inf\pycharm\python_project\youki_qqbot\out\sd'

    # 获取所有文件名并存入列表
    file_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    file_name=random.choice(file_list)
    save_path=Handle.config.get(["sd","save_path"])
    path=f"{save_path}/{file_name}"
    img = image_msg(path)
    await send(img)

# 随机二次元图片，从收藏的p站画师中随机抽取一张输出
@plugin.on_start_match("/image")
async def _():
    # 构造一个“图片”消息段，然后发送
    urls = pixiv.downloadUser_urls()
    url = random.choice(urls)
    img = image_msg(url)
    await send(img)

# 美图搜索，搜索方式为"/search xxx"
@plugin.on_start_match("/search")
async def _():
    # 构造一个“图片”消息段，然后发送
    e = msg_event()
    keyword = e.text[5:]
    urls = pixiv.downloadKeyword_urls(keyword)
    url = random.choice(urls)
    img = image_msg(url)
    await send(img)

# R18图片获取，QQ会主动阻断涩图，现已禁用
"""
@plugin.on_start_match("/r18")
async def _():
    # 构造一个“图片”消息段，然后发送
    urls = pixiv.downloadRanking_urls_r18()
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
    last_executed_info = file.load_last_executed_info(filename=f"{event.group_id}_xnn_data.json")
    
    # 检查是否已经执行过
    if last_executed_info['date'] != today.strftime('%Y-%m-%d') :
        # 如果还没有执行过，则随机选择一个群成员
        xnn_id = 3646247300
        while xnn_id == 3646247300:
            member_list = (await melobot.context.get_group_member_list(event.group_id, noCache=False).resp).data
            xnn = random.choice(member_list)
            xnn_id = xnn["user_id"]

        # 保存本次执行的日期
        file.save_last_executed_info(today,xnn["user_id"],filename=f"{event.group_id}_xnn_data.json")
        
        # 发送消息到群聊
        await send([at_msg(xnn_id), text_msg(" 今天变成了香香软软的小南娘🤤🤤🤤")])
    else:
        # 如果已经执行过了，则通知用户
        await send([text_msg("今天已经抽过小南娘啦，今天抽中的群友是："),at_msg(last_executed_info['member'])])

@plugin.on_start_match("")
async def _(e = msg_event()):
    sender_inf={"id":e.sender.id,
                "nickname":e.sender.nickname}
    print(sender_inf,e.text,type(e.text),e.content[0]["type"]=="text")
    print(e.content)
    print(e.group_id)
    if e.group_id:
        id = e.group_id
    else:
        id = e.sender.id
    #把content存入history
    #相同表情复读
    Handle.history.store_content(id,e.content[0])
    if Handle.history.history_list[str(id)][-2]["type"]==e.content[0]["type"]==("image" or "mface") and Handle.history.history_list[str(id)][-2]["data"]["file"]==e.content[0]["data"]["file"]:
        Handle.history.store_content(id,{'type': '', 'data':""})
        url=e.content[0]["data"]["url"]
        img=image_msg(url)
        await send(img)
    #相同对话复读
    elif Handle.history.history_list[str(id)][-2]["type"]==e.content[0]["type"]=="text" and Handle.history.history_list[str(id)][-2]["data"]==e.content[0]["data"]:
        Handle.history.store_content(id,{'type': '', 'data':""})
        await send(e.text)

    #判断昵称用户是否在list里，并且不是关闭事件，并且非表情包
    if sender_inf["nickname"] in Handle.youki.talker["talker_list"] and e.text!="close" and e.content[0]["type"]=="text":

        id=str(sender_inf["id"])
        if id in Handle.user_inf["user_list"]:
            identity=Handle.user_inf[id]
            response=Handle.youki.get_request(username=sender_inf["nickname"],identity=identity,msg=e.text)
        else:
            response=Handle.youki.get_request(username=sender_inf["nickname"],identity="朋友",msg=e.text)

        await send(response)
        if Handle.config.get(["enable","audio"]):
            audio_path = await Handle.audio.get_audio_path(response)  # Await the async method
            record = melobot.models.record_msg(audio_path)
            await send(record)
        
        """
        elif e.content[0]["type"]==("image" or "mface"):
            url=e.content[0]["data"]["url"]
            img=image_msg(url)
            await send(img)
        """
# 早安指令
@plugin.on_start_match("/早安")
async def _(e = msg_event()):
    reply = reply_msg(e.sender.id)
    await melobot.context.send_reply([reply,text_msg("，早啊，早啊，早啊！")])


# 脏话提醒，被动开启，用于整治口吐芬芳或是鉴证群友
@plugin.on_contain_match(badwords.badwords)
async def _(e = msg_event()):
    at = at_msg(e.sender.id)
    await melobot.context.send_reply([at,text_msg(",小楚南杂鱼又说脏话，杂鱼~~杂鱼~~")])

# 打招呼指令，用于测试bot是不是还活着
@plugin.on_start_match("/hello")
async def _(e = msg_event()):
    if e.sender.id != 1041365078:
        await send("Ciallo～(∠・ω＜)⌒☆，你好啊！")
        return
    # 接下来是机器人主人的处理逻辑
    await send("Ciallo～(∠・ω＜)⌒☆,主人好!")


if __name__ == "__main__":
    Handle=handle("config.json")
    bot = MeloBot(__name__)
    # 如果你的 OneBot 实现程序的服务的 host 和 port 不一致，请自行修改
    bot.init(ForwardWsConn("127.0.0.1", 3001))
    bot.load_plugin(plugin)
    bot.run()

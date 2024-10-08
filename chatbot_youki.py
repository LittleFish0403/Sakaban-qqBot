
from melobot import MeloBot, BotPlugin, send, ForwardWsConn, msg_event
from melobot.models import image_msg, poke_msg, reply_msg, at_msg, text_msg,record_msg,face_msg
import melobot
import random,datetime
import badwords.badwords as badwords
import json, os, requests
from utils.handle import handle
import utils.file as file

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

@plugin.on_start_match("/sd1")
async def _():
    # 构造一个“图片”消息段，然后发送
    if Handle.config:
        e = msg_event()
        prompt = e.text
        print("sd prompt:",prompt[4:])
        prompt=prompt[4:]
        Handle.sd.process_input(prompt)
        now_img_name=Handle.sd.now_img_name
        print("sd finish")
        save_path=Handle.config.get(["sd","save_path"])
        path=f"{save_path}/{now_img_name}"
        img = image_msg(path)
        await send(img)
    else:
        await send([text_msg("杂鱼主人没开SD，杂鱼~~杂鱼~~")])


@plugin.on_start_match("/sd2")
async def _():
    # 构造一个“图片”消息段，然后发送
    if Handle.config:
        e = msg_event()
        prompt = e.text
        print("sd prompt:",prompt[4:])
        prompt=prompt[4:]
        Handle.sd.process_input_2(prompt)
        now_img_name=Handle.sd.now_img_name
        print("sd finish")
        save_path=Handle.config.get(["sd","save_path"])
        path=f"{save_path}/{now_img_name}"
        img = image_msg(path)
        await send(img)
    else:
        await send([text_msg("杂鱼主人没开SD，杂鱼~~杂鱼~~")])


# 脏话提醒，被动开启，用于整治口吐芬芳或是鉴证群友
@plugin.on_contain_match(badwords.badwords)
async def _(e = msg_event()):
    at = at_msg(e.sender.id)
    await melobot.context.send_reply([at,text_msg(",小楚南杂鱼又说脏话，杂鱼~~杂鱼~~")])

@plugin.on_start_match("/fac")
async def _(e = msg_event()):
        face = face_msg("73569241a1aa4ebe0d6512a628e1c23b")
        await send(face)
        
# 通配
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
            record = record_msg(audio_path)
            await send(record)
        
        """
        elif e.content[0]["type"]==("image" or "mface"):
            url=e.content[0]["data"]["url"]
            img=image_msg(url)
            await send(img)
        """

@plugin.on_start_match("/img")
async def _(e=msg_event()):
    folder_path = r"D:\software_inf\pycharm\python_project\youki_qqbot\out\image"  # 替换为你要指定的文件夹路径
    random_file = file.select_random_file(folder_path)
    img=image_msg(random_file)
    await send(img)

@plugin.on_start_match("/say")
async def _(e=msg_event()):
    content = e.text[4:]  # Extract content
    audio_path = await Handle.audio.get_audio_path(content)  # Await the async method

    print(audio_path)
    record = record_msg(audio_path)
    await send(record)
@plugin.on_at_qq("youki")
async def _(e = msg_event()):
    sender_inf={"id":e.sender.id,
                "nickname":e.sender.nickname}
    #判断对话人身份
    id=str(sender_inf["id"])
    if id in Handle.user_inf["user_list"]:
        identity=Handle.user_inf[id]
        response=Handle.youki.get_request(username=sender_inf["nickname"],identity=identity,msg=e.text)
    else:
        response=Handle.youki.get_request(username=sender_inf["nickname"],identity="朋友",msg=e.text)

    at = at_msg(e.sender.id)
    await melobot.context.send_reply([at,text_msg(response)])
@plugin.on_contain_match(["youki","初雪"])
async def _(e = msg_event()):
    #sender id nickname 
    sender_inf={"id":e.sender.id,
                "nickname":e.sender.nickname}

    if sender_inf["nickname"] not in Handle.youki.talker["talker_list"]:
        Handle.youki.talker["talker_list"].append(sender_inf["nickname"])
        Handle.youki.talker[sender_inf["nickname"]]=sender_inf["id"]
        id=str(sender_inf["id"])
        if id in Handle.user_inf["user_list"]:
            identity=Handle.user_inf[id]
            response=Handle.youki.get_request(username=sender_inf["nickname"],identity=identity,msg=e.text)
        else:
            response=Handle.youki.get_request(username=sender_inf["nickname"],identity="朋友",msg=e.text)

        await send(response)
        if Handle.config.get(["enable","audio"]):
            audio_path = await Handle.audio.get_audio_path(response)  # Await the async method
            record = record_msg(audio_path)
            await send(record)
@plugin.on_contain_match(["拜拜","再见","下次见"])
async def _(e = msg_event()):
    sender_inf={"id":e.sender.id,
                "nickname":e.sender.nickname}
    try:
        del Handle.youki.talker[sender_inf["nickname"]]
        Handle.youki.talker["talker_list"].remove(sender_inf["nickname"])
    except:
        pass

@plugin.on_start_match("close")
async def _(e = msg_event()):
    sender_inf={"id":e.sender.id,
                "nickname":e.sender.nickname}
    try:
        del Handle.youki.talker[sender_inf["nickname"]]
        Handle.youki.talker["talker_list"].remove(sender_inf["nickname"])
    except:
        pass



if __name__ == "__main__":

    Handle=handle("config.json")
    bot = MeloBot(__name__)
    # 如果你的 OneBot 实现程序的服务的 host 和 port 不一致，请自行修改
    bot.init(ForwardWsConn("127.0.0.1", 3001))
    bot.load_plugin(plugin)
    bot.run()

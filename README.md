# Sakaban-qqBot

## 项目介绍
一个基于melobot的qqbot，用于好友群聊骚

## 项目使用
版本：python>=3.10,我用的3.10
所需库安装：见requirements


要开sd的话把config里的enable改成true
llm请自行到utils.youki 完成对接，我懒
把spark3.5的id，key，secret填入config(不开sd就不用填了)
sd可以用秋叶包开下api，原生webui也行
audio用的gpt-so-vits，用别的的话，去utils.audio里完成对接


运行demo.py

## 项目计划
- [ ] 基础指令集
    - [ ] /hello 打招呼
    - [ ] /luck 今日运势
    - [ ] waiting...
- [ ] 被动 复读功能
- [ ] /image 每日更新涩图
- [ ] /meal 今天吃什么
- [ ] /xnn 每天抽一位群友当群男娘
- [ ] /sd1 英文提示词sd绘图
- [ ] /sd2 中文提示词sd绘图(spark做提示词增强)
- [ ] /csd 随机抽一张之前sd的图


## 其他
如有问题，及时联系
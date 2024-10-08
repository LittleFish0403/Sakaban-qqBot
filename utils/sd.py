
import webuiapi
from PIL import Image
import numpy as np
import time
import logging
from sparkai.llm.llm import ChatSparkLLM
from sparkai.core.messages import ChatMessage
import asyncio, os
import json
from datetime import datetime
from typing import List, Iterable
from utils.config import config


class sd:
    def __init__(self, path): 
        self.config=config(path)
        self.new_img = None
        self.sd_config = self.config.get(["sd"])
        self.now_img_name=""
        self.app_id = self.config.get(["spark","id"])
        self.app_key = self.config.get(["spark","key"])
        self.app_secret = self.config.get(["spark","secret"])
        self.spark_model=self.ChatModel(self.app_id, self.app_key, self.app_secret, stream=True)

        try:
            # 创建 API 客户端
            self.api = webuiapi.WebUIApi(host=self.sd_config["ip"], port=self.sd_config["port"])

        except Exception as e:
            logging.error(e)


    def save_image_locally(self, img):
        # 确保有一个用于保存图片的目录
        save_dir = self.sd_config["save_path"]
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        from datetime import datetime

        # 获取当前的日期和时间
        now = datetime.now()

        # 打印当前的日期和时间，包括微秒
        print("当前时间:", now)

        #   获取精确的时间组件
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f'{now}.png'

        # 保存图片
        img_path = os.path.join(save_dir, filename)
        img.save(img_path)
        self.now_img_name=filename
        logging.info(f"图片保存在：{img_path}")

    def process_input(self, user_input):

        prompt=self.sd_config["positive_prompt"]+user_input

        # 使用用户输入的文本作为 prompt 调用 API
        """
            prompt：主要文本提示，用于指定生成图像的主题或内容。
            negative_prompt：负面文本提示，用于指定与生成图像相矛盾或相反的内容。
            seed：随机种子，用于控制生成过程的随机性。可以设置一个整数值，以获得可重复的结果。
            styles：样式列表，用于指定生成图像的风格。可以包含多个风格，例如 ["anime", "portrait"]。
            cfg_scale：提示词相关性，无分类器指导信息影响尺度(Classifier Free Guidance Scale) -图像应在多大程度上服从提示词-较低的值会产生更有创意的结果。
            sampler_index：采样器索引，用于指定生成图像时使用的采样器。默认情况下，该参数为 None。
            steps：生成图像的步数，用于控制生成的精确程度。
            enable_hr：是否启用高分辨率生成。默认为 False。
            hr_scale：高分辨率缩放因子，用于指定生成图像的高分辨率缩放级别。
            hr_upscaler：高分辨率放大器类型，用于指定高分辨率生成的放大器类型。
            hr_second_pass_steps：高分辨率生成的第二次传递步数。
            hr_resize_x：生成图像的水平尺寸。
            hr_resize_y：生成图像的垂直尺寸。
            denoising_strength：去噪强度，用于控制生成图像中的噪点。
        """
        result = self.api.txt2img(prompt=prompt,
            negative_prompt=self.sd_config["negative_prompt"],
            seed=self.sd_config["seed"],
            styles=self.sd_config["styles"],
            cfg_scale=self.sd_config["cfg_scale"],
            # sampler_index='DDIM',
            steps=self.sd_config["steps"],
            enable_hr=self.sd_config["enable_hr"],
            hr_scale=self.sd_config["hr_scale"],
            # hr_upscaler=webuiapi.HiResUpscaler.Latent,
            hr_second_pass_steps=self.sd_config["hr_second_pass_steps"],
            hr_resize_x=self.sd_config["hr_resize_x"],
            hr_resize_y=self.sd_config["hr_resize_y"],
            denoising_strength=self.sd_config["denoising_strength"],
        )

        try:
            # 获取返回的图像
            img = result.image
            self.new_img = img

            # 保存图片到本地
            if self.sd_config["save_enable"]:
                self.save_image_locally(img)
        except Exception as e:
            logging.error(e)
            return None
        
    def process_input_2(self, user_input):

        prompt=self.sd_config["positive_prompt"]+self.spark_model.run_infer(user_input)

        # 使用用户输入的文本作为 prompt 调用 API
        result = self.api.txt2img(prompt=prompt,
            negative_prompt=self.sd_config["negative_prompt"],
            seed=self.sd_config["seed"],
            styles=self.sd_config["styles"],
            cfg_scale=self.sd_config["cfg_scale"],
            # sampler_index='DDIM',
            steps=self.sd_config["steps"],
            enable_hr=self.sd_config["enable_hr"],
            hr_scale=self.sd_config["hr_scale"],
            # hr_upscaler=webuiapi.HiResUpscaler.Latent,
            hr_second_pass_steps=self.sd_config["hr_second_pass_steps"],
            hr_resize_x=self.sd_config["hr_resize_x"],
            hr_resize_y=self.sd_config["hr_resize_y"],
            denoising_strength=self.sd_config["denoising_strength"],
        )

        try:
            # 获取返回的图像
            img = result.image
            self.new_img = img

            # 保存图片到本地
            if self.sd_config["save_enable"]:
                self.save_image_locally(img)
        except Exception as e:
            logging.error(e)
            return None
    class ChatModel:
        def __init__(self, app_id: str, app_key: str, app_secret: str, stream: bool = False,
                 domain: str = 'generalv3.5', model_url: str = 'wss://spark-api.xf-yun.com/v3.5/chat'):
            self.spark = ChatSparkLLM(
                spark_api_url=model_url,
                spark_app_id=app_id,
                spark_api_key=app_key,
                spark_api_secret=app_secret,
                spark_llm_domain=domain,
                streaming=stream,
            )
            self.stream = stream

        def generate_stream(self, msgs: str | List[ChatMessage]) -> Iterable[str]:
            if not self.stream:
                raise Exception('Model initialized for streaming output, use generate method instead')
            

            system_messages = {
                0: "角色设定：你是一个AI绘画助手，你是一个翻译官"
                "任务：你要把输入的中文，做创造性的扩充，把每个元素用(,)逗号来分割,元素包含(主体人物，风景，颜色，细节，形容词，描述词)可以给每个元素加权重，如(可爱:1.3),不要分段，不要出现完整的句子，用短语回答，不要超过一百字，输出请使用英文"
                "输出使用英语，禁止出现中文，简短一些，用一些，禁止出现长句，可以给每个元素加权重，如(可爱:1.3)",
            }

            messages = [ChatMessage(role="system", content=system_messages[0])]
            messages += self.__trans_msgs(msgs)
            
        
            resp_iterable = self.spark.stream(messages)
            
            for resp in resp_iterable:
                
                yield resp.content

        def __trans_msgs(self, msg: str):
            if isinstance(msg, str):
                return [ChatMessage(role="user", content=msg)]
            return msg
        


        def run_infer(self,prompt):
            try:   
                response=""
                print("prompt",prompt)
                for chunk_text in self.generate_stream(prompt):
                    response += chunk_text
                return response
            except:
                print('[WARNING] ')


if __name__=="__main__":
    with open("config.json","r",encoding="utf-8") as f:
        config=json.load(f)
    sd=SD(config["sd"])
    prompt="猫娘在厨房里偷吃"
    sd.process_input_2(prompt)

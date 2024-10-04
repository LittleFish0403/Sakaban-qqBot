import json, logging, os
import aiohttp
import traceback
import base64
import mimetypes
import websockets
import asyncio
from utils.config import config
class audio:
    def __init__(self,path):
        self.count=0
        self.config=config(path)


    async def run(self,content):
        data = {
        "type": self.config.get(["gpt_sovits","type"]),
        "ws_ip_port": self.config.get(["gpt_sovits","ws_ip_port"]),
        "api_ip_port": self.config.get(["gpt_sovits","api_ip_port"]),
        "ref_audio_path": self.config.get(["gpt_sovits","ref_audio_path"]),
        "prompt_text": self.config.get(["gpt_sovits","prompt_text"]),
        "prompt_language": self.config.get(["gpt_sovits","prompt_language"]),
        "language": "auto",
        "cut": self.config.get(["gpt_sovits","cut"]),
        "webtts": self.config.get(["gpt_sovits","webtts"]),
        "content": content
        }

        try:
            voice_tmp_path = await self.gpt_sovits_api(data)
            return voice_tmp_path
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    # Entry point for the async function

    async def get_audio_path(self, content):
        audio_path = await self.run(content)  # Await the async method
        self.count += 1
        if self.count >= 100:
            self.count = 0
        return audio_path



    async def gpt_sovits_api(self, data):

        def file_to_data_url(file_path):
            # 根据文件扩展名确定 MIME 类型
            mime_type, _ = mimetypes.guess_type(file_path)

            # 读取文件内容
            with open(file_path, "rb") as file:
                file_content = file.read()

            # 转换为 Base64 编码
            base64_encoded_data = base64.b64encode(file_content).decode('utf-8')

            # 构造完整的 Data URL
            return f"data:{mime_type};base64,{base64_encoded_data}"

        async def websocket_client(data_json):
            try:
                async with websockets.connect(data["ws_ip_port"]) as websocket:
                    # 设置最大连接时长（例如 30 秒）
                    return await asyncio.wait_for(websocket_client_logic(websocket, data_json), timeout=30)
            except asyncio.TimeoutError:
                logging.error("gpt_sovits WebSocket连接超时")
                return None

        async def websocket_client_logic(websocket, data_json):
            async for message in websocket:
                logging.debug(f"Received message: {message}")

                # 解析收到的消息
                data = json.loads(message)
                # 检查是否是预期的消息
                if "msg" in data:
                    if data["msg"] == "send_hash":
                        # 发送响应消息
                        response = json.dumps({"session_hash":"3obpzfqql7f","fn_index":3})
                        await websocket.send(response)
                        logging.debug(f"Sent message: {response}")
                    elif data["msg"] == "send_data":
                        # audio_path = "F:\\GPT-SoVITS\\raws\\ikaros\\1.wav"
                        audio_path = data_json["ref_audio_path"]

                        # 发送响应消息
                        response = json.dumps(
                            {
                                "session_hash":"3obpzfqql7f",
                                "fn_index":3,
                                "data":[
                                    {
                                        "data": file_to_data_url(audio_path),
                                        "name": os.path.basename(audio_path)
                                    },
                                    data_json["prompt_text"], 
                                    data_json["prompt_language"], 
                                    data_json["content"], 
                                    data_json["language"],
                                    data_json["cut"]
                                ]
                            }
                        )
                        await websocket.send(response)
                        logging.debug(f"Sent message: {response}")
                    elif data["msg"] == "process_completed":
                        return data["output"]["data"][0]["name"]
                    
        try:
            logging.debug(f"data={data}")
            
            if data["type"] == "api":
                try:
                    data_json = {
                        "refer_wav_path": data["ref_audio_path"],
                        "prompt_text": data["prompt_text"],
                        "prompt_language": data["prompt_language"],
                        "text": data["content"],
                        "text_language": data["language"]
                    }
                                        
                    async with aiohttp.ClientSession() as session:
                        async with session.post(data["api_ip_port"], json=data_json, timeout=30) as response:
                            response = await response.read()
                            
                            file_name = 'gpt_sovits_' + str(self.count) + '.wav'

                            voice_tmp_path = self.config.get(["gpt_sovits","save_path"])+file_name

                            with open(voice_tmp_path, 'wb') as f:
                                f.write(response)

                            return voice_tmp_path
                except aiohttp.ClientError as e:
                    logging.error(traceback.format_exc())
                    logging.error(f'gpt_sovits请求失败: {e}')
                except Exception as e:
                    logging.error(traceback.format_exc())
                    logging.error(f'gpt_sovits未知错误: {e}')
            
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.error(f'gpt_sovits未知错误，请检查您的gpt_sovits推理是否启动/配置是否正确，报错内容: {e}')
        
        return None
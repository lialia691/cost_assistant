import requests
import json
import re



class AiChatModel():
    def __init__(self,user_input):
        self.user_input= user_input
        
        
###增加ai
    def ai_chat(self):
            # 初始化 ai_response 变量
        ai_response = ""
        # 调用扣子 API
        api_url = 'https://api.coze.cn/open_api/v2/chat'
        headers = {
            'Authorization': 'Bearer pat_juaBtToJ0OTdMzRy0BMheS4xIEasHiGO9JJaBwqTngZoikR2RdtcbHedLRqriHud',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Host': 'api.coze.cn',
            'Connection': 'keep-alive'
        }
        data = {
            "conversation_id": "123",
            "bot_id": "7380347095159111731",  # 替换为你的 Bot ID
            "user": "123333333",
            "query": self.user_input,
            "stream": False  #如果未指定值或设置为 false，则采用非流式响应。 “非流式响应”是指所有响应全部准备好后再返回给客户端，客户端不需要拼接内容。
        }
        try:
            response = requests.post(api_url, headers=headers, json=data)
            if response.status_code == 200:
                response_json=response.json()
                messages = response_json.get('messages', [])
                ai_response = self.extract_content(messages)
            else:
                ai_response = f"请求失败，状态码: {response.status_code}"
        except requests.RequestException as e:
            ai_response = f"网络请求异常: {str(e)}"        
        return  ai_response  
     

    def extract_content(self,messages):
        ai_response_conclusion = " "  # 初始化为空字符串
        ai_response_According = " "
        for message in messages:
            if message['type'] == 'answer':
                if message['content_type'] == 'text':
                    ai_response_conclusion +=message['content'] + "\n"
                elif message['content_type'] == 'card':
                    # 使用 findall 提取所有标题、链接和参考内容
                    titles = re.findall(r'"title\\":\\"([^"]+)', message['content'])
                    links = re.findall(r'"link\\":\\"([^"]+)', message['content'])
                    references = re.findall(r'"reference\\":\\"([^"]+)', message['content'])
                    # 获取最长列表的长度，用于迭代
                    max_length = max(len(titles), len(links), len(references))
                    card_infos = []
                    for i in range(max_length):
                        card_info = {}
                        # 尝试获取每个列表中的元素，如果不存在则跳过
                        if i < len(titles):
                            card_info['title'] = titles[i].replace('\\', '')
                        if i < len(links):
                            card_info['link'] = links[i].replace('\\', '')
                        if i < len(references):
                            card_info['reference'] = references[i].replace('\\', '')                       
                        # 仅当字典非空时，将其添加到列表中
                        if card_info:
                            card_infos.append(card_info)
                    # 格式化输出列表中的每个字典信息
                    for info in card_infos:
                        if 'title' in info:
                            ai_response_According+=f"\n名称：{info['title']}\n"
                        if 'link' in info:
                            ai_response_According+=f"[网址]({info['link']})\n"
                        if 'reference' in info:
                            ai_response_According+=f"内容：{info['reference']}\n"
            # 将换行符替换为HTML的换行标签
        ai_response_conclusion = ai_response_conclusion.replace("\n", "<br>")
        ai_response_According = ai_response_According.replace("\n", "<br>")
        return ai_response_conclusion ,ai_response_According
        
if __name__== "__main__":
    user_input='C30的单价是多少'
    ai_1=AiChatModel(user_input)
    myai=ai_1.ai_chat()
    print(myai)





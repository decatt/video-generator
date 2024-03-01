from modelscope import AutoTokenizer, AutoModel, snapshot_download
import json
import time
import re
import numpy as np

class LLMAgent:
    def __init__(self):
        self.model_dir = snapshot_download("ZhipuAI/chatglm3-6b", revision = "v1.0.0")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_dir, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(self.model_dir, trust_remote_code=True).half().cuda()
        self.model = self.model.eval()
        self.history = []
        self.relu = ''
        self.define_rules()


    def define_rules(self):
        rule = ''
        rule += '我将给你提供一个小说章节，请给出你认为小说章节中的重要的几个画面。'
        rule += '为每一个画面给出至少3个描述画面的关键词。'
        rule += '你明白吗？'
        response, self.history = self.model.chat(self.tokenizer, rule, history=self.history)
        self.relu = self.history
        print(response)

    def get_keywords(self, text):
        response, self.history = self.model.chat(self.tokenizer, text, history=self.relu)
        return response
    
if __name__ == '__main__':
    agent = LLMAgent()
    text_path = 'text.txt'
    text = ''
    with open(text_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().replace('\n', ' ') 
            text += line + ' '
    print(agent.get_keywords(text))
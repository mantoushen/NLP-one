"""
中文分词技术
编辑者：馒头
博客：https://www.cnblogs.com/mantou0/
"""
# 逆向最大匹配法
class RMM(object):
    def __init__(self):
        self.windowSize = 3 # 词典中最长的词的词长
        self.dic = ["研究","研究生","生命","命","的","起源"] # 词典
    def cut(self,text):
        result = [] # 存放分割出的词
        index = len(text) # 初始化进行要分割的词的初始索引
        while index > 0:
            for size in range(index - self.windowSize,index):
                piece = text[size:index]
                if piece in self.dic:
                    index = size + 1
                    break
            index = index - 1
            result.append(piece+"---")
        result.reverse()
        print(result)


if __name__ == '__main__':
    text = "研究生命的起源"
    tokenizer = RMM()
    tokenizer.cut(text)
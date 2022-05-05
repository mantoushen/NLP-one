"""
中文分词技术
编辑者：馒头
博客：https://www.cnblogs.com/mantou0/
"""
class M(object):
    def __init__(self):
        self.windowSize = 3 # 词典中最长的词的词长
        self.dic = ["研究","研究生","生命","命","的","起源"] # 词典

    #正向最大匹配算法
    def MM(self,text):
        result = [] # 存放分割出的词
        index = 0 # 初始化进行要分割的词的初始索引
        text_length = len(text)
        while text_length > index:
            for size in range(self.windowSize+index,index,-1):
                piece = text[index:size]
                if piece in self.dic:
                    index = size -1
                    break
            index = index + 1
            result.append(piece+"---")
        return result

    #逆向最大匹配算法
    def RMM(self, text):
        result = []  # 存放分割出的词
        index = len(text)  # 初始化进行要分割的词的初始索引
        while index > 0:
            for size in range(index - self.windowSize, index):
                piece = text[size:index]
                if piece in self.dic:
                    index = size + 1
                    break
            index = index - 1
            result.append(piece + "---")
        result.reverse()
        return result

    def BMM(self, MM_result,RMM_result):
        """
           比较两个分词方法分词的结果

           比较方法:
               1. 如果正反向分词结果词数不同，则取分词数量较少的那个
               2. 如果分词结果词数相同：
                   2.1 分词结果相同，说明没有歧义，可返回任意一个
                   2.2 分词结果不同，返回其中单字较少的那个

           :param MM_result: 正向最大匹配法的分词结果
           :param RMM_result: 逆向最大匹配法的分词结果
           :return:
               1.词数不同返回词数较少的那个
               2.词典结果相同，返回任意一个(MM_result)
               3.词数相同但是词典结果不同，返回单字最少的那个
           """
        if len(MM_result) != len(RMM_result):
            # 如果两个结果词数不同，返回词数较少的那个
            return MM_result if (len(MM_result) < len(RMM_result)) else RMM_result
        else:
            if MM_result == RMM_result:
                # 因为RMM的结果是取反了的，所以可以直接匹配
                # 词典结果相同，返回任意一个
                return MM_result
            else:
                # 词数相同但是词典结果不同，返回单字最少的那个
                MM_word_1 = 0
                RMM_word_1 = 0
                for word in MM_result:
                    # 判断正向匹配结果中单字出现的词数
                    if len(word) == 1:
                        MM_word_1 += 1

                for word in RMM_result:
                    # 判断逆向匹配结果中单字出现的词数
                    if len(word) == 1:
                        RMM_word_1 += 1

                if (MM_word_1 < RMM_word_1):
                    return MM_result
                else:
                    return RMM_result

if __name__ == '__main__':
    text = "研究生命的起源"
    token = M()
    token.BMM(token.MM(text),token.RMM(text))
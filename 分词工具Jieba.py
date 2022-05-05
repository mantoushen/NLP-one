"""
中文分词技术
编辑者：馒头
博客：https://www.cnblogs.com/mantou0/
"""
import jieba
sent = '中文分词工具是文本处理不可或缺的一步！'
seg_list = jieba.cut(sent,cut_all=True)
print('全模式:','/'.join(seg_list))
seg_list = jieba.cut(sent,cut_all=False)
print('精准模式:','/'.join(seg_list))
seg_list = jieba.cut(sent)
print('默认精准模式:','/'.join(seg_list))
seg_list = jieba.cut_for_search(sent)
print('搜索引擎模式:','/'.join(seg_list))


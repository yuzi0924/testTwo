# 原始贝叶斯

# # 共含6个文档
# import bayes as bayes
#
# ListOPosts = [['my', 'dog', 'has', 'flea',
#                'problems', 'help', 'please'],
#               ['maybe', 'not', 'take', 'him',
#                'to', 'dog', 'park', 'stupid'],
#               ['my', 'dalmation', 'is', 'so', 'cute',
#                'I', 'love', 'him'],
#               ['stop', 'posting', 'stupid',
#                'worthless', 'garbage'],
#               ['mr', 'licks', 'ate', 'my', 'steak', 'how',
#                'to', 'stop', 'him'],
#               ['quit', 'buying', 'worthless',
#                'dog', 'food', 'stupid']]
#
# # 对应上面六个文档的类别，1代表侮辱性文字，0代表正常言论
# ListClasses = [0, 1, 0, 1, 0, 1]
#
# # 对上面文档中的单词进行拆分，创建一个不重复的词汇列表
# myVocabList = ['cute', 'love', 'help', 'garbage', 'quit', 'I', 'problems', 'is' 'park',
#                'stop', 'flea', 'dalmatian', 'licks', 'food', 'not', 'him', 'buying',
#                'posting', 'has', 'worthless', 'ate', 'to', 'maybe', 'please', 'dog',
#                'how', 'stupid', 'so', 'take', 'mr', 'steak', 'my']
#
#
# # 该函数记录输入文本中出现在词汇表中的单词的个数
# # 其中vocabList为词汇表，inputSet为输入文本
# def setOfWords2Vec(vocabList, inputSet):
#     returnVec = [0] * len(vocabList)
#     for word in inputSet:
#         if word in vocabList:
#             returnVec[vocabList.index(word)] += 1
#         else:
#             print("the word： %s is not in my Vocabulary! " % word)
#     return returnVec
#
#
# # x = setOfWords2Vec(myVocabList, ListOPosts[0])
# # y = setOfWords2Vec(myVocabList, ListOPosts[3])
# print(setOfWords2Vec(myVocabList, ListOPosts[0]))
# print(setOfWords2Vec(myVocabList, ListOPosts[1]))
# print(setOfWords2Vec(myVocabList, ListOPosts[2]))
# print(setOfWords2Vec(myVocabList, ListOPosts[3]))
# print(setOfWords2Vec(myVocabList, ListOPosts[4]))
# print(setOfWords2Vec(myVocabList, ListOPosts[5]))
# print(len(myVocabList))

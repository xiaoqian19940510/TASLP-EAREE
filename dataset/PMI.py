# coding=utf-8

class PMI:
    def __init__(self, document):
        self.document = document
        self.pmi = {}
        self.miniprobability = float(1.0) / document.__len__()
        self.minitogether = float(0)/ document.__len__()
        self.set_word = self.getset_word()

    def calcularprobability(self, document, wordlist):

        """
        :param document:
        :param wordlist:
        :function : 计算单词的document frequency
        :return: document frequency
        """

        total = document.__len__()
        number = 0
        for doc in document:
            if set(wordlist).issubset(doc):
                number += 1
        percent = float(number)/total
        return percent

    def togetherprobablity(self, document, wordlist1, wordlist2):

        """
        :param document:
        :param wordlist1:
        :param wordlist2:
        :function: 计算单词的共现概率
        :return:共现概率
        """

        joinwordlist = wordlist1 + wordlist2
        percent = self.calcularprobability(document, joinwordlist)
        return percent

    def getset_word(self):

        """
        :function: 得到document中的词语词典
        :return: 词语词典
        """
        list_word = []
        for doc in self.document:
            list_word = list_word + list(doc)
        set_word = []
        for w in list_word:
            if set_word.count(w) == 0:
                set_word.append(w)
        return set_word

    def get_dict_frq_word(self):

        """
        :function: 对词典进行剪枝,剪去出现频率较少的单词
        :return: 剪枝后的词典
        """
        dict_frq_word = {}
        for i in range(0, self.set_word.__len__(), 1):
            list_word=[]
            list_word.append(self.set_word[i])
            probability = self.calcularprobability(self.document, list_word)
            if probability > self.miniprobability:
                dict_frq_word[self.set_word[i]] = probability
        return dict_frq_word

    def calculate_nmi(self, joinpercent, wordpercent1, wordpercent2):
        """
        function: 计算词语共现的nmi值
        :param joinpercent:
        :param wordpercent1:
        :param wordpercent2:
        :return:nmi
        """
        return (joinpercent)/(wordpercent1*wordpercent2)

    def get_pmi(self):
        """
        function:返回符合阈值的pmi列表
        :return:pmi列表
        """
        dict_pmi = {}
        dict_frq_word = self.get_dict_frq_word()
        for word1 in dict_frq_word:
            wordpercent1 = dict_frq_word[word1]
            for word2 in dict_frq_word:
                if word1 == word2:
                    continue
                wordpercent2 = dict_frq_word[word2]
                list_together=[]
                list_together.append(word1)
                list_together.append(word2)
                together_probability = self.calcularprobability(self.document, list_together)
                if together_probability > self.minitogether:
                    string = word1 + ',' + word2
                    dict_pmi[string] = self.calculate_nmi(together_probability, wordpercent1, wordpercent2)
        return dict_pmi
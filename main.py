import math
import csv

data_set_row = []
with open('dataset.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data_set_row.append(row[0])

print(data_set_row)

############# Read Text File ######################

stop_words_list = []
with open('stopwords.txt') as f:
    stop_words_list = f.readlines()
############# Remove \n  ######################
stop_words = []
for i in stop_words_list:
    stop_words.append(i.strip('\n'))

final_dataSet_list = []
for row in data_set_row:
    querywords = row.split()
    resultwords = [word for word in querywords if word.lower() not in stop_words]
    result = ' '.join(resultwords)
    final_dataSet_list.append(result)

single_str = ""
single_str = ' '.join(final_dataSet_list)   #replace in string so we convert it in string


single_str = single_str.replace(",", "")
single_str = single_str.replace(".", "")
single_str = single_str.replace(":", "")
single_str = single_str.replace("!", "")
single_str = single_str.replace("?", "")
single_str = single_str.replace('"', "")
splited_str = single_str.split(" ")
word_dict = dict()
unique_words = []
for i in splited_str:
    length = splited_str.count(i)
    if length <= 1:
        unique_words.append(i)
    else:
        word_dict[i] = splited_str.count(i)


def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict


def IDF(corpus, unique_words):
    idf_dict = {}
    N = len(corpus)
    for i in unique_words:
        count = 0
        for sen in corpus:
            if i in sen.split():
                count = count + 1
            idf_dict[i] = (math.log((1 + N) / (count + 1))) + 1
    return idf_dict


print("IDF: \n", IDF(word_dict, unique_words))
print("\n")
print("TF:\n", computeTF(word_dict, unique_words))
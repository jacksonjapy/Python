import jieba

if __name__ == '__main__':
    path = r"三国演义.txt"
    # 打开文件
    f = open(path, 'r', encoding='utf-8')
    # 操作文件
    s = f.read()
    # 关闭文件
    f.close()

    # 分词
    words = jieba.lcut(s)
    # 统计
    count_words = set(words) - {"\n", "（", "、", "，", "。", "）"}  # 确定统计对象并去重和去掉符号
    count_result = {}  # 统计结果
    for word in count_words:
        count_result[word] = words.count(word)  # 每循环一次统计一个词语
    # 排序
    sorted_result = sorted(count_result.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_result:
        print(f"{word}:{count}")

import datetime

if __name__ == '__main__':
    tips = ["星期一：坚持下去不是因为我很坚强，而是因为我别无选择。",
            "星期二：含泪播种的人一定能笑着收获。",
            "星期三：做对的事情比把事情做对重要。",
            "星期四：命运给予我们的不是失望之酒，而是机会之杯。",
            "星期五：不要等到明天，明天太遥远，今天就行动。",
            "星期六：求知若饥，虚心若愚。",
            "星期日：成功将属于那些从不说“不可能”的人。"]
    today = datetime.datetime.now().weekday() #该方法获取的信息为0,1,2,3……，十分方便
    print(tips[today])
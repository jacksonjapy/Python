from csv import DictWriter

if __name__ == '__main__':
    file_path = r"test.csv"
    data = [{"班级": "信安22-1", "姓名": "test", "学号": "22705000"}]
    try:
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            writer = DictWriter(f, fieldnames=["班级", "姓名", "学号"])
            writer.writeheader()  # 写入表头
            writer.writerows(data)  # 写入数据(多行写入，单行写入为writer.writerow())
    except PermissionError:
        print("文件被占用，请关闭文件后再试")

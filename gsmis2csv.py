import json

# 将loadXskbData.do请求的预览中，jgList的值复制到此处
json_data = '''

'''


def translate_weeks(week_string):
    start = None
    end = None
    result = []

    for i in range(len(week_string)):
        if week_string[i] == '1':
            if start is None:
                start = i + 1  # 找到起始点
            end = i + 1  # 更新终止点
        elif start is not None:
            # 当前是 '0' 并且之前有起始点
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")
            start = None
            end = None

    # 处理字符串末尾的连续 '1'
    if start is not None:
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}-{end}")

    return "、".join(result)


def main():
    # 解析JSON数据
    data = json.loads(json_data)

    seen_ids = set()

    # 打开CSV文件准备写入
    with open('output.csv', mode='w', newline='') as csv_file:
        csv_file.write('课程名称,星期,开始节数,结束节数,老师,地点,周数\n')

        # 写入数据
        for row in data:
            wid = row['WID']
            if wid not in seen_ids:
                seen_ids.add(wid)
            else:
                continue

            csv_file.write(
                f"\"{row['KCMC']}\",{row['XQ']},{row['KSJCDM']},{row['KSJCDM']},\"{str(row['JGJSXM'])}\",\"{row['JASMC']}\","
                f"{translate_weeks(row['ZCBH'])}\n")

    print("JSON数据已成功转换为CSV文件：output.csv")


if __name__ == "__main__":
    main()

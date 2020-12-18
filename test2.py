import pandas as pd
df = pd.read_csv("dis.csv")
channelstoclear = []
black_list = []
wib = [692787298856861758,501114768820535305,624730049526104133,679457474599845930,735971323528085516]
wibc = [719052086607740939,723329200018292779]
print(df)
for line in df.channelstoclear:
    try:
        if line.is_integer():
            if int(line) >= 1:
                channelstoclear.append(int(line))
    except:
        if isinstance(line, int):
            if int(line) >= 1:
                channelstoclear.append(int(line))
for line in df.black_list:
    try:
        if line.is_integer():
            black_list.append(int(line))
    except:
        if isinstance(line, int):
            black_list.append(int(line))
print(channelstoclear)

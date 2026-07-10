import pandas as pd

# 行/列映射
LINE_MAP = {
    'A': '横下 (7+8+9)',
    'B': '横中 (4+5+6)',
    'C': '横上 (1+2+3)',
    'D': '左斜 (1+5+9)',
    'E': '竖左 (1+4+7)',
    'F': '竖中 (2+5+8)',
    'G': '竖右 (3+6+9)',
    'H': '右斜 (3+5+7)',
}

# 九宫格示意图
GRID = """
九宫格位置编号：
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┴───┴───┘
"""

print("正在加载数据 data_3.csv ...")
df = pd.read_csv('./data/data_3.csv')
print(f"数据加载完成，共 {df.shape[0]} 条记录。\n")

print(GRID)

# 输入4个位置及对应数值
positions = []
values = []
for i in range(4):
    pos = int(input(f"请输入第{i+1}个揭示格的位置编号 (1-9): "))
    val = int(input(f"请输入该位置的数值 (1-9): "))
    positions.append(pos)
    values.append(val)

# 确保位置和数值排序一致（data_3.csv 中 A,B,C,D 是按位置升序的）
paired = sorted(zip(positions, values))
positions = [p for p, v in paired]
values = [v for p, v in paired]

# 查询匹配行
match = df[
    (df['A'] == positions[0]) &
    (df['B'] == positions[1]) &
    (df['C'] == positions[2]) &
    (df['D'] == positions[3]) &
    (df['E'] == values[0]) &
    (df['F'] == values[1]) &
    (df['G'] == values[2]) &
    (df['H'] == values[3])
]

if match.empty:
    print("\n未找到匹配结果，请检查输入是否正确。")
else:
    best_line = match.iloc[0]['ex_n']
    best_value = match.iloc[0]['ex_v']
    print(f"\n{'='*40}")
    print(f"揭示格: {dict(zip(positions, values))}")
    print(f"推荐选择: {LINE_MAP[best_line]} (代号: {best_line})")
    print(f"期望收益: {best_value:.1f} 金碟币")
    print(f"{'='*40}")
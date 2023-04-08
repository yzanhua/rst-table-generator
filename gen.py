from table import table_list

def get_num_rows_cols(table_list):
  num_rows = len(table_list)
  assert num_rows > 1
  num_cols = len(table_list[0])
  assert num_cols > 0
  for row in table_list:
    assert len(row) == num_cols
  return num_rows, num_cols

num_rows, num_cols = get_num_rows_cols(table_list)

coloum_widths = [0] * num_cols
for row in table_list:
  for col in range(num_cols):
    for item in row[col]:
      coloum_widths[col] = max(coloum_widths[col], len(item))

row_heights = [0] * num_rows
for row in range(num_rows):
  for col in range(num_cols):
    row_heights[row] = max(row_heights[row], len(table_list[row][col]))

boarder_normal = "+"
boarder_header = "+"
for col_width in coloum_widths:
  boarder_normal += "-" * (col_width + 3) + "+"
  boarder_header += "=" * (col_width + 3) + "+"

for row_id in range(num_rows):
  for col_id in range(num_cols):
    while len(table_list[row_id][col_id]) < row_heights[row_id]:
      table_list[row_id][col_id].append("")
    for idx in range(row_heights[row_id]):
      table_list[row_id][col_id][idx] = table_list[row_id][col_id][idx].ljust(coloum_widths[col_id])

print(boarder_normal)
for row_id in range(num_rows):
  for idx in range(row_heights[row_id]):
    for col_id in range(num_cols):
      print("| | ", end="")
      print(table_list[row_id][col_id][idx], end="")
    print("|")
  if row_id == 0:
    print(boarder_header)
  else:
    print(boarder_normal)
# 
# print(boarder_header)
  


    
# 2d keypad

numpad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ("*", 0, "#"))

for item in numpad:
    for item in item:
        print(item, end=" ")
    print()
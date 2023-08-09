def random_rects():
    rect_cnt = int(input("How many rectangles? "))
    total_area = 0
    for cnt in range(1, int(rect_cnt) + 1):
        rect_width = int(input(f"Width {cnt}? "))
        rect_height = int(input(f"Height {cnt}? "))
        total_area += rect_width * rect_height
        for height in range(rect_height):
            print("*"*rect_width)
    print(f"Total area: {total_area}")


random_rects()
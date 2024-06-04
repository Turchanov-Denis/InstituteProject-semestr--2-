    # о раскладке по ящикам
def min_boxes(objects, box_capacity):
    objects.sort(reverse=True)
    num_boxes = 0
    current_box_space = box_capacity

    for obj in objects:
        if obj <= current_box_space:
            current_box_space -= obj
        else:
            num_boxes += 1
            current_box_space = box_capacity - obj

    if current_box_space < box_capacity:
        num_boxes += 1
    return num_boxes


objects = [4, 3, 2, 2, 1, 4, 4]
box_capacity = 5

min_num_boxes = min_boxes(objects, box_capacity)
print("Минимальное количество ящиков, необходимых для упаковки всех объектов:", min_num_boxes)

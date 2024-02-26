def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    return num

grocery_list = ["pen", "ball", "eraser", "pen", "band", "pen", "Pencil", "ball"]
most_common_item = most_frequent(grocery_list)
print(f"The most occurring item in the list is: {most_common_item}")

   
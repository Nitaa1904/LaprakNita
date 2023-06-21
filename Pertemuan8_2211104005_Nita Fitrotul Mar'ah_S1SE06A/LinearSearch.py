def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"Keyword {keyword} has found at index {i}")
            return i
    print(f"Keyword {keyword} not found")
    return -1

data = [20, 15, 71, 8, 32, 5, 21]
keyword = input("Input keyword: ")
linear_search(keyword, data)

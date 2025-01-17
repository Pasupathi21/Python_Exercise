categories = [
    {"category": "Electronics", "items": ["Phone", "Laptop", "Tablet"]},
    {"category": "Clothing", "items": ["Shirt", "Pants", "Jacket"]},
    {"category": "Groceries", "items": ["Apple", "Bread", "Milk"]},
    {"category": "Groceries", "items": ["Apple", "Bread", "Milk", "Eggs"]}
]

# find the dict from list using next method

get_one = next((ct for ct in categories if ct.get("category") == "Groceries"), {})

# print("get_one >>>>>>>", get_one)

new_list = [
    {
        "S.No": i + 1,
        **it
    }
    for i, it in enumerate(categories)
]

print("new list", new_list)
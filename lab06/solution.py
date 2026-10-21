def count_items(values: list) -> dict:
    counts={}
    for item in values:
        counts[item]=counts.get(item,0)+1
    return counts

def unique_sorted(values: list) -> list:
    values_sorted = sorted(set(values))
    return values_sorted





values = ["ошибка", "запуск", "ошибка", "проверка"]
print(count_items(values))
print(unique_sorted(values))
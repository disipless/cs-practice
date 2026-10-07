def winner(names: list[str], scores: list[float]) -> str:
    if len(names) == 0:
        return ""
    best = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best]:
            best = i
    return names[best]


def average(scores: list[float]) -> float:
    if len(scores)==0:
        return 0.0
    return round(sum(scores)/len(scores),2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    pairs = list(zip(names, scores))
    pairs.sort(key=lambda x: x[1], reverse=True)
    return [name for name, scores in pairs]

def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    result = []
    for i in range(len(names)):
        if scores[i] > avg:
            result.append(names[i])
    return result

names = ["Аня", "Боря", "Вика"]
scores = [7.0, 9.0, 9.0]
print("Победитель:", winner(names, scores))
print("Средний результат:", average(scores))
print("Рейтинг:", ranking(names, scores))
print("Выше среднего:", above_average(names, scores))
"""Определите расстояние Левенштейна для двух данных строк s1 и s2."""

def levenstein(s1: str, s2: str):
    len_s1 = len(s1)
    len_s2 = len(s2)
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    for i in range(len_s1 + 1):
        dp[i][0] = i
    for j in range(len_s2 + 1):
        dp[0][j] = j
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,        # удаление
                           dp[i][j - 1] + 1,        # вставка
                           dp[i - 1][j - 1] + cost) # замена
    return dp[len_s1][len_s2]

# print(levenstein("sitting", "kitten"))
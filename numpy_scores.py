import numpy as np

#task1

scores = np.random.randint(50, 101, size=(5, 4))
print("Scores:\n", scores)
print("\n3rd student, 2nd subject:", scores[2, 1])
print("\nLast 2 students:\n", scores[-2:])
print("\nFirst 3 students, subjects 2 & 3:\n", scores[:3, 1:3])

#task2

column_mean = np.round(scores.mean(axis=0), 2)
print("Column wise mean:", column_mean)
bonusineachsub = np.array([5, 4, 3, 2])
bonused_scores = scores + bonusineachsub
bonused_scores = np.clip(bonused_scores, 0, 100)
print("Bonus + Scores:\n", bonused_scores)
row_max = bonused_scores.max(axis=1)
print("Best score per students:", row_max)

#task3

row_min = bonused_scores.min(axis=1, keepdims=True)
row_max = bonused_scores.max(axis=1, keepdims=True)
normalized = (bonused_scores - row_min) / (row_max - row_min)
print("\nNormalized Scores:\n", normalized)
max_index = np.unravel_index(np.argmax(normalized), normalized.shape)
print("\nHighest normalized value at (student, subject):", max_index)
above_90 = bonused_scores[bonused_scores > 90]
print("\nScores above 90:", above_90)
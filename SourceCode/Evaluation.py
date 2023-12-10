import matplotlib.pyplot as plt

relevant_docs = 20
total_docs = 91794
ranked_list = [
    {"DocID": "1", "Relevance": 0},
    {"DocID": "2", "Relevance": 0},
    {"DocID": "3", "Relevance": 1},
    {"DocID": "4", "Relevance": 0},
    {"DocID": "5", "Relevance": 0},
    {"DocID": "6", "Relevance": 1},
    {"DocID": "7", "Relevance": 1},
    {"DocID": "8", "Relevance": 0},
    {"DocID": "9", "Relevance": 1},
    {"DocID": "10", "Relevance": 1},
    {"DocID": "11", "Relevance": 0},
    {"DocID": "12", "Relevance": 0},
    {"DocID": "13", "Relevance": 0},
    {"DocID": "14", "Relevance": 0},
    {"DocID": "15", "Relevance": 1},
    {"DocID": "16", "Relevance": 1},
    {"DocID": "17", "Relevance": 0},
    {"DocID": "18", "Relevance": 0},
    {"DocID": "19", "Relevance": 0},
    {"DocID": "20", "Relevance": 1},
]

precision_values = []
recall_values = []

relevant_in_top_n = 0
retrieved_relevant = 0

for i, entry in enumerate(ranked_list):
    if entry["Relevance"] == 1:
        retrieved_relevant += 1

    precision = retrieved_relevant / (i + 1)
    recall = retrieved_relevant / relevant_docs

    precision_values.append(precision)
    recall_values.append(recall)

# Interpolating 11 points
interpolated_precision = []
recall_levels = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

for level in recall_levels:
    max_precision = 0
    for recall_val, precision_val in zip(recall_values, precision_values):
        if recall_val >= level:
            max_precision = max(max_precision, precision_val)
    interpolated_precision.append(max_precision)

print(interpolated_precision)
print(recall_levels)
plt.plot(recall_values, precision_values, marker='.', label='Precision-Recall Curve')
plt.plot(recall_levels, interpolated_precision, marker='o', linestyle='-', label='11-point Interpolation')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve with 11-point Interpolation')
plt.legend()
plt.grid(True)
plt.show()

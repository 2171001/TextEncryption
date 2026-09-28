from collections import Counter


def analyze_frequency(text):
    freq = Counter(text)
    total = sum(freq.values())

    print("\n[Frequency Analysis]")
    for k, v in sorted(freq.items()):
        print(f"{k}: {v} ({(v/total)*100:.2f}%)")
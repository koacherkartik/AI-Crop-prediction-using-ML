def recommend_fertilizer(nitrogen, phosphorus, potassium):
    if nitrogen < 50:
        return "Urea"
    elif phosphorus < 40:
        return "DAP"
    elif potassium < 40:
        return "MOP"
    else:
        return "No fertilizer required"

if __name__ == "__main__":
    print(recommend_fertilizer(45, 60, 55))

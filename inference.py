# Minimal inference handler for HF Spaces validation
def predict(input_text):
    return f"Processed: {input_text}"

if __name__ == "__main__":
    print("Inference ready!")
    result = predict("test")
    print(result)
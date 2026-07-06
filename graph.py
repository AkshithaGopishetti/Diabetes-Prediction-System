import matplotlib.pyplot as plt

# Replace these values with your actual results
models = ["Logistic Regression", "Decision Tree", "Random Forest", "SVM"]
accuracy = [77.92, 72.08, 75.97, 79.22]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracy)

plt.title("Disease Prediction Model Comparison")
plt.xlabel("Machine Learning Models")
plt.ylabel("Accuracy (%)")

for i, value in enumerate(accuracy):
    plt.text(i, value + 0.5, f"{value:.2f}%")

plt.ylim(0, 100)

plt.show()

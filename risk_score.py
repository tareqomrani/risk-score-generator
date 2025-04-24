from transformers import pipeline

# Load zero-shot classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Risk-related categories
labels = ["Urgent", "Security Breach", "Billing Problem", "Data Access Request", "General"]

# Get input
ticket = input("Paste a ticket or message:\n")

# Classify
result = classifier(ticket, labels)
top_label = result['labels'][0]
score = result['scores'][0]

# Generate a risk score
risk_map = {
    "Security Breach": 90,
    "Data Access Request": 75,
    "Urgent": 60,
    "Billing Problem": 50,
    "General": 10
}
risk_score = risk_map.get(top_label, 0)

print(f"Category: {top_label}")
print(f"Confidence: {score:.2f}")
print(f"Estimated Risk Score: {risk_score}/100")
knowledge_base = {
    "flu": ["cough", "fever"],
    "cold": ["cough", "runny_nose"],
    "fever": ["sore_throat"]
}

facts = ["cough", "sore_throat"]
inferred = True

def forward_chaining():
    global inferred
    inferred = False
    for disease, symptoms in knowledge_base.items():
        if all(symptom in facts for symptom in symptoms) and disease not in facts:
            facts.append(disease)
            inferred = True

while inferred:
    forward_chaining()

if "flu" in facts:
    print("The patient is diagnosed with flu.")
elif "cold" in facts:
    print("The patient is diagnosed with cold.")
else:
    print("No conclusive diagnosis could be made.")

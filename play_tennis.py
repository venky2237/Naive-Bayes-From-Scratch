import pandas as pd

# -------------------------------
# Step 1: Create Tennis Dataset
# -------------------------------

data = {
    "Outlook": [
        "Sunny", "Sunny", "Overcast", "Rain", "Rain",
        "Rain", "Overcast", "Sunny", "Sunny", "Rain",
        "Sunny", "Overcast", "Overcast", "Rain"
    ],
    "Temperature": [
        "Hot", "Hot", "Hot", "Mild", "Cool",
        "Cool", "Cool", "Mild", "Cool", "Mild",
        "Mild", "Mild", "Hot", "Mild"
    ],
    "Humidity": [
        "High", "High", "High", "High", "Normal",
        "Normal", "Normal", "High", "Normal", "Normal",
        "Normal", "High", "Normal", "High"
    ],
    "Wind": [
        "Weak", "Strong", "Weak", "Weak", "Weak",
        "Strong", "Strong", "Weak", "Weak", "Weak",
        "Strong", "Strong", "Weak", "Strong"
    ],
    "Play": [
        "No", "No", "Yes", "Yes", "Yes",
        "No", "Yes", "No", "Yes", "Yes",
        "Yes", "Yes", "Yes", "No"
    ]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# -----------------------------------
# Step 2: Prior Probabilities
# -----------------------------------

print("\nPrior Probabilities")

total = len(df)

p_yes = len(df[df["Play"] == "Yes"]) / total
p_no = len(df[df["Play"] == "No"]) / total

print("P(Yes) =", p_yes)
print("P(No)  =", p_no)

# -----------------------------------
# Step 3: Conditional Probabilities
# -----------------------------------

lookup = {}

features = ["Outlook", "Temperature", "Humidity", "Wind"]

for feature in features:

    lookup[feature] = {}

    table = pd.crosstab(df[feature], df["Play"])

    print(f"\nCrosstab for {feature}")
    print(table)

    for value in table.index:

        yes_prob = table.loc[value, "Yes"] / table["Yes"].sum()

        no_prob = table.loc[value, "No"] / table["No"].sum()

        lookup[feature][value] = {
            "Yes": yes_prob,
            "No": no_prob
        }

# -----------------------------------
# Step 4: Print Lookup Table
# -----------------------------------

print("\nLookup Table")

for feature in lookup:

    print("\n", feature)

    for value in lookup[feature]:

        print(
            value,
            "->",
            lookup[feature][value]
        )

# -----------------------------------
# Step 5: Prediction Function
# -----------------------------------

def predict(outlook, temperature, humidity, wind):

    yes_probability = p_yes

    no_probability = p_no

    yes_probability *= lookup["Outlook"][outlook]["Yes"]
    yes_probability *= lookup["Temperature"][temperature]["Yes"]
    yes_probability *= lookup["Humidity"][humidity]["Yes"]
    yes_probability *= lookup["Wind"][wind]["Yes"]

    no_probability *= lookup["Outlook"][outlook]["No"]
    no_probability *= lookup["Temperature"][temperature]["No"]
    no_probability *= lookup["Humidity"][humidity]["No"]
    no_probability *= lookup["Wind"][wind]["No"]

    print("\nProbability of YES =", yes_probability)
    print("Probability of NO  =", no_probability)

    if yes_probability > no_probability:
        print("\nPrediction : YES (Play Tennis)")
    else:
        print("\nPrediction : NO (Don't Play Tennis)")

# -----------------------------------
# Step 6: Test Example
# -----------------------------------

predict(
    outlook="Sunny",
    temperature="Hot",
    humidity="High",
    wind="Weak"
)
# product_catalog.py

# Mock product catalog
products = [
    {"name": "Eco Water Bottle", "tags": ["eco-friendly", "durable", "recyclable"]},
    {"name": "Trail Backpack", "tags": ["durable", "water-resistant", "lightweight"]},
    {"name": "Vegan Leather Wallet", "tags": ["vegan", "stylish", "compact"]},
    {"name": "Bamboo Toothbrush", "tags": ["eco-friendly", "vegan", "biodegradable"]},
    {"name": "Smartwatch", "tags": ["tech", "durable", "stylish"]},
    {"name": "Noise-Canceling Headphones", "tags": ["tech", "stylish", "lightweight"]},
    {"name": "Solar Charger", "tags": ["eco-friendly", "tech", "portable"]}
]

# Step 1: Collect customer preferences
customer_preferences = []

print("Welcome to the Product Recommendation Engine!")
print("Please enter your preferences (e.g., eco-friendly, durable, tech).")
print("Type 'N' when you are finished.\n")

while True:
    pref = input("Enter a preference (or 'N' to stop): ").lower()
    if pref == "n":
        break
    customer_preferences.append(pref)

# Step 2: Convert preferences to set (removes duplicates)
customer_preferences = set(customer_preferences)

# Step 3: Convert product tags into sets
for product in products:
    product["tags"] = set(product["tags"])

# Step 4: Count matching tags
def count_matches(product_tags, preferences):
    return len(product_tags.intersection(preferences))

# Step 5: Recommend products
def recommend_products(products, preferences):
    recommendations = []
    for product in products:
        matches = count_matches(product["tags"], preferences)
        if matches > 0:  # only recommend if there’s at least one match
            recommendations.append((product["name"], matches))
    # Sort by number of matches, highest first
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

# Step 6: Display results
results = recommend_products(products, customer_preferences)

print("\nRecommended Products:")
if results:
    for name, score in results:
        print(f"- {name} ({score} match(es))")
else:
    print("No products match your preferences.")

# --------------------------------------------------------
# DESIGN MEMO (200–300 words)
"""
Design Memo:

For this product recommendation prototype, the core data structure I used was the list of dictionaries, 
where each dictionary represented a product with a name and a set of tags. I converted both the 
customer preferences and the product tags into sets. This allowed me to use the set intersection 
operation to quickly find overlapping tags between customer preferences and products. Using sets 
ensures that duplicate preferences are removed and improves efficiency when comparing large numbers 
of items.

The program flow follows a straightforward algorithm: first, gather user preferences in a loop, 
store them in a set, and then iterate through the product catalog. For each product, I calculated 
the number of matching tags by calling the `count_matches()` function. I stored product names and 
their match scores in a list of tuples, then sorted them by the number of matches in descending order. 
This ensures that the most relevant products appear at the top of the recommendation list.

If this program had to handle 1,000+ products, efficiency would become even more important. The 
current use of sets for intersections is scalable, but additional optimizations could be considered. 
For example, using dictionaries to map tags directly to products would allow faster lookups instead 
of iterating through every product. Additionally, for very large datasets, a database with indexing 
would be more efficient than in-memory lists.

Overall, this solution balances simplicity with efficiency by leveraging sets and basic sorting. 
It demonstrates how fundamental data structures can directly solve real-world recommendation problems 
while remaining easy to expand for larger applications.
"""

    # age_category: str
    # The age category of the individual. It should be one of the following: 
    # 'teen', 'young_adult', 'adult', or 'senior'. This is a string input.

    # nutrients: dict
    # A dictionary containing the nutritional information of the product.
    # The keys are nutrient names (strings like 'sugar', 'sodium', 'calories', etc.)
    # and the values are their respective amounts (floats or integers, depending on the nutrient).
    # Example: {'sugar': 5, 'sodium': 150, 'calories': 200}

    # serving_size: float (optional, default=1)
    # The size of one serving of the food in grams. It is a floating-point number (e.g., 50.0).
    # The default is set to 1 gram if no serving size is specified.
    

def calculate_health_score(age_category, nutrients, serving_size=1):
    # Ensure that nutrients contains all necessary data
    required_nutrients = ['sugar', 'sodium', 'saturated_fat', 'fiber', 'protein', 'calcium', 'iron', 'vitamin_a', 'vitamin_d', 'calories']
    
    for nutrient in required_nutrients:
        if nutrient not in nutrients:
            print(f"Warning: {nutrient} is missing from the nutrient data.")
            # Optionally, we can set a default value (e.g., 0 or a reasonable value based on age category)
            nutrients[nutrient] = 0  # Default missing nutrients to 0 for simplicity (or adjust as necessary)

    # Normalize the nutrient values to 100g per serving
    normalized_nutrients = {}
    for nutrient, value in nutrients.items():
        if nutrient not in ['calories', 'serving_size']:  # We don't normalize calories and serving size
            normalized_nutrients[nutrient] = (value * 100) / serving_size

    # Define the healthy ranges based on RDA and WHO/FSSAI guidelines for age-specific needs
    healthy_ranges = {
        'sugar': (0, 10),            
        'sodium': (0, 8),           
        'saturated_fat': (0, 5),     
        'fiber': (15, 30),           
        'protein': (15, 30),         
        'calcium': (800, 1200),      # Example for calcium (mg/day)
        'iron': (10, 18),           # Example for iron (mg/day)
        'vitamin_a': (700, 900),    # Example for Vitamin A (mcg/day)
        'vitamin_d': (400, 800),    # Example for Vitamin D (IU/day)
    }

    # Adjust ranges based on age category
    if age_category == "teen":
        healthy_ranges.update({'sugar': (0, 10), 'sodium': (0, 10), 'saturated_fat': (0, 7), 'fiber': (20, 35), 'protein': (20, 40)})
    elif age_category == "young_adult":
        healthy_ranges.update({'sugar': (0, 10), 'sodium': (0, 12), 'saturated_fat': (0, 10), 'fiber': (15, 30), 'protein': (15, 30)})
    elif age_category == "adult":
        healthy_ranges.update({'sugar': (0, 8), 'sodium': (0, 8), 'saturated_fat': (0, 7), 'fiber': (20, 30), 'protein': (10, 20)})
    elif age_category == "senior":
        healthy_ranges.update({'sugar': (0, 8), 'sodium': (0, 8), 'saturated_fat': (0, 5), 'fiber': (25, 40), 'protein': (15, 30)})

    # Nutrient weights (higher value means more importance)
    weights = {
        'sugar': 1,
        'sodium': 2,
        'saturated_fat': 2,
        'fiber': 1.5,
        'protein': 1.5,
        'calcium': 2,
        'iron': 1.5,
        'vitamin_a': 1,
        'vitamin_d': 1,
    }

    # Additive penalties (updated with different levels of impact based on food type)
    additives_penalty = {
        'preservatives': 2,
        'artificial_sweeteners': 5,
        'artificial_colors': 4,
        'trans_fats': 6,
    }

    # Nutrient density score (added based on the ratio of nutrients to calories)
    nutrient_density_weights = {
        'fiber': 1.5,
        'protein': 2,
        'calcium': 1.5,
        'iron': 1.5,
        'vitamin_a': 1,
        'vitamin_d': 1
    }

    # Calculate health score
    health_score = 0
    total_possible_score = 100  # Max score is 100 points

    # Evaluate nutrients
    for nutrient, range_values in healthy_ranges.items():
        healthy_min, healthy_max = range_values
        nutrient_value = normalized_nutrients.get(nutrient, 0)

        # Calculate nutrient score based on ranges
        if nutrient_value < healthy_min:
            score = (nutrient_value / healthy_min) * 20  # Penalize if below minimum
        elif nutrient_value > healthy_max:
            score = max(0, (healthy_max - nutrient_value) / healthy_max * 20)  # Penalize if above maximum
        else:
            score = (20 * (nutrient_value - healthy_min)) / (healthy_max - healthy_min)

        # Apply weight to the score
        weighted_score = score * weights[nutrient]
        health_score += weighted_score

    # Apply penalties for additives and preservatives
    for additive, penalty in additives_penalty.items():
        if additive in nutrients:
            health_score -= penalty

    # Evaluate nutrient density score based on calories (portion size factored in)
    total_calories = nutrients.get('calories', 0)
    if total_calories > 0:
        nutrient_density_score = 0
        for nutrient, weight in nutrient_density_weights.items():
            nutrient_value = normalized_nutrients.get(nutrient, 0)
            nutrient_density_score += (nutrient_value * weight) / total_calories

        health_score += nutrient_density_score * 10  # Nutrient density scaling factor

    # Ensure the final health score doesn't exceed 100 points
    health_score = min(health_score, total_possible_score)

    return round(health_score, 2)

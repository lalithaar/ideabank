# Health Score Algorithm Documentation

This document provides a detailed explanation of the Health Score Algorithm designed to assess the health quality of food based on nutritional content and various age categories. The health score is calculated by evaluating the nutrient values of a product against recommended daily allowances (RDA) and healthy ranges for different age groups. The algorithm also factors in additives, preservatives, and nutrient density to provide a comprehensive score.

## Table of Contents
1. [Introduction](#introduction)
2. [Parameters](#parameters)
3. [Healthy Ranges](#healthy-ranges)
4. [Nutrient Weights](#nutrient-weights)
5. [Additive Penalties](#additive-penalties)
6. [Nutrient Density Score](#nutrient-density-score)
7. [Health Score Calculation](#health-score-calculation)
8. [Age Category Adjustments](#age-category-adjustments)
9. [Final Calculation](#final-calculation)
10. [References](#references)

---

## 1. Introduction

The Health Score Algorithm is designed to evaluate the nutritional quality of food products based on their content of various nutrients and their appropriateness for specific age categories. The score is calculated by comparing nutrient levels to established healthy ranges and incorporating penalties for harmful additives and a nutrient density evaluation based on calories.

---

## 2. Parameters

The following parameters are taken into account during the health score calculation:

- **Age Category**: Specifies the age group of the individual consuming the product. Possible values are:
  - `teen`
  - `young_adult`
  - `adult`
  - `senior`
  
- **Nutrients**: A dictionary of nutrients in the food product, with each nutrient's value expressed in grams or milligrams. The key-value pairs represent nutrient names and their respective amounts. Example:
  ```python
  {'sugar': 5, 'sodium': 150, 'calories': 200}
  ```

- **Serving Size** (Optional): The size of one serving of the food in grams. The default value is 1 gram.

---

## 3. Healthy Ranges

The algorithm evaluates the nutrient values based on recommended daily intake values or healthy ranges for each nutrient. These values differ based on the age category. The following healthy ranges are used as a baseline:

### Standard Healthy Ranges
These are the general healthy range values used for all age categories unless adjusted by the specific age category.

- **Sugar**: 0–10 grams per 100 grams of food
- **Sodium**: 0–8 grams per 100 grams of food
- **Saturated Fat**: 0–5 grams per 100 grams of food
- **Fiber**: 15–30 grams per 100 grams of food
- **Protein**: 15–30 grams per 100 grams of food
- **Calcium**: 800–1200 mg per 100 grams of food
- **Iron**: 10–18 mg per 100 grams of food
- **Vitamin A**: 700–900 mcg per 100 grams of food
- **Vitamin D**: 400–800 IU per 100 grams of food

### Age Category Adjustments

Age-specific adjustments are made based on the individual's needs:

- **Teen**: Higher fiber, protein, and sodium ranges to support growth.
- **Young Adult**: Moderate adjustments to sugar, sodium, and fat.
- **Adult**: Balanced ranges to maintain health.
- **Senior**: Adjusted for reduced caloric intake and higher fiber needs.

---

## 4. Nutrient Weights

The importance of each nutrient is evaluated using weights. Higher weights reflect the greater impact the nutrient has on overall health. The weights used in the algorithm are as follows:

- **Sugar**: 1
- **Sodium**: 2
- **Saturated Fat**: 2
- **Fiber**: 1.5
- **Protein**: 1.5
- **Calcium**: 2
- **Iron**: 1.5
- **Vitamin A**: 1
- **Vitamin D**: 1

These weights are applied during the score calculation to emphasize the importance of certain nutrients in maintaining health.

---

## 5. Additive Penalties

Penalties are applied for the presence of harmful additives, which can negatively impact health. The following additives and their penalties are considered in the calculation:

- **Preservatives**: Penalty score = 2
- **Artificial Sweeteners**: Penalty score = 5
- **Artificial Colors**: Penalty score = 4
- **Trans Fats**: Penalty score = 6

The presence of these additives in the product will reduce the health score.

---

## 6. Nutrient Density Score

The nutrient density score is calculated to assess how well the nutrients in the product contribute to overall health, based on the number of calories it contains. Nutrients that contribute positively to health (fiber, protein, calcium, iron, vitamins) are weighted and added to the nutrient density score. The formula for nutrient density is:

\[
\text{Nutrient Density Score} = \sum \left(\frac{\text{Nutrient Value} \times \text{Weight}}{\text{Calories}}\right)
\]

This score is then scaled by a factor of 10 to adjust its influence on the final health score.

---

## 7. Health Score Calculation

The health score is calculated as a weighted sum of the nutrient scores, adjusted by additive penalties and nutrient density:

1. **Evaluate Nutrients**: Compare the nutrient values to the healthy range for the relevant age category. A score is calculated for each nutrient based on how close its value is to the ideal range.
2. **Apply Weight**: Each nutrient score is multiplied by its respective weight.
3. **Add Penalties**: Any harmful additives in the product will reduce the overall health score based on predefined penalties.
4. **Add Nutrient Density**: The nutrient density score is added, giving more weight to nutrient-dense foods.

The total health score is capped at 100.

---

## 8. Age Category Adjustments

Different age categories require different nutrient needs. The algorithm adjusts the healthy ranges for each nutrient based on the age category. For example:

- **Teen**: Higher fiber, protein, and sodium ranges to support growth.
- **Young Adult**: Moderate adjustments.
- **Adult**: Balanced ranges for maintaining health.
- **Senior**: Higher fiber and protein needs, adjusted for a more controlled calorie intake.

---

## 9. Final Calculation

After evaluating the nutrients, applying weights, penalties, and adjusting for nutrient density, the final health score is computed. The score is capped at 100 points, ensuring it represents the maximum possible health benefit.

---

## 10. References

1. **Dietary Guidelines for Americans** - U.S. Department of Agriculture.  
   [https://www.dietaryguidelines.gov](https://www.dietaryguidelines.gov)  
   Provides recommendations for nutrient intake across different age groups.

2. **World Health Organization (WHO) Nutrition Guidelines**  
   [https://www.who.int/nutrition](https://www.who.int/nutrition)  
   International guidelines for healthy eating and nutrient intake.

3. **Food and Drug Administration (FDA) Nutritional Labeling**  
   [https://www.fda.gov](https://www.fda.gov)  
   Provides standardized nutrient labeling for food products.

4. **Centers for Disease Control and Prevention (CDC) Nutrition**  
   [https://www.cdc.gov/nutrition](https://www.cdc.gov/nutrition)  
   Provides evidence-based nutrition guidelines.

5. **The Academy of Nutrition and Dietetics**  
   [https://www.eatright.org](https://www.eatright.org)  
   Offers expert advice on nutrition and health, including daily intake recommendations.

---

This documentation should provide a clear understanding of how the Health Score Algorithm works and its reliance on established health research and guidelines.

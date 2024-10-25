import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

def diet_planner_app():
    # Load your trained model
    model = joblib.load('./diet_model3.pkl')

    FEATURE_NAMES = [
        'Gender', 'Age', 'Diabetes', 'Weight', 'Wanna Loose Weight', 'Height', 'BMI', 'Calories', 'Meal Type',
        'Exercise_Lightly Active', 'Exercise_Moderate', 'Exercise_Sedentary', 'Exercise_Super Active', 'Exercise_Very Active',
        'Workout_High intensity Exercise', 'Workout_Light Exercise', 'Workout_Moderate Exercise', 'Workout_Sedentary Lifestyle'
    ]

    DIET_NAME_MAPPING = {
        0: 'Balanced Diet',
        1: 'Energy boost diet',
        2: 'Light Activity Fuel',
        3: 'Fitness Diet'
    }

    recipes = {
        'Balanced Diet': {
            'vegetarian': {
                'breakfast': [
                    'Oatmeal with Fruits and Nuts',
                    'Greek Yogurt with Honey and Almonds',
                    'Chia Pudding with Fresh Berries',
                    'Smoothie with Spinach and Banana',
                    'Whole Grain Toast with Avocado',
                    'Vegetable Upma with Coconut Chutney',
                    'Quinoa Porridge with Almond Milk'
                ],
                'lunch': [
                    'Vegetable Stir-fry with Brown Rice',
                    'Lentil Soup with Whole Grain Bread',
                    'Stuffed Bell Peppers with Quinoa',
                    'Grilled Paneer with Mixed Vegetables',
                    'Vegetable Pasta Salad',
                    'Chickpea Salad with Lemon Dressing',
                    'Mushroom and Spinach Wrap'
                ],
                'dinner': [
                    'Roasted Sweet Potatoes with Kale Salad',
                    'Whole Wheat Pasta with Marinara Sauce',
                    'Tofu and Broccoli Stir-fry',
                    'Mixed Vegetable Curry with Brown Rice',
                    'Palak Paneer with Whole Wheat Roti',
                    'Chole (Chickpea Curry) with Rice',
                    'Baingan Bharta (Roasted Eggplant Curry)'
                ]
            },
            'non_vegetarian': {
                'breakfast': [
                    'Whole Grain Toast with Avocado and Poached Egg',
                    'Scrambled Eggs with Veggies',
                    'Smoothie with Spinach and Banana',
                    'Greek Yogurt with Honey and Almonds',
                    'Chicken Sausage with Roasted Veggies',
                    'Egg White Omelette with Onions and Tomatoes',
                    'Protein Pancakes with Turkey Bacon'
                ],
                'lunch': [
                    'Grilled Chicken with Steamed Vegetables',
                    'Chicken Butter Masala with Naan',
                    'Chicken Tikka Salad',
                    'Spinach and Mushroom Frittata',
                    'Tandoori Chicken with Quinoa',
                    'Stuffed Bell Peppers with Ground Turkey',
                    'Lemon Herb Chicken Wrap'
                ],
                'dinner': [
                    'Baked Salmon with Asparagus',
                    'Grilled Shrimp with Quinoa and Arugula Salad',
                    'Butter Chicken with Basmati Rice',
                    'Chicken Biryani with Raita',
                    'Stuffed Eggplant with Ground Turkey',
                    'Lamb Rogan Josh with Rice',
                    'Seared Tuna with Roasted Vegetables'
                ]
            }
        },
        'Energy Boost Diet': {
            'vegetarian': {
                'breakfast': [
                    'Peanut Butter Banana Smoothie',
                    'Green Smoothie with Chia Seeds',
                    'Protein-Packed Overnight Oats',
                    'Energy Balls with Dates and Almonds',
                    'Greek Yogurt with Granola and Berries',
                    'Almond Butter Toast with Banana',
                    'Spinach and Mushroom Omelette'
                ],
                'lunch': [
                    'Quinoa Salad with Roasted Veggies',
                    'Chickpea and Avocado Wrap',
                    'Lentil and Veggie Power Bowl',
                    'Stuffed Sweet Potatoes with Black Beans',
                    'Tofu Stir-fry with Mixed Vegetables',
                    'Edamame and Hummus Snack Plate',
                    'Paneer Tikka with Green Salad'
                ],
                'dinner': [
                    'Veggie Stir-fry with Tofu and Quinoa',
                    'Lentil Soup with Spinach',
                    'Chickpea and Sweet Potato Stew',
                    'Zoodles with Pesto and Cherry Tomatoes',
                    'Mixed Vegetable Curry with Rice',
                    'Palak Chole (Spinach Chickpea Curry)',
                    'Stir-fried Vegetables with Brown Rice'
                ]
            },
            'non_vegetarian': {
                'breakfast': [
                    'Protein Smoothie with Berries and Greek Yogurt',
                    'Scrambled Eggs with Smoked Salmon',
                    'Turkey and Avocado Wrap',
                    'Cottage Cheese with Pineapple Chunks',
                    'Chicken Sausage and Veggie Scramble',
                    'Egg and Cheese Breakfast Burrito',
                    'Chicken and Spinach Omelette'
                ],
                'lunch': [
                    'Grilled Chicken with Avocado Salad',
                    'Chicken Biryani with Raita',
                    'Shrimp and Spinach Salad',
                    'Tuna Sandwich with Whole Grain Bread',
                    'Chicken and Hummus Wrap',
                    'Butter Chicken with Jeera Rice',
                    'Tandoori Salmon with Quinoa'
                ],
                'dinner': [
                    'Grilled Salmon with Asparagus',
                    'Roasted Chicken with Sweet Potatoes',
                    'Shrimp Stir-fry with Mixed Vegetables',
                    'Chicken Curry with Brown Rice',
                    'Turkey Meatloaf with Steamed Veggies',
                    'Lamb Curry with Naan',
                    'Baked Cod with Spinach'
                ]
            }
        },
        'Light Activity Fuel': {
            'vegetarian': {
                'breakfast': [
                    'Whole Grain Toast with Almond Butter',
                    'Greek Yogurt with Berries',
                    'Avocado Smoothie with Almond Milk',
                    'Scrambled Eggs with Spinach',
                    'Cottage Cheese with Peaches',
                    'Apple Slices with Peanut Butter',
                    'Poha (Flattened Rice) with Vegetables'
                ],
                'lunch': [
                    'Vegetable Pasta Salad',
                    'Quinoa and Chickpea Salad',
                    'Baked Falafel with Cucumber Yogurt',
                    'Stuffed Portobello Mushrooms',
                    'Spinach Salad with Nuts and Berries',
                    'Lentil and Avocado Salad',
                    'Vegetable Korma with Rice'
                ],
                'dinner': [
                    'Zucchini Noodles with Pesto',
                    'Stuffed Eggplant with Spinach and Feta',
                    'Roasted Beet and Goat Cheese Salad',
                    'Miso Soup with Tofu',
                    'Vegetable Stir-fry with Brown Rice',
                    'Mushroom and Spinach Risotto',
                    'Palak Paneer with Roti'
                ]
            },
            'non_vegetarian': {
                'breakfast': [
                    'Egg and Cheese Breakfast Sandwich',
                    'Turkey Sausage with Scrambled Eggs',
                    'Protein Smoothie with Spinach and Berries',
                    'Cottage Cheese with Honey and Walnuts',
                    'Avocado and Egg on Whole Wheat Toast',
                    'Chicken and Veggie Omelette',
                    'Masala Omelette with Toast'
                ],
                'lunch': [
                    'Grilled Chicken Salad with Olive Oil Dressing',
                    'Turkey and Spinach Roll-Ups',
                    'Chickpea Salad with Grilled Chicken',
                    'Baked Tilapia with Steamed Broccoli',
                    'Chicken and Hummus Wrap',
                    'Butter Chicken with Naan',
                    'Chicken Tikka Masala with Rice'
                ],
                'dinner': [
                    'Roasted Chicken with Sweet Potatoes',
                    'Grilled Salmon with Couscous',
                    'Shrimp Stir-fry with Mixed Veggies',
                    'Chicken Curry with Steamed Rice',
                    'Turkey Meatballs with Zoodles',
                    'Baked Cod with Spinach',
                    'Lamb Vindaloo with Rice'
                ]
            }
        },
        'Fitness Diet': {
            'vegetarian': {
                'breakfast': [
                    'Protein Shake with Almond Milk',
                    'Omelette with Spinach and Tomatoes',
                    'Avocado and Egg on Whole Wheat Toast',
                    'Smoothie with Berries and Protein Powder',
                    'Cottage Cheese with Pineapple Chunks',
                    'Chia Pudding with Protein Powder',
                    'Protein Pancakes with Greek Yogurt'
                ],
                'lunch': [
                    'Quinoa Bowl with Black Beans and Salsa',
                    'Chickpea Salad with Olive Oil Dressing',
                    'Stir-fried Tofu with Vegetables',
                    'Grilled Veggie Wrap with Hummus',
                    'Vegetable Biryani with Raita',
                    'Stuffed Bell Peppers with Quinoa',
                    'Roasted Veggie and Chickpea Salad'
                ],
                'dinner': [
                    'Roasted Sweet Potatoes with Black Beans',
                    'Stuffed Zucchini with Lentils and Veggies',
                    'Spinach and Mushroom Stir-fry with Tofu',
                    'Cauliflower Rice Stir-fry',
                    'Mixed Vegetable Curry with Rice',
                    'Paneer Tikka with Mint Chutney',
                    'Baked Eggplant with Mediterranean Spices'
                ]
            },
            'non_vegetarian': {
                'breakfast': [
                    'Egg White Scramble with Veggies',
                    'Protein Shake with Almond Milk',
                    'Protein Pancakes with Turkey Bacon',
                    'Greek Yogurt with Honey and Almonds',
                    'Omelette with Spinach and Tomatoes',
                    'Turkey Sausage with Roasted Veggies',
                    'Avocado and Egg on Whole Wheat Toast'
                ],
                'lunch': [
                    'Grilled Chicken with Brown Rice',
                    'Chicken Butter Masala with Naan',
                    'Salmon with Sweet Potato',
                    'Chicken Caesar Salad',
                    'Turkey Wrap with Mixed Veggies',
                    'Shrimp and Spinach Salad',
                    'Butter Chicken with Jeera Rice'
                ],
                'dinner': [
                    'Roasted Chicken with Steamed Veggies',
                    'Seared Steak with Mixed Veggie Stir-fry',
                    'Baked Tilapia with Green Beans',
                    'Turkey Meatballs with Zoodles',
                    'Grilled Salmon with Avocado Salad',
                    'Stir-fried Shrimp with Broccoli',
                    'Chicken Korma with Rice'
                ]
            }
        }
    }

    st.title("Automatic Diet Plan Generator")

    st.write("Please fill in the details to generate your personalized diet plan.")

    age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
    weight = st.number_input("Enter your weight (kg)", min_value=0.0, value=70.0)
    height = st.number_input("Enter your height (cm)", min_value=0.0, value=170.0)

    gender = st.radio("Gender", ('Male', 'Female'))
    gender = 0 if gender == 'Male' else 1

    diet_preference = st.radio("Diet Preference", ('Vegetarian', 'Non-Vegetarian'))

    bmi = weight / ((height / 100) ** 2)
    calories = st.number_input("Calories intake per day", min_value=1000, max_value=4000, value=2000)

    exercise = st.selectbox("Select your exercise level", ['Sedentary', 'Lightly Active', 'Moderate', 'Very Active', 'Super Active'])
    workout = st.selectbox("Select your workout intensity", ['Sedentary Lifestyle', 'Light Exercise', 'Moderate Exercise', 'High intensity Exercise'])

    if st.button("Generate Diet Plan"):
        input_data = {
            'Age': age,
            'Weight': weight,
            'Height': height,
            'Gender': gender,
            'BMI': bmi,
            'Calories': calories,
            f'Exercise_{exercise}': 1,
            f'Workout_{workout}': 1
        }

        input_df = pd.DataFrame([input_data])
        input_df = input_df.reindex(columns=FEATURE_NAMES, fill_value=0)

        predicted_key = model.predict(input_df)[0]
        recommended_diet = DIET_NAME_MAPPING.get(predicted_key)

        st.subheader("Your Recommended Diet Plan:")
        st.subheader(recommended_diet)

        recommended_recipes = recipes.get(recommended_diet, {}).get('vegetarian' if diet_preference == 'Vegetarian' else 'non_vegetarian')
        if recommended_recipes:
            days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

            breakfast_recipes = pd.DataFrame(recommended_recipes['breakfast'], columns=['Breakfast Recipes'], index=days_of_week)
            lunch_recipes = pd.DataFrame(recommended_recipes['lunch'], columns=['Lunch Recipes'], index=days_of_week)
            dinner_recipes = pd.DataFrame(recommended_recipes['dinner'], columns=['Dinner Recipes'], index=days_of_week)

            st.subheader("Breakfast Recipes:")
            st.table(breakfast_recipes)

            st.subheader("Lunch Recipes:")
            st.table(lunch_recipes)

            st.subheader("Dinner Recipes:")
            st.table(dinner_recipes)

            # Visualization: Pie chart of meal types
            meal_labels = ['Breakfast', 'Lunch', 'Dinner']
            meal_counts = [len(recommended_recipes['breakfast']),
                           len(recommended_recipes['lunch']),
                           len(recommended_recipes['dinner'])]
            plt.figure(figsize=(8, 4))
            plt.pie(meal_counts, labels=meal_labels, autopct='%1.1f%%', startangle=140)
            plt.title('Distribution of Meal Types')
            st.pyplot(plt)

            # Visualization: Bar graph of calories
            data = {
                'Meal Type': ['Breakfast', 'Lunch', 'Dinner'],
                'Calories': [calories * 0.3, calories * 0.4, calories * 0.3]  # Assuming meal distribution
            }
            df = pd.DataFrame(data)
            plt.figure(figsize=(8, 4))
            plt.bar(df['Meal Type'], df['Calories'], color=['skyblue', 'orange', 'green'])
            plt.title('Calorie Distribution by Meal Type')
            plt.xlabel('Meal Type')
            plt.ylabel('Calories')
            st.pyplot(plt)
        else:
            st.write("No recipes available for the predicted diet.")
import streamlit as st
import json
from io import StringIO



RECIPES = [
    # South Indian Breakfast
    {
        "name": "Masala Dosa",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["rice", "urad dal", "potato", "onion", "mustard seeds", "curry leaves"],
        "steps": [
            "Soak rice and urad dal overnight.",
            "Grind into batter and ferment for 8 hours.",
            "Prepare potato filling by boiling and mashing potatoes with sautéed onions and spices.",
            "Heat a griddle and pour batter to make thin dosa.",
            "Place potato filling on dosa and fold it.",
            "Serve hot with chutney and sambar."
        ]
    },
    {
        "name": "Idli",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["rice", "urad dal", "fenugreek seeds"],
        "steps": [
            "Soak rice and urad dal separately overnight.",
            "Grind both to a smooth batter.",
            "Mix and ferment batter for 8-12 hours.",
            "Pour batter into idli molds and steam for 10-15 mins.",
            "Serve with coconut chutney and sambar."
        ]
    },
    {
        "name": "Upma",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["semolina", "mustard seeds", "green chili", "onion", "curry leaves", "ginger"],
        "steps": [
            "Dry roast semolina until fragrant.",
            "Heat oil, add mustard seeds, green chili, onion, curry leaves, and ginger.",
            "Add water and bring to boil.",
            "Slowly add semolina, stirring to avoid lumps.",
            "Cook until thickened.",
            "Serve hot."
        ]
    },
    {
        "name": "Medu Vada",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["urad dal", "black pepper", "curry leaves", "ginger", "onion"],
        "steps": [
            "Soak urad dal for 4-5 hours and grind to a smooth batter.",
            "Add chopped onions, curry leaves, pepper, and salt.",
            "Shape batter into doughnut shapes.",
            "Deep fry until golden brown.",
            "Serve with sambar and chutney."
        ]
    },
    {
        "name": "Pongal",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["rice", "moong dal", "ginger", "black pepper", "curry leaves", "cashews"],
        "steps": [
            "Dry roast moong dal and cook with rice.",
            "In another pan, fry ginger, black pepper, curry leaves, and cashews in ghee.",
            "Mix the fried ingredients with cooked rice and dal.",
            "Serve hot with coconut chutney."
        ]
    },
    # North Indian Breakfast
    {
        "name": "Aloo Paratha",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["wheat flour", "potato", "green chili", "coriander", "ghee"],
        "steps": [
            "Boil and mash potatoes.",
            "Mix mashed potatoes with chopped green chili and coriander.",
            "Prepare dough with wheat flour and water.",
            "Roll dough into discs, place potato filling inside and seal.",
            "Roll again and cook on a hot pan with ghee until golden.",
            "Serve with yogurt or pickle."
        ]
    },
    {
        "name": "Poha",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["flattened rice", "mustard seeds", "green chili", "onion", "peanuts"],
        "steps": [
            "Rinse flattened rice and drain.",
            "Sauté mustard seeds, green chili, and onions.",
            "Add peanuts and flattened rice.",
            "Cook for 5 minutes and garnish with coriander.",
            "Serve hot."
        ]
    },
    {
        "name": "Chole Bhature",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["chickpeas", "flour", "onion", "tomato", "spices"],
        "steps": [
            "Soak chickpeas overnight and cook till soft.",
            "Prepare onion-tomato gravy with spices.",
            "Add chickpeas and simmer.",
            "Prepare dough for bhature and deep fry puffed bread.",
            "Serve chole with hot bhature."
        ]
    },
    {
        "name": "Paneer Paratha",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["wheat flour", "paneer", "green chili", "spices"],
        "steps": [
            "Grate paneer and mix with chopped green chili and spices.",
            "Prepare dough with wheat flour and water.",
            "Roll dough, stuff with paneer mixture and seal.",
            "Roll again and cook on hot tawa with ghee.",
            "Serve hot with yogurt."
        ]
    },
    {
        "name": "Aloo Puri",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["wheat flour", "potato", "tomato", "spices"],
        "steps": [
            "Prepare dough with wheat flour for puri and roll into small discs.",
            "Deep fry until puffed and golden.",
            "Prepare potato curry with tomato and spices.",
            "Serve puri with aloo curry."
        ]
    },
    # Chinese Breakfast
    {
        "name": "Congee",
        "cuisine": "Chinese",
        "veg": False,
        "meal": "Breakfast",
        "ingredients": ["rice", "chicken", "ginger", "spring onion"],
        "steps": [
            "Cook rice in plenty of water to make porridge.",
            "Add shredded cooked chicken and ginger.",
            "Simmer until thick and creamy.",
            "Garnish with spring onion and serve."
        ]
    },
    {
        "name": "Steamed Buns",
        "cuisine": "Chinese",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["flour", "yeast", "sugar", "vegetables", "soy sauce"],
        "steps": [
            "Prepare dough with flour, yeast, and sugar and let rise.",
            "Prepare vegetable filling with soy sauce.",
            "Shape buns with filling inside.",
            "Steam for 15 minutes and serve."
        ]
    },
    {
        "name": "Egg Fried Rice",
        "cuisine": "Chinese",
        "veg": False,
        "meal": "Breakfast",
        "ingredients": ["rice", "egg", "soy sauce", "spring onion", "peas"],
        "steps": [
            "Cook rice and cool.",
            "Scramble eggs in a pan.",
            "Add rice, soy sauce, peas and spring onion.",
            "Fry together and serve hot."
        ]
    },
    {
        "name": "Scallion Pancakes",
        "cuisine": "Chinese",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["flour", "scallion", "oil", "salt"],
        "steps": [
            "Make dough with flour and water.",
            "Roll out dough, sprinkle chopped scallions.",
            "Roll and flatten, then pan fry until crispy.",
            "Serve with dipping sauce."
        ]
    },
    {
        "name": "Soy Milk",
        "cuisine": "Chinese",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["soybeans", "water", "sugar"],
        "steps": [
            "Soak soybeans overnight.",
            "Blend with water and strain to get soy milk.",
            "Boil soy milk and add sugar.",
            "Serve warm or cold."
        ]
    },
    # Italian Breakfast
    {
        "name": "Frittata",
        "cuisine": "Italian",
        "veg": False,
        "meal": "Breakfast",
        "ingredients": ["eggs", "cheese", "vegetables", "olive oil"],
        "steps": [
            "Beat eggs with cheese and chopped vegetables.",
            "Cook in an oven-safe pan until set.",
            "Finish in the oven until golden.",
            "Serve warm."
        ]
    },
    {
        "name": "Cornetti",
        "cuisine": "Italian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["flour", "butter", "sugar", "yeast", "milk"],
        "steps": [
            "Prepare dough with flour, butter, sugar, yeast, and milk.",
            "Roll into crescent shapes.",
            "Bake until golden.",
            "Serve with jam or butter."
        ]
    },
    {
        "name": "Espresso and Biscotti",
        "cuisine": "Italian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["coffee beans", "flour", "sugar", "almonds"],
        "steps": [
            "Brew espresso.",
            "Prepare biscotti dough with flour, sugar, and almonds.",
            "Bake biscotti twice for crispness.",
            "Serve biscotti with espresso."
        ]
    },
    {
        "name": "Panettone",
        "cuisine": "Italian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["flour", "yeast", "sugar", "raisins", "candied fruit"],
        "steps": [
            "Prepare sweet yeast dough with flour, sugar, and yeast.",
            "Add raisins and candied fruit.",
            "Let rise and bake until golden.",
            "Cool and serve sliced."
        ]
    },
    {
        "name": "Ricotta Pancakes",
        "cuisine": "Italian",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["ricotta", "flour", "egg", "milk", "sugar"],
        "steps": [
            "Mix ricotta with flour, egg, milk, and sugar.",
            "Cook on a griddle until golden on both sides.",
            "Serve with honey or syrup."
        ]
    },
    # Japanese Breakfast
    {
        "name": "Tamago Kake Gohan",
        "cuisine": "Japanese",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["rice", "egg", "soy sauce"],
        "steps": [
            "Cook rice and serve hot.",
            "Crack raw egg on top.",
            "Add soy sauce and mix well.",
            "Eat immediately."
        ]
    },
    {
        "name": "Miso Soup",
        "cuisine": "Japanese",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["miso paste", "tofu", "seaweed", "dashi stock"],
        "steps": [
            "Heat dashi stock.",
            "Add miso paste and dissolve.",
            "Add tofu cubes and seaweed.",
            "Simmer briefly and serve hot."
        ]
    },
    {
        "name": "Rice Balls (Onigiri)",
        "cuisine": "Japanese",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["rice", "salt", "nori"],
        "steps": [
            "Cook rice and let cool slightly.",
            "Shape rice into triangles.",
            "Wrap partially with nori.",
            "Serve as snack or breakfast."
        ]
    },
    {
        "name": "Grilled Fish",
        "cuisine": "Japanese",
        "veg": False,
        "meal": "Breakfast",
        "ingredients": ["fish", "salt", "lemon"],
        "steps": [
            "Season fish with salt.",
            "Grill until cooked through.",
            "Serve with lemon wedges."
        ]
    },
    {
        "name": "Japanese Omelette (Tamagoyaki)",
        "cuisine": "Japanese",
        "veg": True,
        "meal": "Breakfast",
        "ingredients": ["egg", "soy sauce", "mirin", "sugar"],
        "steps": [
            "Beat eggs with soy sauce, mirin, and sugar.",
            "Cook thin layers in a rectangular pan.",
            "Roll layers to form omelette.",
            "Slice and serve."
        ]
    },
    # South Indian Lunch
    {
        "name": "Sambar",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["toor dal", "tamarind", "vegetables", "sambar powder"],
        "steps": [
            "Cook toor dal until soft.",
            "Prepare tamarind extract.",
            "Add vegetables and tamarind to dal.",
            "Cook with sambar powder and temper with mustard seeds.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Rasam",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["tomato", "tamarind", "pepper", "cumin", "mustard seeds"],
        "steps": [
            "Boil tomatoes and tamarind extract.",
            "Add roasted pepper and cumin powder.",
            "Temper with mustard seeds.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Lemon Rice",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["rice", "lemon", "mustard seeds", "chili", "peanuts"],
        "steps": [
            "Cook rice and cool.",
            "Tempered mustard seeds, chili and peanuts in oil.",
            "Add lemon juice and mix with rice.",
            "Serve at room temperature."
        ]
    },
    {
        "name": "Curd Rice",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["rice", "curd", "mustard seeds", "ginger", "curry leaves"],
        "steps": [
            "Cook rice and cool.",
            "Mix with curd.",
            "Temper mustard seeds, ginger and curry leaves in oil.",
            "Add tempering to rice mixture.",
            "Serve chilled."
        ]
    },
    {
        "name": "Vegetable Kurma",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["mixed vegetables", "coconut", "spices", "onion"],
        "steps": [
            "Grind coconut with spices to a paste.",
            "Cook vegetables with onion and add paste.",
            "Simmer until vegetables are tender.",
            "Serve with rice or roti."
        ]
    },
    # North Indian Lunch
    {
        "name": "Rajma",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["kidney beans", "onion", "tomato", "spices"],
        "steps": [
            "Soak kidney beans overnight and boil until soft.",
            "Prepare onion-tomato gravy with spices.",
            "Add cooked beans to gravy and simmer.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Paneer Butter Masala",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["paneer", "butter", "tomato", "cream", "spices"],
        "steps": [
            "Prepare tomato-based gravy with butter and spices.",
            "Add paneer cubes and cook for 10 minutes.",
            "Add cream and simmer.",
            "Serve hot with naan or rice."
        ]
    },
    {
        "name": "Chicken Curry",
        "cuisine": "North Indian",
        "veg": False,
        "meal": "Lunch",
        "ingredients": ["chicken", "onion", "tomato", "spices"],
        "steps": [
            "Sauté onions and spices.",
            "Add chicken and brown.",
            "Add tomato puree and cook till chicken is tender.",
            "Serve hot with rice or roti."
        ]
    },
    {
        "name": "Dal Tadka",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["yellow lentils", "onion", "tomato", "mustard seeds", "spices"],
        "steps": [
            "Cook lentils until soft.",
            "Prepare tempering with mustard seeds, onion, tomato and spices.",
            "Add tempering to cooked lentils.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Aloo Gobi",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["potato", "cauliflower", "onion", "tomato", "spices"],
        "steps": [
            "Sauté onions and spices.",
            "Add potatoes and cauliflower.",
            "Cook till tender.",
            "Serve hot."
        ]
    },
    # Chinese Lunch
    {
        "name": "Kung Pao Chicken",
        "cuisine": "Chinese",
        "veg": False,
        "meal": "Lunch",
        "ingredients": ["chicken", "peanuts", "chilies", "soy sauce", "garlic"],
        "steps": [
            "Marinate chicken with soy sauce and spices.",
            "Stir fry chicken with garlic and chilies.",
            "Add peanuts and sauce.",
            "Cook until sauce thickens.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Vegetable Chow Mein",
        "cuisine": "Chinese",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["noodles", "cabbage", "carrot", "soy sauce", "onion"],
        "steps": [
            "Boil noodles and drain.",
            "Stir fry vegetables with soy sauce.",
            "Add noodles and toss well.",
            "Serve hot."
        ]
    },
    {
        "name": "Sweet and Sour Pork",
        "cuisine": "Chinese",
        "veg": False,
        "meal": "Lunch",
        "ingredients": ["pork", "pineapple", "capsicum", "vinegar", "ketchup"],
        "steps": [
            "Fry pork pieces until crispy.",
            "Prepare sweet and sour sauce with vinegar and ketchup.",
            "Add pork and vegetables to sauce.",
            "Cook for 5 mins.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Chinese",
        "veg": False,
        "meal": "Lunch",
        "ingredients": ["tofu", "minced pork", "chili bean paste", "garlic", "ginger"],
        "steps": [
            "Stir fry minced pork with garlic and ginger.",
            "Add chili bean paste and tofu cubes.",
            "Simmer for 10 mins.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Egg Fried Rice",
        "cuisine": "Chinese",
        "veg": False,
        "meal": "Lunch",
        "ingredients": ["rice", "egg", "soy sauce", "spring onion", "peas"],
        "steps": [
            "Cook rice and cool.",
            "Scramble eggs in a pan.",
            "Add rice, soy sauce, peas and spring onion.",
            "Fry together and serve hot."
        ]
    },
    # Italian Lunch
    {
        "name": "Margherita Pizza",
        "cuisine": "Italian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["pizza dough", "tomato sauce", "mozzarella", "basil"],
        "steps": [
            "Preheat oven to 220°C.",
            "Roll out pizza dough.",
            "Spread tomato sauce over dough.",
            "Add mozzarella and basil leaves.",
            "Bake for 15-20 mins until crust is golden.",
            "Serve hot."
        ]
    },
    {
        "name": "Lasagna",
        "cuisine": "Italian",
        "veg": False,
        "meal": "Lunch",
        "ingredients": ["lasagna sheets", "minced beef", "tomato sauce", "cheese", "bechamel sauce"],
        "steps": [
            "Cook minced beef with tomato sauce.",
            "Layer lasagna sheets with meat sauce and bechamel.",
            "Top with cheese and bake at 180°C for 45 mins.",
            "Serve hot."
        ]
    },
    {
        "name": "Pasta Alfredo",
        "cuisine": "Italian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["fettuccine", "cream", "parmesan", "butter", "garlic"],
        "steps": [
            "Cook fettuccine until al dente.",
            "Prepare sauce with butter, garlic, cream and parmesan.",
            "Mix pasta with sauce.",
            "Serve hot."
        ]
    },
    {
        "name": "Risotto",
        "cuisine": "Italian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["arborio rice", "vegetable broth", "parmesan", "onion", "white wine"],
        "steps": [
            "Sauté onion and rice.",
            "Add white wine and let absorb.",
            "Add broth gradually, stirring continuously.",
            "Cook until creamy.",
            "Add parmesan and serve."
        ]
    },
    {
        "name": "Caprese Salad",
        "cuisine": "Italian",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["tomato", "mozzarella", "basil", "olive oil", "balsamic vinegar"],
        "steps": [
            "Slice tomato and mozzarella.",
            "Arrange on plate alternating slices.",
            "Add basil leaves.",
            "Drizzle olive oil and balsamic vinegar.",
            "Serve fresh."
        ]
    },
    # Japanese Lunch
    {
        "name": "Sushi Rolls",
        "cuisine": "Japanese",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["sushi rice", "nori sheets", "cucumber", "avocado", "carrot", "soy sauce"],
        "steps": [
            "Prepare sushi rice with vinegar.",
            "Place nori sheet on bamboo mat.",
            "Spread rice on nori evenly.",
            "Add vegetable strips.",
            "Roll tightly and slice.",
            "Serve with soy sauce."
        ]
    },
    {
        "name": "Tempura",
        "cuisine": "Japanese",
        "veg": False,
        "meal": "Lunch",
        "ingredients": ["shrimp", "vegetables", "tempura batter", "oil"],
        "steps": [
            "Prepare batter with flour and cold water.",
            "Dip shrimp and vegetables in batter.",
            "Deep fry until crispy.",
            "Serve with dipping sauce."
        ]
    },
    {
        "name": "Ramen",
        "cuisine": "Japanese",
        "veg": False,
        "meal": "Lunch",
        "ingredients": ["ramen noodles", "pork", "egg", "broth", "scallion"],
        "steps": [
            "Prepare pork broth.",
            "Cook ramen noodles.",
            "Assemble noodles, broth, sliced pork, boiled egg, and scallions in bowl.",
            "Serve hot."
        ]
    },
    {
        "name": "Katsu Curry",
        "cuisine": "Japanese",
        "veg": False,
        "meal": "Lunch",
        "ingredients": ["pork cutlet", "curry sauce", "rice"],
        "steps": [
            "Bread and deep fry pork cutlet.",
            "Prepare Japanese curry sauce.",
            "Serve cutlet over rice topped with curry."
        ]
    },
    {
        "name": "Udon Noodle Soup",
        "cuisine": "Japanese",
        "veg": True,
        "meal": "Lunch",
        "ingredients": ["udon noodles", "broth", "scallions", "tofu"],
        "steps": [
            "Cook udon noodles.",
            "Prepare broth.",
            "Add noodles, tofu, and scallions to broth.",
            "Serve hot."
        ]
    },
    # South Indian Dinner
    {
        "name": "Chicken Chettinad",
        "cuisine": "South Indian",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["chicken", "coconut", "chettinad spices", "onion", "tomato"],
        "steps": [
            "Grind coconut and spices to a paste.",
            "Sauté onions and tomatoes.",
            "Add chicken and paste, cook till done.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Vegetable Biryani",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["rice", "mixed vegetables", "yogurt", "spices"],
        "steps": [
            "Cook vegetables with spices.",
            "Layer cooked rice and vegetables with yogurt.",
            "Cook on low flame to blend flavors.",
            "Serve with raita."
        ]
    },
    {
        "name": "Fish Curry",
        "cuisine": "South Indian",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["fish", "tamarind", "coconut", "spices"],
        "steps": [
            "Prepare tamarind extract.",
            "Cook fish with tamarind and coconut-based gravy.",
            "Simmer till fish is cooked.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Pongal (Ven Pongal)",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["rice", "moong dal", "black pepper", "ginger", "curry leaves"],
        "steps": [
            "Cook rice and moong dal together.",
            "Temper with pepper, ginger, and curry leaves in ghee.",
            "Mix and serve hot."
        ]
    },
    {
        "name": "Dosa",
        "cuisine": "South Indian",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["rice", "urad dal", "fenugreek seeds"],
        "steps": [
            "Soak rice, urad dal and fenugreek seeds overnight.",
            "Grind into batter and ferment.",
            "Make thin pancakes on a hot griddle.",
            "Serve with chutney and sambar."
        ]
    },
    # North Indian Dinner
    {
        "name": "Tandoori Chicken",
        "cuisine": "North Indian",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["chicken", "yogurt", "spices", "lemon"],
        "steps": [
            "Marinate chicken in yogurt and spices overnight.",
            "Cook in tandoor or oven until charred and cooked.",
            "Serve hot with salad and lemon wedges."
        ]
    },
    {
        "name": "Dal Makhani",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["whole black lentils", "kidney beans", "butter", "cream", "spices"],
        "steps": [
            "Soak lentils and beans overnight.",
            "Cook lentils and beans until soft.",
            "Prepare tomato-based gravy with butter and spices.",
            "Add lentils and cream, simmer for hours.",
            "Serve hot with naan."
        ]
    },
    {
        "name": "Baingan Bharta",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["eggplant", "onion", "tomato", "spices"],
        "steps": [
            "Roast eggplant until skin chars.",
            "Peel and mash the pulp.",
            "Cook with onions, tomatoes and spices.",
            "Serve hot with roti."
        ]
    },
    {
        "name": "Chicken Korma",
        "cuisine": "North Indian",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["chicken", "yogurt", "nuts", "cream", "spices"],
        "steps": [
            "Marinate chicken with yogurt and spices.",
            "Cook with nuts and cream-based gravy.",
            "Simmer until tender.",
            "Serve hot with naan or rice."
        ]
    },
    {
        "name": "Roti",
        "cuisine": "North Indian",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["wheat flour", "water", "salt"],
        "steps": [
            "Make dough with wheat flour, water, and salt.",
            "Roll into flat discs.",
            "Cook on hot tawa until golden spots appear.",
            "Serve hot."
        ]
    },
    # Chinese Dinner
    {
        "name": "Sweet and Sour Chicken",
        "cuisine": "Chinese",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["chicken", "pineapple", "capsicum", "vinegar", "ketchup"],
        "steps": [
            "Fry chicken pieces until crispy.",
            "Prepare sweet and sour sauce with vinegar and ketchup.",
            "Add chicken and vegetables to sauce.",
            "Cook for 5 mins.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Beef and Broccoli",
        "cuisine": "Chinese",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["beef", "broccoli", "soy sauce", "garlic", "ginger"],
        "steps": [
            "Stir fry beef strips with garlic and ginger.",
            "Add broccoli and soy sauce.",
            "Cook until broccoli is tender.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Vegetable Stir Fry",
        "cuisine": "Chinese",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["mixed vegetables", "soy sauce", "garlic", "ginger", "sesame oil"],
        "steps": [
            "Heat sesame oil and stir fry garlic and ginger.",
            "Add mixed vegetables.",
            "Add soy sauce and cook until tender-crisp.",
            "Serve hot."
        ]
    },
    {
        "name": "Hot and Sour Soup",
        "cuisine": "Chinese",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["mushrooms", "tofu", "vinegar", "chili", "egg"],
        "steps": [
            "Boil broth with mushrooms and tofu.",
            "Add vinegar, chili and beaten egg.",
            "Simmer until soup thickens.",
            "Serve hot."
        ]
    },
    {
        "name": "Chow Mein",
        "cuisine": "Chinese",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["noodles", "cabbage", "carrot", "soy sauce", "onion"],
        "steps": [
            "Boil noodles and drain.",
            "Stir fry vegetables with soy sauce.",
            "Add noodles and toss well.",
            "Serve hot."
        ]
    },
    # Italian Dinner
    {
        "name": "Spaghetti Carbonara",
        "cuisine": "Italian",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["spaghetti", "egg", "bacon", "parmesan cheese", "black pepper"],
        "steps": [
            "Cook spaghetti until al dente.",
            "Fry bacon until crisp.",
            "Beat eggs and mix with cheese and pepper.",
            "Drain spaghetti and quickly mix with egg mixture and bacon.",
            "Serve immediately."
        ]
    },
    {
        "name": "Risotto ai Funghi",
        "cuisine": "Italian",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["arborio rice", "mushrooms", "onion", "parmesan", "white wine"],
        "steps": [
            "Sauté onions and mushrooms.",
            "Add rice and cook with wine and broth slowly.",
            "Cook until creamy.",
            "Add parmesan and serve."
        ]
    },
    {
        "name": "Lasagna Bolognese",
        "cuisine": "Italian",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["lasagna sheets", "minced beef", "tomato sauce", "béchamel sauce", "cheese"],
        "steps": [
            "Cook minced beef in tomato sauce.",
            "Layer lasagna sheets with meat sauce and béchamel.",
            "Top with cheese and bake until golden.",
            "Serve hot."
        ]
    },
    {
        "name": "Eggplant Parmesan",
        "cuisine": "Italian",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["eggplant", "tomato sauce", "mozzarella", "parmesan", "breadcrumbs"],
        "steps": [
            "Slice eggplant and coat with breadcrumbs.",
            "Fry until golden.",
            "Layer with tomato sauce and cheeses.",
            "Bake until bubbly.",
            "Serve hot."
        ]
    },
    {
        "name": "Panna Cotta",
        "cuisine": "Italian",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["cream", "sugar", "gelatin", "vanilla"],
        "steps": [
            "Heat cream and sugar.",
            "Add gelatin and vanilla.",
            "Pour into molds and chill until set.",
            "Serve cold."
        ]
    },
    # Japanese Dinner
    {
        "name": "Sukiyaki",
        "cuisine": "Japanese",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["beef", "tofu", "vegetables", "soy sauce", "sugar", "mirin"],
        "steps": [
            "Cook beef in soy sauce, sugar, and mirin broth.",
            "Add tofu and vegetables.",
            "Simmer until cooked.",
            "Serve hot with rice."
        ]
    },
    {
        "name": "Karaage",
        "cuisine": "Japanese",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["chicken", "soy sauce", "ginger", "garlic", "potato starch"],
        "steps": [
            "Marinate chicken with soy sauce, ginger, and garlic.",
            "Coat with potato starch.",
            "Deep fry until crispy.",
            "Serve hot."
        ]
    },
    {
        "name": "Okonomiyaki",
        "cuisine": "Japanese",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["cabbage", "flour", "egg", "green onion", "okonomiyaki sauce"],
        "steps": [
            "Mix cabbage, flour, egg, and green onions.",
            "Cook on a hot griddle to form pancake.",
            "Serve with okonomiyaki sauce and mayo."
        ]
    },
    {
        "name": "Tonkatsu",
        "cuisine": "Japanese",
        "veg": False,
        "meal": "Dinner",
        "ingredients": ["pork cutlet", "flour", "egg", "breadcrumbs", "tonkatsu sauce"],
        "steps": [
            "Coat pork cutlet with flour, egg, and breadcrumbs.",
            "Deep fry until golden.",
            "Serve with tonkatsu sauce."
        ]
    },
    {
        "name": "Chawanmushi",
        "cuisine": "Japanese",
        "veg": True,
        "meal": "Dinner",
        "ingredients": ["egg", "dashi", "soy sauce", "mushrooms", "chicken"],
        "steps": [
            "Beat eggs and mix with dashi and soy sauce.",
            "Add mushrooms and chicken pieces.",
            "Steam until set.",
            "Serve warm."
        ]
    }
]


# Extract unique ingredients
def get_unique_ingredients(recipes):
    ing_set = set()
    for r in recipes:
        for ing in r['ingredients']:
            ing_set.add(ing.lower())
    return sorted(ing_set)

ALL_INGREDIENTS = get_unique_ingredients(RECIPES)

# Filter and rank recipes based on ingredient match and filters
def filter_and_rank_recipes(user_ingredients, cuisine, veg_nonveg, meal):
    user_set = set(i.strip().lower() for i in user_ingredients)
    results = []
    for r in RECIPES:
        if cuisine != "Any" and r['cuisine'] != cuisine:
            continue
        if veg_nonveg != "Any":
            if veg_nonveg == "Veg" and not r['veg']:
                continue
            if veg_nonveg == "Non-Veg" and r['veg']:
                continue
        if meal != "Any" and r['meal'] != meal:
            continue
        recipe_set = set(ing.lower() for ing in r['ingredients'])
        matched_ingredients = user_set.intersection(recipe_set)
        match_score = len(matched_ingredients)
        if match_score > 0:
            penalty = len(recipe_set - user_set)
            final_score = match_score - penalty * 0.5
            results.append((r, final_score))
    results.sort(key=lambda x: x[1], reverse=True)
    return results

def recipe_to_text(recipe):
    text = f"Recipe: {recipe['name']}\nCuisine: {recipe['cuisine']}\nMeal: {recipe['meal']}\nVeg: {'Yes' if recipe['veg'] else 'No'}\n\nIngredients:\n"
    for ing in recipe['ingredients']:
        text += f"- {ing}\n"
    text += "\nSteps:\n"
    for idx, step in enumerate(recipe['steps'], 1):
        text += f"{idx}. {step}\n"
    return text

# -------- UI Styling --------
st.set_page_config(page_title="Foodie Recipe Finder", page_icon="🍽️", layout="centered")

st.markdown("""
<style>
    /* General */
    .stApp {
        background-color: #f7f9fc;
        color: #222222;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Headers */
    .header {
        font-size: 2.75rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    .subheader {
        font-size: 1.25rem;
        color: #555555;
        margin-bottom: 1.75rem;
    }
    /* Recipe Card */
    .recipe-card {
        background: white;
        border-radius: 10px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 5px 12px rgba(0,0,0,0.08);
        transition: box-shadow 0.3s ease;
    }
    .recipe-card:hover {
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }
    .recipe-title {
        color: #e74c3c;
        font-weight: 700;
        font-size: 1.7rem;
        margin-bottom: 8px;
    }
    .recipe-meta {
        color: #888888;
        font-size: 0.95rem;
        margin-bottom: 12px;
        font-style: italic;
    }
    /* Buttons */
    .css-1emrehy.edgvbvh3 {  /* Streamlit button class */
        background-color: #e74c3c;
        color: white;
        font-weight: 600;
    }
    .css-1emrehy.edgvbvh3:hover {
        background-color: #c0392b;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Session state for pages
if "page" not in st.session_state:
    st.session_state.page = "input"
if "results" not in st.session_state:
    st.session_state.results = []

def show_input_page():
    st.markdown('<div class="header">Foodie Recipe Finder 🍽️</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Select ingredients you have or add your own, then find recipes!</div>', unsafe_allow_html=True)

    selected_ingredients = st.multiselect(
        "Select ingredients you have:",
        options=ALL_INGREDIENTS,
        default=[],
        help="Scroll and select ingredients you have"
    )
    custom_ingredients_input = st.text_input(
        "Add other ingredients not in list (comma separated):",
        placeholder="e.g. quinoa, kale"
    )
    custom_ingredients = [ing.strip().lower() for ing in custom_ingredients_input.split(",") if ing.strip()]
    final_ingredients = list(set(selected_ingredients + custom_ingredients))

    cuisine = st.selectbox("Select Cuisine", options=["Any", "North Indian", "South Indian", "Chinese", "Italian", "Japanese"])
    veg_nonveg = st.selectbox("Veg or Non-Veg", options=["Any", "Veg", "Non-Veg"])
    meal = st.selectbox("Meal Type", options=["Any", "Breakfast", "Lunch", "Dinner"])

    if st.button("Find Recipes"):
        if not final_ingredients:
            st.warning("Please select or enter at least one ingredient.")
        else:
            results = filter_and_rank_recipes(final_ingredients, cuisine, veg_nonveg, meal)
            if not results:
                st.info("No matching recipes found. Try broadening your ingredient list or changing filters.")
            else:
                st.session_state.results = results
                st.session_state.page = "results"
                st.session_state.user_ingredients = final_ingredients
                st.session_state.filters = (cuisine, veg_nonveg, meal)
                st.experimental_rerun()

def show_results_page():
    st.markdown('<div class="header">Recipe Results 🍳</div>', unsafe_allow_html=True)

    st.markdown(f"### Recipes matching your ingredients and filters:")
    st.markdown(f"**Your Ingredients:** {', '.join(st.session_state.user_ingredients)}")
    cuisine, veg_nonveg, meal = st.session_state.filters
    st.markdown(f"**Cuisine:** {cuisine} | **Veg/Non-Veg:** {veg_nonveg} | **Meal:** {meal}")

    if st.button("← Back to Search"):
        st.session_state.page = "input"
        st.experimental_rerun()

    results = st.session_state.results

    if not results:
        st.info("No recipes found.")
        return

    for idx, (recipe, score) in enumerate(results, 1):
        with st.container():
            st.markdown(f'<div class="recipe-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="recipe-title">{idx}. {recipe["name"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="recipe-meta">{recipe["cuisine"]} | {"Veg" if recipe["veg"] else "Non-Veg"} | {recipe["meal"]}</div>', unsafe_allow_html=True)
            st.markdown(f"**Ingredients:** {', '.join(recipe['ingredients'])}")
            st.markdown("**Steps:**")
            for i, step in enumerate(recipe['steps'], 1):
                st.write(f"{i}. {step}")
            st.download_button(
                label="Download Recipe",
                data=recipe_to_text(recipe),
                file_name=f"{recipe['name'].replace(' ', '_').lower()}_recipe.txt",
                mime="text/plain",
                key=f"download_{idx}"
            )
            st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.page == "input":
    show_input_page()
else:
    show_results_page()
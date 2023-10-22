# -*- coding: utf-8 -*-
"""Streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aY4ESfaW1f6gcQ7EALdYKipqliAbkUHq
"""

import streamlit as st

def main():
    st.title("Player Rating Prediction")
    # Train the model
model = GradientBoostingRegressor()
model.fit(Xtrain, Ytrain)

# Save the trained model to a file
with open('/content/drive/My Drive/Colab Notebooks/FIFA_Player_Ratings/GBRtrained_model.pkl', 'wb') as f:
    pickle.dump(model, f)


    features_list = ['overall', 'potential', 'movement_reactions', 'passing', 'mentality_composure', 'dribbling',
                     'release_clause_eur', 'wage_eur', 'value_eur', 'power_shot_power', 'physic', 'mentality_vision',
                     'attacking_short_passing', 'shooting', 'goalkeeping_speed', 'skill_long_passing', 'age',
                     'skill_ball_control', 'international_reputation', 'league_level']



    st.write("Enter 10 features from the list below to continue:")
    selected_features = st.multiselect("Features", features_list, key="features", default=[])

    if len(selected_features) == 10:
        feature_values = []

        for feature in selected_features:
            value = st.text_input(f"Enter value for {feature}", key=feature)
            feature_values.append(value)

        if st.button("Predict"):
            # Call your prediction function with the feature values and display the result
            prediction = predict_rating(feature_values)
            st.success(f"The predicted rating is: {prediction}")

    else:
        st.warning("Please select exactly 10 features.")

def predict_rating(features):

    return model.predict(features)

if __name__ == '__main__':
    main()

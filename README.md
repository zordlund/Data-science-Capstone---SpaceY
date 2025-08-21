SpaceX Launch Prediction – IBM Data Science Capstone

This repository contains my capstone project from the IBM Data Science Professional Certificate.
The task was to act as a consultant for the fictional company SpaceY and build a model that could predict whether SpaceX Falcon 9 first stage boosters would land successfully.

Project Overview

The project covers the full data science workflow:

Data collection via the SpaceX API and Wikipedia web scraping

Data wrangling & feature engineering to create a target class

Exploratory data analysis using visualization, SQL queries, geospatial maps (Folium), and an interactive dashboard (Plotly Dash)

Predictive modelling using multiple classification algorithms (Logistic Regression, SVM, KNN, Decision Tree) with hyperparameter tuning

The best performing models were Logistic Regression and SVM, both reaching around 83% accuracy. While the results are promising, the dataset was relatively small, so a larger dataset would likely improve the models further.

Reflections

Working on this project was both challenging and rewarding. It pushed me to combine different skills I had learned throughout the certificate, from Python programming and SQL to machine learning and dashboard creation. 
I especially enjoyed experimenting with different modelling strategies and noticing how small methodological changes (such as stratifying train/test splits and avoiding data leakage) affected the results.

For me, the real takeaway is not only that machine learning can help support decision-making in complex domains like space exploration, but also how important it is to critically evaluate data quality, dataset size, and methodological choices before trusting predictions.

Repository Structure

Data collection (API & web scraping) notebooks

Data wrangling notebook

EDA (visualization & SQL) notebooks

Geospatial mapping (Folium) notebook

Dashboard app (Plotly Dash)

Machine learning notebook (classification & evaluation)

Acknowledgements

This project was completed as part of the IBM Data Science Professional Certificate on Coursera.


# BOSTON HOMES 🌴🏠🌴

Welcome to our website that predicts the housing prices in Boston. Our website utilizes machine learning techniques to provide accurate and reliable predictions for potential buyers and sellers in the Boston housing market. Our ensemble learning algorithm combines multiple models to improve the accuracy and generalization of the predictions. So, let's get started and explore the fascinating world of machine learning and the Boston housing market! 

#### 

## DISCLAIMER ⚠️

This web application is a proof-of-concept project and the predictions generated here are for educational and informational purposes only. The data used in this project is provided as-is, without any guarantee or warranty from the creator, and should not be used to make any real-world housing market decisions. If you choose to use the predictions for any purpose, you do so at your own risk and the creator is not responsible for any damages or losses that may result. It is important to note that this project is intended to demonstrate the potential of machine learning and deep learning in the real estate industry if developed at a large scale and with authentic and verified data.

## MOTIVATION 💪

The real estate market in Boston, USA was experiencing high demand and low inventory, leading to increasing prices for both rental and sales properties. The market conditions are constantly changing, and it's important to consult up-to-date sources for the latest information on the Boston real estate market.

- Here are the factors that will be used to predict house prices in this project:

1. CRIM: per capita crime rate by town
2. ZN: proportion of residential land zoned for lots over 25,000 sq.ft.
3. INDUS: proportion of non-retail business acres per town
4. CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise)
5. NOX: nitric oxides concentration (parts per 10 million)
6. RM: average number of rooms per dwelling
7. AGE: proportion of owner-occupied units built prior to 1940
8. DIS: weighted distances to five Boston employment centers
9. RAD: index of accessibility to radial highways
10. TAX: full-value property-tax rate per $10,000
11. PTRATIO: pupil-teacher ratio by town
12. B: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
13. LSTAT: % lower status of the population

## DATA SOURCE 📊

- [The Boston House Dataset ](https://www.kaggle.com/code/prasadperera/the-boston-housing-dataset/notebook)

## Software And Tools Requirements

1. [Github Account](https://github.com)
2. [HerokuAccount](https://heroku.com)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

# Built with 🛠️

<code><img height="70" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code> &nbsp;
<code><img height="70" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png"></code> &nbsp;
<code><img height="70" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png"></code> &nbsp;
<code><img height="70" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png"></code> &nbsp;
<code><img height="70" src="https://github.com/tomchen/stack-icons/raw/master/logos/bootstrap.svg"></code> &nbsp;
<code><img height="70" src="https://cdn.iconscout.com/icon/free/png-256/heroku-225989.png"></code> &nbsp;

<code><img height="70" src="https://raw.githubusercontent.com/numpy/numpy/7e7f4adab814b223f7f917369a72757cd28b10cb/branding/icons/numpylogo.svg"></code> &nbsp;
<code><img height="70" src="https://raw.githubusercontent.com/pandas-dev/pandas/761bceb77d44aa63b71dda43ca46e8fd4b9d7422/web/pandas/static/img/pandas.svg"></code> &nbsp;
<code><img height="70" src="https://matplotlib.org/_static/logo2.svg"></code> &nbsp;
<code><img height="70" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png"></code> &nbsp;

<code><img height="70" src="https://user-images.githubusercontent.com/79560110/229375410-567cf168-204a-4210-be7e-8c3d614076cf.png"></code> &nbsp;
<code><img height="70" src="https://user-images.githubusercontent.com/79560110/229375710-35f11050-e33c-46dd-84c6-cc4265761597.png"></code> &nbsp;

## DEPLOYMENT 🚀

#### Deployment is done using [deploy](https://github.com/dhyeyjoshi/BostonHousePrice-Predictor) branch
#### This website is deployed at [Heroku](https://www.heroku.com/)
#### You can access it [here](https://bostonhomes.herokuapp.com/)
#### Note: The website may take a minute to load sometimes, as the server may be in hibernate state

## How to use 💻

- Boston House Price Predictor ==> This simple and user-friendly web app is designed to predict Boston house prices using an ensemble learning algorithm. With just a few clicks, you can input random int or float values for the parameters, and the app will estimate the price of the house based on those values. 
    - Simply click on the search icon to access the parameters section, fill in the values, and hit the Estimate Price button. 
    - The page will reload and display the predicted price at the bottom of the search section. 
    - Try it out now and experience the power of machine learning in predicting Boston house prices!

- Based on my analysis of the Boston Housing Dataset, the following features are important in predicting the housing prices in Boston:
<pre>
    RM: average number of rooms per dwelling
    LSTAT: % lower status of the population
    PTRATIO: pupil-teacher ratio by town
    DIS: weighted distances to five Boston employment centers
    NOX: nitric oxides concentration (parts per 10 million)
    TAX: full-value property-tax rate per $10,000
    CRIM: per capita crime rate by town </pre>
      - These features have the strongest correlations with the median value of owner-occupied homes, and are therefore the most important predictors of housing prices in Boston. Machine learning models trained on these features can be used to accurately predict housing prices in Boston.

## How to run locally 🛠️

- Before the following steps make sure you have [git](https://git-scm.com/download), [Anaconda](https://www.anaconda.com/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system
- Clone the complete project with `https://github.com/dhyeyjoshi/BostonHousePrice-Predictor.git` or you can just download the code and unzip it
- **Note:** The master branch doesn't have the updated code used for deployment, to download the updated code used for deployment.

- I have not created any sperate branch to deploy the application, `master` branch has not only the code required for deploying the app but also the code that was used for training the models, data preparation.

- Once the project is cloned, open anaconda prompt in the directory where the project was cloned and paste the following block

  ```
  conda create -p venv python==3.7 -y
  conda activate venv/
  pip install -r requirements.txt
  ```
- And finally run the project with
  ```
  python app.py
  ```
- Open the localhost url provided after running `app.py` and now you can use the project locally in your web browser.

## What's the use of `Dockerfile`?
   - I have used Heroku to deploy our web application through GitHub Action using Docker. 
   - I set up the Heroku Continuous Integration and Deployment (CI/CD) pipelines using Git as a single source of truth.
### Benefits of having an Heroku CI/CD pipeline:
<pre>
    1. Improved code quality and testability
    2. Faster development and code review
    3. Risk mitigation
    4. Deploy more often</pre>
<code><img height="300" width="1500" src="https://user-images.githubusercontent.com/79560110/229378443-fa354149-8c34-458c-b89c-23513df3ceda.png"></code> &nbsp;
    
## DEMO

### Boston-House Price Prediction System

- Working of Web App - [Demo-Video](https://github.com/dhyeyjoshi/BostonHousePrice-Predictor/blob/main/Demo-Video.mp4) 

  - Working of `Predict_API`- 
  
<code><img  src="https://user-images.githubusercontent.com/79560110/229380218-b164483c-4fac-4a54-8add-09fb78a5d863.gif"></code> &nbsp;

## Usage ⚙️
You can use this project for further developing it and adding your work in it. If you use this project, kindly mention the original source of the project and mention the link of this repo in your report.

## Further Improvements 📈
This was my first big project so there are lot of things to improve upon

- CSS code is totally messed up :pensive: (some code in file and some inline)
- Frontend can be made more nicer (PS: I suck at frontend development) :cry:	
- More data can be collected manually via web scrapping to make the system more accurate :monocle_face:	
- Modularized code can be written instead of writing in Jupyter Notebooks (will follow this in upcoming projects)

## License 📝
This project is licensed under [Apache License 2.0](https://github.com/dhyeyjoshi/BostonHousePrice-Predictor/blob/main/LICENSE).

## Contact 📞

#### If you have any doubt or want to contribute feel free to email me or hit me up on [LinkedIn](https://www.linkedin.com/in/dhyey-joshi12/)

# What To Watch

## A movie and tv show recommendation system project

_Author: Gracie Bryan_

### Project Overview

> The purpose of this project is to develop a system for recommending movies and tv shows using a machine learning model trained with the [IMDB dataset found on Kaggle](https://www.kaggle.com/datasets/ashirwadsangwan/imdb-dataset) and user data.
>
> It will consist of a machine learning model, an API to access the model, and a front end for user interaction.
>
> It will utilise AWS resources to create the ML model as well as host the API and front end.
>
> The necessary Amazon Cloud services will be setup with Terraform. The API will be written in Python with the FastAPI library, and the front end will be built with React.

### ChatGPT

> The idea for this application came from talking with the [ChatGPT](https://chat.openai.com/chat) chatbot.
> The conversation can be found [here](ChatGPT.md).

### Project Plan

> 1.  #### Gather and prepare the dataset.
>
>     > - Download the IMDB dataset from Kaggle: https://www.kaggle.com/PromptCloudHQ/imdb-data
>     >
>     > - Use a tool like Pandas in Python to read and manipulate the data. Pandas is a popular data analysis library that makes it easy to work with CSV/TSV data in Python. You can use it to load the IMDB data into a Pandas DataFrame, which is a structured, tabular data structure that allows you to easily manipulate and analyze the data.
>     >
>     > - Clean and prepare the data for use in your machine learning model. Depending on the specific requirements of your project, you may need to do some preprocessing on the IMDB data to clean and prepare it for use in your machine learning model. This could include tasks such as removing missing or invalid data, normalizing data values, and generating new features or derived data.
>
> 2.  #### Use Terraform to set up your AWS resources.
>
>     Start by creating an AWS account and installing Terraform on your local machine. Then, create a new Terraform project and define the necessary AWS resources in your main.tf file. This should include an Amazon S3 bucket for storing your datasets and the front-end application, an Amazon SageMaker notebook instance for training your machine learning model, an Amazon EC2 instance for hosting your back-end API, and an Amazon RDS instance for storing your user data in a traditional database.
>
> 3.  #### Train your machine learning model.
>
>     Use the Amazon SageMaker notebook instance to train a machine learning model using the IMDB dataset. You can experiment with different algorithms and parameters to find the best model for your purposes. For example, you could use a k-nearest neighbors algorithm to make recommendations based on the similarity of movies and TV shows.
>
> 4.  #### Set up a system for continuously training the model.
>
>     Use the Amazon RDS instance to store user data in a traditional database, and set up a system that periodically fetches that data, trains the machine learning model on it, and saves the updated model back to Amazon S3. This will allow you to continuously improve the model's performance over time.
>
> 5.  #### Build the back-end API.
>
>     Use Python and FastAPI to create a RESTful API that allows your front-end application to interact with the machine learning model and the AWS resources you created. The API should provide endpoints for retrieving movie and TV show recommendations, as well as for storing and retrieving user preferences. You can use the Amazon EC2 instance you created to host the API and make it accessible to the front-end application.
>
> 6.  #### Build the front-end application.
>     Use React to create a web-based interface that allows users to input their preferences and receive recommendations from the machine learning model. The front-end application should communicate with the back-end API to retrieve data and send user input. You can use the AWS S3 bucket to store the front-end application and make it accessible to users.

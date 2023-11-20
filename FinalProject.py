import streamlit  as st
from streamlit_option_menu import option_menu
#from streamlit_lottie import st_lottie
from PIL import Image
#import requests
import pandas as pd
with st.container():
    selected=option_menu("Final Project", ["Predicting Breast Cancer in a patient","E-commerce Customer Segmentation", "Predicting Term Deposit Subscription by a client"], icons=['hospital' ,'cart2', 'bank'], menu_icon="brightness-alt-high", default_index=0)
    st.write("---")

    #def load_lottieurl1(url):  # Importing/Loading lottie URL
       # r = requests.get(url)
       # if r.status_code != 200:
        #    return None
       # return r.json()
    # up_left_column, up_right_column = st.columns(2)
    def Breast_Prediction():
        st.header("""Predicting Breast Cancer in a patient""")
        title1 = """Abstract:
                       Breast cancer represents one of the diseases that make a high number of deaths every
                       year. It is the most common type of all cancers and the main cause of women's deaths
                       worldwide. Classification and data mining methods are an effective way to classify data.
                       Especially in the medical field, where those methods are widely used in diagnosis and
                       analysis to make decisions."""
        title2 = """Problem Statement:
                       Given the details of cell nuclei taken from breast mass, predict whether or not a patient
                       has breast cancer using the Ensembling Techniques. Perform necessary exploratory
                       data analysis before building the model and evaluate the model based on performance
                       metrics other than model accuracy."""
        title3 = """Dataset Information:
                       The dataset consists of several predictor variables and one target variable, Diagnosis.
                       The target variable has values 'Benign' and 'Malignant', where 'Benign' means that the
                       cells are not harmful or there is no cancer and 'Malignant' means that the patient has
                       cancer and the cells have a harmful effect."""
        st.write()
        st.write(title1)
        st.write(title2)
        st.write(title3)
        st.write("---")
        #lottie_coding3 = load_lottieurl1("https://lottie.host/acb222ab-625b-4ea6-83ed-d0e85f78c638/7eYE054R13.json")
        #st_lottie(lottie_coding3, height=200, key="cod03")
        st.write("---")
        with st.container():
            up_left_column1, up_right_column1 = st.columns(2)
            #
            with up_left_column1:
                st.write("There are 357-'Benign' & 212-'Malignant'patients:")
                st.write("---")
                image_file = Image.open(r"C:\swathi\Practice dataset\B1.png")
                st.image(image_file, use_column_width=True)

            with up_right_column1:
                st.write("* Accuracy:")
                st.write("---")
                st.text("Accuracy on Training data : 91.20%")
                st.text("Accuracy on Test data : 93.56 %")
                st.text("* Score on Malignant")
                st.text("Precision = 94%")
                st.text("Recall = 86%")
                st.text("F1 Score = 90%")
                st.text("* Score on Bengin")
                st.text("Precision = 93 %")
                st.text("Recall = 97 %")
                st.text("F1 Score = 95 %")

            with st.container():
                st.write("---")
                st.write("* Checking for Correlation: ")
                image_filec = Image.open(r"C:\swathi\Practice dataset\BC_Corr.png")
                st.image(image_filec, use_column_width=True)

    def ECommerce():
        st.header("""E-commerce Customer Segmentation""")
        title5 = """Abstract:
                            A key challenge for e-commerce businesses is to analyze the trend in the market to increase their sales. 
                            The trend can be easily observed if the companies can group the customers; based on their activity on the e-commerce site. 
                            This grouping can be done by applying different criteria like previous orders, mostly searched brands and so on."""
        title6 = """Problem Statement:
                            Given the e-commerce data, use k-means clustering algorithm to cluster customers with similar interest."""
        title7 = """Dataset Information:
                            The data was collected from a well known e-commerce website over a period of time based on the customer’s search profile."""
        st.write()
        st.write(title5)
        st.write(title6)
        st.write(title7)
        st.markdown("[E-commerce Segmentation](https: // github.com / swathinagarajan1996 / E - commerce - Customer - Segmentation)")
        st.write("---")
        #lottie_coding2 = load_lottieurl1("https://lottie.host/ed7a3629-c21e-4bcf-bafe-a0e325dc2700/wrF4JQsR0B.json")
        #st_lottie(lottie_coding2, height=200, key="cod02")
        st.write("---")
        with st.container():
            up_left_column2, up_right_column2 = st.columns([1, 2])
            #
            with up_left_column2:
                st.write("* Female - 22054 & Male - 5222")
                st.write("---")
                image_file0 = Image.open(r"C:\swathi\Practice dataset\E1.png")
                st.image(image_file0, width='auto', use_column_width=True)
                st.text("")
                #
            with up_right_column2:
                st.write("* Orders made by Genders:")
                st.write("---")
                image_file1 = Image.open(r"C:\swathi\Practice dataset\E2.png")
                st.image(image_file1, width='auto', use_column_width=True)
                st.text(" ")
        with st.container():
            st.write("KMeans(n_clusters=4, random_state=10)")
            st.write("---")
            st.text("For n_clusters = 4, silhouette_score = 0.28882936660509695")
            st.text("For n_clusters = 5, silhouette_score = 0.2734507732644251")
            st.text("For n_clusters = 6, silhouette_score = 0.21945733520583072")
            st.text("For n_clusters = 7, silhouette_score = 0.2038118827349176")
            st.text("For n_clusters = 8, silhouette_score = 0.19969011593383135")


    def Term_Deposit_Prediction():
        st.header("""Predicting Term Deposit Subscription by a client""")
        title9 = """Abstract:
                    Marketing campaigns are characterized by focusing on the customer needs and their
                    overall satisfaction. Nevertheless, there are different variables that determine whether a
                    marketing campaign will be successful or not. There are certain variables that we need
                    to take into consideration when making a marketing campaign.
                    A Term deposit is a deposit that a bank or a financial institution offers with a fixed rate
                    (often better than just opening a deposit account) in which your money will be returned
                    back at a specific maturity time."""
        title10 = """Problem Statement:
                    Predict if a customer subscribes to a term deposits or not, when contacted by a
                    marketing agent, by understanding the different features and performing predictive
                    analytics"""
        title11 = """Dataset Information:
                    The data is related with direct marketing campaigns of a Portuguese banking
                    institution. The marketing campaigns were based on phone calls. Often, more than one
                    contact to the same client was required, in order to assess if the product (bank term
                    deposit) would be ('yes') or not ('no') subscribed.
                    The dataset consists of several predictor variables and one target variable, Outcome.
                    Predictor variables includes the age, job, marital status, and so on"""
        st.write()
        st.write(title9)
        st.write(title10)
        st.write(title11)
        st.markdown("[Predicting Term Deposit](https://github.com/swathinagarajan1996/Predicting-Term-Deposit-Subscription-by-a-client/blob/main/Predicting%20Term%20Deposit%20Subscription%20by%20%20a%20client%20_new.ipynb)")
        st.write("---")
        #lottie_coding1 = load_lottieurl1("https://lottie.host/fea04366-64b6-40e2-9cd8-d4f22f70194c/fYKGyM41v6.json")
        #st_lottie(lottie_coding1, height=200, key="cod01")
        st.write("---")
        with st.container():
            st.write("* Age visualization:")
            st.write("---")
            image_file5 = Image.open(r"C:\swathi\Practice dataset\D1.png")
            st.image(image_file5, width='auto', use_column_width=True)
            st.write("---")
        with st.container():
            st.write("* Marital Vs Job:")
            st.write("---")
            image_file5 = Image.open(r"C:\swathi\Practice dataset\D2.png")
            st.image(image_file5, width='auto', use_column_width=True)
            st.write("---")
        with st.container():
            st.write("* Y Vs Job:")
            st.write("---")
            image_file5 = Image.open(r"C:\swathi\Practice dataset\D3.png")
            st.image(image_file5, width='auto', use_column_width=True)
            st.write("---")
        with st.container():
            st.text("* SVM using Polynomial kernal with degree of polynomial = 2")
            st.text("Accuracy Of SVM sigmoid kernal:  89.37 %")
            st.text("Precision_Score : 0.98 ")
            st.text("Recall_Score : 0.90 ")
            st.text("F1_Score : 0.94 ")
            #

        with st.container():
            st.write("* Marital Vs Y VS loansubset:")
            st.write("---")
            image_file5 = Image.open(r"C:\swathi\Practice dataset\D4.png")
            st.image(image_file5, width='auto', use_column_width=True)
            st.write("---")
        with st.container():
            st.write("* Correlation")
            st.write("---")
            image_file5 = Image.open(r"C:\swathi\Practice dataset\D5corr.png")
            st.image(image_file5, width='auto', use_column_width=True)
            st.write("---")
if selected == "Predicting Breast Cancer in a patient":
        Breast_Prediction()
        st.write("---")
elif selected == "E-commerce Customer Segmentation":
        ECommerce()
        st.write("---")
elif selected == "Predicting Term Deposit Subscription by a client":
        Term_Deposit_Prediction()
        st.write("---")
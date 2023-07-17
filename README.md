# Phonepe_Pulse_Data_VisualizationExploration

Introducing the Phonepe Data Visualization project, a Python-based solution designed to analyze and visualize data from the Phonepe Pulse Github repository(https://github.com/PhonePe/pulse). The project retrieves data from the repository, transforms it, and securely stores it in a MySQL database. The visualization is presented through an interactive dashboard using Streamlit, Plotly, and other data manipulation libraries, offering multiple pages with diverse visualizations for users to explore.

With a focus on efficiency, security, and user-friendliness, this project provides valuable insights and information about the data within the Phonepe Pulse Github repository. It serves as a data visualization tool for PhonePe's pulse data spanning from 2018 to 2022, enabling users to analyze various metrics related to PhonePe's business performance in an intuitive and interactive manner.

Enjoy exploring the code and gaining valuable insights from the Phonepe Data Visualization project!

## Prerequisites

Prerequisites for the PhonePe Pulse Project:

    Python: Make sure you have Python installed on your system. The project is built using Python, and having Python installed is essential to run the code.
    
    Jupyter Notebook: You'll need Jupyter Notebook installed to execute the project code. Though not explicitly mentioned in the library imports, the project may involve creating and working with Jupyter Notebooks for data exploration and analysis.
    
    GitHub: Ensure you have a GitHub account and know the basics of using Git version control. The project uses GitHub for versioning, collaboration, and sharing code.
    
    MySQL: Install MySQL or have access to a MySQL database. The project involves data extraction, transformation, and storage using MySQL, so having a MySQL server is necessary.
    
    Required Libraries: Install the necessary Python libraries using pip install or any package manager. The essential libraries include:
    
      * pandas
      * streamlit
      * PIL (Python Imaging Library)
      * mysql-connector
      * plotly.express
      * scikit-learn (for LabelEncoder)
      * numpy
      * requests
      * sqlalchemy
      * matplotlib

Ensure all these libraries are installed before running the project code.

With these prerequisites in place, you'll be ready to explore and run the PhonePe Pulse project using Python, Jupyter Notebook, GitHub, and MySQL. Happy coding!


# Installation & Usage

To access the web app, simply open the provided URL in your web browser. Once there, you can start exploring the various features available on each page of the app. The user-friendly interface allows you to interact with the app seamlessly. Provide the necessary inputs based on your specific needs, and in return, you'll receive insightful and interactive visualizations. Enjoy the experience and gain valuable insights from the PhonePe Pulse data at your fingertips.

    1. Clone the repository to your local machine using the following command: git clone https://github.com/preky777/Phonepe_Pulse_Data_VisualizationExploration.git.
    2. Install the required libraries.
    3. Run the .ipynb file to clean and transform the data and generate the CSV files.
    4. Create a MySQL database and tables, define constraints, and push data into MySQL using user-defined functions.
    5. Open a terminal window and navigate to the directory where the app is located using the following command: cd C:\Users\prajw\OneDrive\Desktop\phone3.
    6. Run the Streamlit app using the command [streamlit run Introduction.py] and access the app through the local URL provided.
    7. The app should now be running on a local server. If it doesn't start automatically, you can access it by going to either the given Local URL or Network URL.
    8. Explore the different pages of the app, enter inputs as required, and interact with the visualizations to gain insights into the PhonePe transaction data.


## Components of the Dashboard

    1.Introduction
    
    2.Application
    
    3.Visualization
    
    4.Question_Answer
    

1. Introduction_page:
   "Introduction.py" showcases PhonePe's impact on the digital payments landscape in India, its contribution to the API-driven digitization of payments, and its initiative to give back to the ecosystem through "PhonePe Pulse". The web app offers an engaging and informative introduction to PhonePe with visual elements and downloadable resources.


        * The app starts with a page title "INTRODUCTION" and adds a dynamic PhonePe Pulse GIF for visual appeal.
  
        * It displays the PhonePe logo image and provides a detailed description of PhonePe's role in India's digital payments revolution and its contributions to the ecosystem through "PhonePe Pulse".
        
        * The section "THE BEAT OF PHONEPE" is introduced with a title and an image related to PhonePe is displayed.
        
        * Users can download the PhonePe annual report in PDF format using the "DOWNLOAD REPORT" button.
        
        * An image of the report is also shown to provide users with further insights into PhonePe's activities.
      


  3. Application_page:
     "1_Application.py" presents an informative web app that introduces PhonePe, its background, and its affiliation with UPI, encouraging users to download the app for their digital payment needs.
  

          * The app starts with a page title "APPLICATION" and adds a horizontal line for separation.
    
          * It displays an image of PhonePe with a width of 300 and follows with a subheader describing PhonePe as an Indian company headquartered in Bengaluru, founded in December 2015 by Sameer Nigam, Rahul Chari, and Burzin Engineer. It highlights that PhonePe's app is based on the Unified Payments Interface (UPI) and went live in August 2016. The ownership by Flipkart, a subsidiary of Walmart, is also mentioned.
          
          * To encourage app downloads, the app includes a "DOWNLOAD THE APP NOW" button, linking to the app download page.
          
          * The web app provides additional information about the UPI (Unified Payments Interface) through an embedded video using st.video().
      
      

  4. Visualization_page:
     "2_Visualization.py" provides a comprehensive tool to explore and interpret PhonePe's data, aiding users in making informed decisions based on the visualized information.
  

          * "2_Visualization.py" is an interactive and informative web app that empowers users to explore and gain insights from PhonePe's transaction and user data.
          
          * The app offers various visualization options, including maps and bar graphs, to provide a better understanding of data patterns and trends.
          
          * Users can analyze transaction data and user demographics based on geographical and temporal parameters.
          
          * The web app also presents valuable insights into overall transactions and the user base of the PhonePe platform over the years.
    
          * Additionally, users can easily comprehend top-performing states and districts with key metrics such as registered users, app openings, total transactions, and transaction amounts. 
      


  5. Question_Answer_page:
     "3_Question_Answer.py" provides an interactive interface to explore and visualize various insights related to phonepe pulse data using MySQL queries and bar charts created with Matplotlib.
  

          * The app connects to a MySQL database with specific credentials for the "localhost" server and the "phonepe_visualization" database.
    
          * Users can select a question from a dropdown select box, which includes options such as top states based on year and transaction amount, least states based on transaction type and amount, top transaction types based on transaction amount, top registered users based on state and district, top districts based on state and transaction count, least districts based on state and transaction amount, least transaction count based on districts and state, and top registered users based on state and district.
            
          * Upon selection, the script executes corresponding MySQL queries and transforms the retrieved data into pandas DataFrames.
            
          * The app generates a web page displaying the answer to the selected question, along with horizontal bar charts created using Matplotlib to visualize insights related to the question's context.
            
          * After viewing the answer, users can go back to the select box to explore different questions and insights. The script ensures to close the MySQL cursor and connection once the user finishes interacting with the web application.




## App Screenshots

![Screenshot (19)](https://github.com/preky777/Phonepe_Pulse_Data_VisualizationExploration/assets/107749942/e66ee04e-cf1e-469c-b1c5-510ef43b38fa)
![Screenshot (30)](https://github.com/preky777/Phonepe_Pulse_Data_VisualizationExploration/assets/107749942/960131bb-5a6b-4dca-8792-62c25e414a84)
![Screenshot (21)](https://github.com/preky777/Phonepe_Pulse_Data_VisualizationExploration/assets/107749942/5efb27c6-b475-4dc7-8afe-6b57de4a77ea)
![Screenshot (23)](https://github.com/preky777/Phonepe_Pulse_Data_VisualizationExploration/assets/107749942/880eeb3a-2d25-40e2-8106-d51751d4d9f4)
![Screenshot (22)](https://github.com/preky777/Phonepe_Pulse_Data_VisualizationExploration/assets/107749942/c2932134-d5e1-466b-9023-d4e7a9d7fc50)
![Screenshot (33)](https://github.com/preky777/Phonepe_Pulse_Data_VisualizationExploration/assets/107749942/cc8a1855-293c-4c26-b81f-132e71622e65)
![Screenshot (26)](https://github.com/preky777/Phonepe_Pulse_Data_VisualizationExploration/assets/107749942/0c696797-517c-42a5-81a1-abfdd93a2b6d)
![Screenshot (27)](https://github.com/preky777/Phonepe_Pulse_Data_VisualizationExploration/assets/107749942/6727e30a-58e9-40c7-b708-ad9d4b7d2706)
![Screenshot (32)](https://github.com/preky777/Phonepe_Pulse_Data_VisualizationExploration/assets/107749942/43c67b92-319e-47ff-83a8-2be372d1cdd2)


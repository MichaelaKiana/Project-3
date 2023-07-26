# Project-3

### Summary

[brief summary of the project]

### Overview

##### Data Collection

[Google Books API](https://developers.google.com/books/docs/overview) was used to collect data on books authored by Stephen King and his pen name, Richard Bachman. Restrictions on the API allow for up to 40 rows to be pulled at a time. Our goal is not to have all of the exact books published by the authors, but to have a sufficient amount of data for the development of a dashboard. Obtaining our data required multiple requests. See static/data/get-request.py. MongoDB was used to compile the data into one database, static/data/mongo-king-bachman.json.

##### Data Cleaning

To ensure the quality of our data, our dataset was reviewed using the file, static/data/cleaning-data.ipynb.

The data was examined to find potential duplicate titles. A title was considered a duplicate if the changes in the edition were not substantial (e.g., addition of authors foreword, changes in print style) or if it already existed in the database in English.

Authorship was also examined to confirm that all books in the database were by either Stephen King or his pen name, Richard Bachman. Books that did not include our authors of interest were excluded. Reasons for exclusion include the authors' name appearing in other variables for the book (e.g., the title) or a part of the authors' name being represented among the authors (e.g., Richard L. Bachman).

The resulting dataset contained 201 documents.

##### Developing a Flask App

Our app includes ############### sections.

* Home: Landing page for the app.
* Author: Reviews books published by our authors of interest.
* Book: Reviews a single document in the database.
* About: Summary of the project.

### Authors

* [Michaela Dobbs](https://github.com/MichaelaKiana)
* [Savannah Serrano](https://github.com/SavPepper22)
* [Sarah Stegall-Rodriguez](https://github.com/sarsteg)

### Acknowledgements

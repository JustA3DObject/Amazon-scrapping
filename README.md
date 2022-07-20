# Amazon-Scraping
A project to scrape information about different amazon products using ASIN and country code

## Work flow:
* Using openpyxl library, the code converts ASIN column from spreadsheet to a python list.
* Next it does the same for country code column in spreadsheet.
* Using zip function and amazon product link format ("https://www.amazon.{country}/dp/{asin}"), a list of URLs to look up is created.
* Headers are added so amazon.com dosen't block the code from accessing the content thinking it as a bot.
* URLs from url list are iterated one by one in get function.
* Soup1 variable pulls the HTML of the URL 
* Soup2 variable is prettified version of Soup1
* The try block looks up for an ID in HTML tags named "productTitle" which is used for Product names.
* If an AttributeError occurs, the except block prints 404 Error in terminal and Writes 404 Error in title column of CSV file.
* If no AttributeErrors occured, information about price, details and image url are fetched.
* In the else block code creates 4 headers in the initial run and then appends all the values fetched in the csv file.
* Code stops when while loop ends.

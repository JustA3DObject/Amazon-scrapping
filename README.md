# Amazon-Scrapping
A project to scrape information about different amazon products using ASIN and country code which are provided in a spreadsheet.

## Work flow:
* Using openpyxl library, the code converts ASIN column from spreadsheet to a python list.
* Next it does the same for country code column in spreadsheet.
* Using zip function and amazon product link format ("https://www.amazon.{country}/dp/{asin}"), a list of URLs to look up is created.
* Headers are added so amazon.com dosen't block the code from accessing the content thinking it as a bot.
* While loop is initiated to control number of URLs to be processed.
* URLs from url list are iterated one by one in get function.
* Code checks wheather the page is valid or not by checking response code.
* Soup1 variable pulls the HTML of the URL 
* Soup2 variable is prettified version of Soup1
* A try block tries to pull Product name from the website and throws attribute error if there is none.
* Three more try blocks try to pull Product price, details and image URL from the website and throws attribute error if they are missing.
* If no AttributeErrors occured, information about price, details and image url are written in a dictionary which form list of dictionaries in the loop.
* CSV file is created for better redability in the loop.
* Json file is created from the list named content which is a list of dictionaries after the while loop ends.

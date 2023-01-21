# School Food Scraper

 Scrapes the school lunch menu of finnish schools from the site: "kouluruoka.fi"

 Made by: 0tsoBear
 
This project contains a script and a module that allows you to interact with a school food menu website. The script sends a menu for a specified school to a Telegram chat using the Telegram API. It also uses dotenv to load environment variables from a .env file. The module contains a function that returns a menu for a specified school using the requests and BeautifulSoup libraries.

To use the script, you will need to provide your own Telegram token and chat ID and run the script. To use the function, you will need to import the module and call the function with the name of the school you want to get the menu from. Please note that the name of the school must be in the format "city_schoolname" for the function to work properly. If you are having trouble getting the menu for your school, you can check the correct format by searching for your school on the kouluruoka.fi website and looking at the website address of the school's menu page.

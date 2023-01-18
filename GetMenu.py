import datetime
import requests
from bs4 import BeautifulSoup


# This function takes a date and a string representing the school as input
# and returns a string containing the menu for the given date at the given school.
def ruokalista(thedate, school):
    
    # Format the date into a string in the format '{day}_{month}_{year}' 
    date1 = '{d.day}_{d.month}_{d.year}'.format(d=thedate)

    # Replace the year with an empty string in the formatted date
    date1 = date1.replace(str(datetime.date.today().year), "")

    # Get the HTML content for the given school from the website 'https://kouluruoka.fi/menu/'
    res = requests.get("https://kouluruoka.fi/menu/" + school)
    html_page = res.content

    # Parse the HTML content using the BeautifulSoup library
    soup = BeautifulSoup(html_page, 'html.parser')

    # Extract the menu text for the given date from the parsed HTML content
    soup = soup.find(id=date1)
    text = soup.find_all(text=True)

    
    # Initialize an empty string to hold the extracted menu text
    food = ''

    # A list of HTML tags that we want to exclude from the extracted text
    blacklist = ['h3', "div", "span",]
    
    # Iterate over the extracted text and append only the text that is not
    # inside a tag in the blacklist to the food string
    for t in text:
        if t.parent.name not in blacklist:
            food += '{} '.format(t)

    # Format the food string into a more readable form by replacing certain
    # strings and characters with others, and by adding newline characters
    # at appropriate places
    food = food.replace("Ainesosat: Ravintosisältö (100 g:ssa)", "")
    food = food.rsplit(" * ", 1)
    food = food.pop(0)

    replacements = {
        "N ": "",
        "MU ": "",
        "L ": "",
        "G ": "",
        " S ": "",
        "KM ": "",
        "M ": "",
        "MN": "",
        "VE ": " ",
        "VE*": "",
        "K ": "",
        "VEG": "",
        "  ": ", ",
        ",  ": ", ",
    }

    # iterate over the items in the replacements dictionary
    for substring, replacement in replacements.items():
        # replace each substring with its corresponding replacement
        food = food.replace(substring, replacement)

    # Capitalize the first letter of each word in the food string
    food = food.title()

    # Remove the last character from the food string if it is "S", " ", "," or "N"
    for _ in range (6):
        if food[-1] in ["S", " ",",,", ",", "N"]:
          food = food[:-1]

    # Add a period at the end of the food string
    food = food + "."

    # Print an empty line and return the formatted food string
    print("")
    return food

# Get the current date 
today = (datetime.date.today())
tomorrow = (datetime.date.today() + datetime.timedelta(days=1))

# Call the ruokalista function to get the menu for today at the school. For example:'espoo_olarinkoulu'
print(ruokalista(today, "espoo_olarinkoulu"))
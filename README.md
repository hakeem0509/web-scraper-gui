<h2>Web Scraper with GUI</h2>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>
    <h4>Your project directory should have the following structure:</h4>
    <ul>
        <li class="folder">web_scraper_app/
            <ul>
                <li class="folder">phone_scraper/
                    <ul>
                        <li>settings.py</li>
                        <li class="folder">spiders/
                            <ul>
                                <li>phone_spider.py</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>main.py</li>
            </ul>
        </li>
    </ul>
</body>
</html>


<strong>Description</strong><br>
The Web Scraper with GUI project is a Python-based application that combines web scraping and a graphical user interface (GUI) to provide a user-friendly tool for extracting phone numbers associated with specified names from websites. This project leverages the power of the Scrapy framework for web scraping and Tkinter for creating an interactive GUI.
<br><br>
The project is designed to be a simple yet effective way to scan websites for phone numbers linked to individual names, particularly focusing on Kenyan phone numbers that follow a pattern such as 0711111111. It allows users to enter a website URL and a list of names, and it will crawl the website to find and display phone numbers related to those names.
<br><br>
<strong>Features</strong><br>
<strong>Scrapy Framework:</strong> Utilizes Scrapy for powerful and efficient web scraping.<br>
<strong>Tkinter GUI:</strong> Provides a graphical interface for easy user interaction.<br>
<strong>Customizable Search:</strong> Allows users to input a list of names and a URL to search.<br>
<strong>Phone Number Extraction:</strong> Detects Kenyan phone numbers using a regular expression.<br>

<h2>Installation and Setup</h2>

1. Make sure you have Python installed. Install the required Python packages using pip:

   <i>pip install scrapy</i>

2. Once the files and folders match the structure above, Run the Application: To start the Tkinter-based GUI application, run:

   <i>python main.py</i>


<h2>Usage Instructions</h2>

1. Launch the Application:

    Run main.py to open the GUI application.

2. Enter Website URL:

    In the GUI, enter the URL of the website you want to scan in the "Website URL" field.

3. Enter Names:

    Enter a comma-separated list of names you want to search for in the "Names (comma-separated)" field.

4. Start Scraping:

    Click the "Scrape" button to initiate the web scraping process. The application will crawl the specified website and search for the entered names.

5. View Results:

    Once the scraping process is complete, the results will be displayed in the text area of the GUI. It will show the phone numbers associated with the names you provided.

Example
URL: http://example.com
Names: John Doe, Jane Smith
After clicking "Scrape," the application will search http://example.com for occurrences of "John Doe" and "Jane Smith," and extract any phone numbers it finds associated with these names.


<h2>Notes</h2>
The project is designed to work with Kenyan phone numbers following the pattern 0711111111. You may need to adjust the regular expression in phone_spider.py if you need to work with different formats.
Ensure that the website you are scraping allows web scraping and is not violating any terms of service.

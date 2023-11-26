from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def fetch_and_save_content():
    # Send a GET request to the website
    response = requests.get("https://live.yallashoot.tv/")

    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, "html.parser")

    # Add meta tag for refreshing every 5 seconds
    meta_tag = soup.new_tag("meta", attrs={"http-equiv": "refresh", "content": "5"})
    soup.head.append(meta_tag)

    # Save the modified HTML content to a file
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(str(soup.prettify()))

    # Print a message indicating that the file has been saved
    print("Modified HTML content has been saved to 'index.html'")


@app.route("/")
def index():
    fetch_and_save_content()
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()
    return content


if __name__ == "__main__":
    app.run(debug=True)

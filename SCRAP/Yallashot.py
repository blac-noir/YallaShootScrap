
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import time

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
    with open(
        "C:\\Users\\MOHAMED AMINE\\Documents\\VSCode Projects\\Python\\SCRAP\\templates\\modified_page.html",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(str(soup.prettify()))

    # Print a message indicating that the file has been saved
    print("Modified HTML content has been saved to 'modified_page.html'")


@app.route("/")
def index():
    fetch_and_save_content()
    return render_template("modified_page.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        GitHubUser = request.form['GitHubUser']
        url = 'https://github.com/' + GitHubUser
        r = requests.get(url)
        soup = bs(r.content, 'html.parser')
        
        
        img_tag = soup.find('img')
        if img_tag:
            profileImage = img_tag.get('src')
            return render_template('index.html', profileImage=profileImage)

    return render_template('index.html', profileImage=None)

if __name__ == '__main__':
    app.run(debug=True)
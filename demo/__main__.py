import finnsflask as main
app = main.FinnsFlask()


@app.route('/')
def index(request: main.HTTPRequest):
    html = ""
    cookies = request.getCookies()
    for cookie in cookies:
        cookie_str = ""
        cookie = str(cookies[cookie]).split('Set-Cookie: ')
        for i in range(len(cookie)):
            if i != 0:
                cookie_str += cookie[i]
        html += f'{cookie_str}<br>'
    response = main.HTTPResponse(html)
    response.setCookies('Real Finnventor', 'awesome')
    response.setCookies('Finnventor', 'bad')
    return response


@app.route('/jinja')
def test(request: main.HTTPRequest):
    return main.HTTPResponse.load_template('demo/templates/demo.html', name='Real Finnventor')


if __name__ == "__main__":
    app.listen()

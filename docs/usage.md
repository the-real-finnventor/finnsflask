# Usage

## The base

For a project with no endpoints import the module then create a instance with:

```
app = finnsflask.FinnsFlask()
```

Then start the app with:

```
if __name__ == "__main__":
    app.listen()
```

## Endpoints

To declare an endpoint, between your app declaration and when you start the app, put:

```
@app.route('/<path>')
def index(request: finnsflask.HTTPRequest):
    return finnsflask.HTTPResponse("<h1>Real Finnventor is awesome</h1>", 200)
```

## Templates

finnsflask uses jinja2 as a templating system. To use a jinja2 template, use a route declaration like the following:

```
@app.route("/<path>")
def index(request: finnsflask.HTTPRequest):
    return finnsflask.HTTPResponse.load_template('<path-to-jinja2-template>', <template-args>)
```

## Cookies

To get a cookie, use the following inside of your route declaration:

```
cookies = request.getCookies()
```

To set a cookie, use a route declaration like the following:

```
@app.route("/<path>")
def index(request: finnsflask.HTTPRequest):
    response = finnsflask.HTTPResponse()
    response.setCookie("<key>", "<value>")
    return response
```

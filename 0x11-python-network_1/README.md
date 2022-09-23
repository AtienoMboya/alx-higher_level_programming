* [0-hbtn_status.py](0-hbtn_status.py) - fetches `https://alx-intranet.hbtn.io/status` using `urllib`
* [1-hbtn_header.py](1-hbtn_header.py) - takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response
* [2-post_email.py](2-post_email.py) - takes in a URL and an email, sends a POST request to the passed URL with the email as the parameter and displays the body of the response (decoded in `utf-8`)
* [3-error_code.py](3-error_code.py) - takes in a URL, sends a request to the URL and displays the body f the response (decoded in `utf-8`). Manages `urllib.error.HTTPError` exceptions
* [4-hbtn_status.py](4-hbtn_status.py) - fetches `https://alx-intranet.hbtn.io/status` using the package `requests`
* [5-hbtn_header.py](5-hbtn_header.py) - takes in a URL, sends a request to the URL nad displays the value of `X-Request-Id` in the request header using the packages `requests` and `sys`
* [6-post_email.py](6-post_email.py) - takes in a URL and an email address, sends a POST request to the passed URL with the email as the parameter and finally displays the body of the response
* [7-error_code.py](7-error_code.py)
* [8-json_api.py](8-json_api.py) - taeks in a letter and sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as the parameter
* [10-my_github.py](10-my_github.py) - takes my GitHub credentials and used `Github API` to display my id
* [100-github_commits.py](100-github_commits.py)
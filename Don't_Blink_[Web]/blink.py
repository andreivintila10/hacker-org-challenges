import httplib2

url = "http://www.hacker.org/challenge/misc/one.php"

h = httplib2.Http()
h.follow_redirects = False
(response, body) = h.request(url)
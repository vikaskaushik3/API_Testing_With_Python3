import pytest
import requests


class TestHttpStatusCode:

    _baseurl = "https://jsonplaceholder.typicode.com/posts"

    def test_http_statuscode_201(self):
        response = requests.post(self._baseurl, json={"title": "test"})
        assert response.status_code == 201

    def test_http_statuscode_204(self):
        response = requests.get("https://httpbin.org/status/204")
        assert response.status_code == 204
        assert response.text == ''

    def test_http_statuscode_301(self):
        response = requests.get("http://github.com", allow_redirects=False)
        assert response.status_code == 301

    @pytest.mark.xfail
    def test_http_statuscode_301_negative(self):
        response = requests.get("https://httpbin.org/redirect/1", allow_redirects=False)
        assert response.status_code == 301

    def test_http_statuscode_304(self):
        response = requests.get("https://httpbin.org/cache", headers={"If-None-Match": "some-etag"})
        assert response.status_code in [200, 304]

    def test_http_statuscode_403(self):
        response = requests.get("https://httpbin.org/status/403")
        assert response.status_code == 403

    def test_http_statuscode_402(self):
        response = requests.get("https://httpbin.org/status/402")
        assert response.status_code == 402

    def test_http_statuscode_404(self):
        response = requests.get("https://jsonplaceholder.typicode.com/invalid")
        assert response.status_code == 404

    def test_http_statuscode_500(self):
        response = requests.get("https://httpbin.org/status/500")
        assert response.status_code == 500

    def test_http_statuscode_503(self):
        response = requests.get("https://httpbin.org/status/503")
        assert response.status_code == 503




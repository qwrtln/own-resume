import pytest

from .base import TestResourceBase


@pytest.mark.resource
class TestHello(TestResourceBase):
    def test_get(self):
        rv = self.client.get("/")
        assert rv.status_code == 200
        assert b"Hello, mysterious user!" in rv.data

    def test_get_chrome_on_windows(self):
        rv = self.client.get(
            "/",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
            },
        )
        assert rv.status_code == 200
        assert b"Hello, Chrome 81 on Windows!" in rv.data

    def test_get_safari_on_macos(self):
        rv = self.client.get(
            "/",
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15"
            },
        )
        assert rv.status_code == 200
        assert b"Hello, Safari 12 on Macos!" in rv.data

    def test_get_firefox_on_linux(self):
        rv = self.client.get(
            "/",
            headers={
                "User-Agent": "Mozilla/5.0 (Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"
            },
        )
        assert rv.status_code == 200
        assert b"Hello, Firefox 75 on Linux!" in rv.data

    def test_method_not_allowed(self):
        rv = self.client.post("/", data={"spam": "eggs"})
        assert rv.status_code == 405
        assert b"The method is not allowed for the requested URL." in rv.data

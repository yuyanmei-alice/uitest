
from pages.index_page import IndexPage


class TestIndexPage:

    def setup(self):
        self.index_page = IndexPage()
        self.index_page.start()

    def test_search(self):
        """
        验证首页的搜索功能
        :return:
        """
        self.index_page.search("算法")
        assert self.index_page.ielement_is_exsit("id", 'loginsubmit')

    def teardown(self):
        self.index_page.close()


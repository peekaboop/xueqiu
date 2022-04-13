
import pytest,yaml,allure
from page.APP import APP
@allure.epic('雪球app')
@allure.feature("搜索模块")
class Testsearch():

    @pytest.mark.parametrize("key,expValue",yaml.safe_load(open("../datapool/searchdata.yaml")),ids=["阿里巴巴股价搜索",'京东股价搜索'])
    @allure.story("搜索框搜索词汇")
    def test_search001(self,key,expValue):
        shiji=APP().start().main().go_to_searchpage().search(key).get_price()
        assert float(expValue)>shiji
# if __name__ == '__main__':
#     pytest.main('-s -v')



# 生成测试报告
# ls
# cd xueqiuTestCase
# pytest search_testcase.py - s - q - -alluredir =../ report / result
# allure serve ../report/result
# http://192.168.208.1:61993/index.html
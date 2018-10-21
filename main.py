
from tools.MyRepoter import RunSuite
import HTMLTestRunner

filename = 'D:\\result.html'
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = u'接口测试报告',
    description = u'用例执行情况：')

runner.run(RunSuite())

fp.close()
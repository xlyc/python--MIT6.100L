# Python--MIT6.100L
  感谢MIT(麻省理工学院)对此课程资源的公开与[simviso-知秋](https://www.simtoco.com/#/home)的[中文精翻](https://www.bilibili.com/video/BV1WE421V7bL/?spm_id_from=333.1387.homepage.video_card.click&vd_source=3181deb7fb0c10621dd8dbdf8ab90a04)！

  感谢[csdiy.wiki](https://csdiy.wiki/)的作者[@PKUFlyingPig](https://github.com/PKUFlyingPig)让我发现了这门好课！

  这个repo用来记录MIT6.100L的ppt和problem_sets。
## [课程链接 Course Link](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/material-by-lecture/)
## 本门课的作业均在本地环境运行，Problem Sets则可使用官方提供的py程序进行测试(测试用例全在里面哦！)
## 现已更新至ps3(代码仅能通过测试，注释，代码风格等一概莫得)
## 关于[中文精翻](https://www.bilibili.com/video/BV1WE421V7bL/?spm_id_from=333.1387.homepage.video_card.click&vd_source=3181deb7fb0c10621dd8dbdf8ab90a04)的说明
非常用心的翻译，译者还是计算机领域的大佬！

可以参考[译者的学习路线](https://xw4pe0eed67.feishu.cn/docx/JUlZdTX4io0D3WxJPFfceSP9ngc)学习。
## BUG修改
- 修改ps2中test_ps2_student.py的第465，466行，解决因python版本而无法正常运行程序的bug，如下：
  ```
  test_loader = unittest.TestLoader()
  suite.addTest(test_loader.loadTestsFromTestCase(TestPS2))
  ```

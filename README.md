# gsmis2csv
将北航研究生综合服务平台中的我的课表数据转换为适配WakeUp课程表的csv文件

## 这是什么

这是一个简易的python脚本，用于转换北航研究生综合服务平台中的个人课表数据为适配WakeUp课程表的csv文件。

## 使用方法

以下使用方法在Windows10系统下的edge浏览器中完全适用，其它情况下方法应该也是类似的。

你需要登录北航研究生综合服务平台GSMIS，F12调出调试页面并打开“网络”面板，然后进入我的课表app等待你的课表加载。课表加载完成后选择网络面板下的“loadXskbData.do”请求，点选“预览”，右键复制“jgList”的值。

得到这个值之后，你需要将这段数据复制到这个python脚本开头的json_data里，然后运行这个脚本即可生成output.csv，将其发送至手机上并用WakeUp课程表打开即可。


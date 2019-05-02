## 一个简单的身份证号码获取用户信息工具 python 版
中国（大陆地区）公民身份证，数据来源于国家标准GB/T 2260-2007 [中华人民共和国行政区划代码](http://www.mca.gov.cn/article/sj/xzqh/2018/201804-12/201804-06041553.html)
### 说明
一个基于中华人民共和国公民身份证的组件可以获取用户信息。这个适用于任何python的任何版本。
### 使用
```python
 test = IdentityCard("320106198310290811")
 print test.get_province()
 print test.get_city()
 print test.get_county()
 print test.get_area()
 print test.get_zodiac()
 print test.get_constellation()
 print test.generate_id_card()
 print test.is_id_card(test.generate_id_card())
```
### 返回结果
```python
print test.get_info()
{
    "area":"江苏省 南京市 鼓楼区",
    "province":"江苏省",
    "city":"南京市",
    "county":"鼓楼区",
    "gender":"男",
    "birthday":"1983-10-29",
    "zodiac":"猪",
    "age":"35",
    "constellation":"天蝎座"
}
```
### Api
- get_area():string 获取地区
- get_constellation():string 获取星座
- get_zodiac() : string 获取生肖
- get_age():int 获取年龄
- get_birthday():string 获取生日
- get_gender():string 获取性别
- get_county():string 获取县城
- get_city():string 获取城市
- get_province():string 获取省
- get_info():json 获取全部信息
- is_id_card():boole 身份证号是否合法
- generate_id_card():string 生成身份证号

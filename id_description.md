# identity-card
验证身份证号码的正确性,不能仅仅通过正则表达式来验证，我们都知道我国的身份证一共是18位，由十七位数字本体码和一位校验码组成。
其排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位校验码。
1. 地址码 （身份证号码前六位）;表示编码对象常住户口所在县(市、旗、区)的行政区域划分代码，按GB/T2260的规定执行。1-2位省、自治区、直辖市代码； 3-4位地级市、盟、自治州代码； 5-6位县、县级市、区代码。
2. 出生日期码 （身份证号码第七位到第十四位）;表示编码对象出生的年、月、日，按GB/T7408的规定执行，年、月、日代码之间不用分隔符。
3. 顺序码 （身份证号码第十五位到十七位）;表示在同一地址码所标识的区域范围内，对同年、同月、同日出生的人编定的顺序号，顺序码的奇数分配给男性，偶数分配给女性。
4. 校验码（身份证号码最后一位）;是根据前面十七位数字码，按照ISO 7064:1983.MOD 11-2校验码计算出来的检验码。如果某人的尾号是0-9，都不会出现X，但如果尾号是10，那么就得用X来代替，X是罗马数字的10，用X来代替10，可以保证公民的身份证符合国家标准。

##### 校验码计算步骤

- 十七位数字本体码加权求和公式

　　S = Sum(Ai * Wi), i = 0, … , 16 ，先对前17位数字的权求和
  
　　Ai:表示第i位置上的身份证号码数字值(0~9)
  
　　Wi:7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 （表示第i位置上的加权因子）
  
- 计算模

　　Y = mod(S, 11)

- 根据模，查找得到对应的校验码

　　Y: 0 1 2 3 4 5 6 7 8 9 10
  
　　校验码: 1 0 X 9 8 7 6 5 4 3 2
  
对应的代码校验如下:
```java
public class IdentityCard{
    int[] weight={7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2};    //十七位数字本体码权重
    char[] valid={ '1','0','X','9','8','7','6','5','4','3','2'};    //mod11,对应校验码字符值

    ///card是除去最后一位前17位的号码
    public char getValidateCode(String card){
        int sum=0;
        int mode=0;
        for(int i=0;i<card.length();i++){
            sum=sum+Integer.parseInt(String.valueOf(card.charAt(i)))*weight[i];
        }
        mode=sum%11;
        return valid[mode];
    }
}
```
```python
def get_id_card_verify_number(id_card):
    factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    check_sum = sum([a * b for a, b in zip(factor, [int(a) for a in id_card[0:-1]])])
    return check_code_list[check_sum % 11]
```
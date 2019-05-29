class Solution {
public:
    int myAtoi(string str) {
        if(str.empty())
            return 0;
        int sign = 1, base = 0, i = 0, n = str.size();
        /// 扫描空格
        while(i < n && str[i] == ' ')
            ++i;
        if(i < n && (str[i] == '+' || str[i] == '-'))
        {
            sign = (str[i++] == '+') ? 1 : -1;
        }
        while (i < n && str[i] >= '0' && str[i] <= '9')
        {
            /// 考虑2147483647 / 10的情况如果，最后一位大于7则溢出
            if(base > INT_MAX / 10 || (base == INT_MAX / 10 && str[i] - '0' > 7))
                return (sign == 1) ? INT_MAX : INT_MIN;
            base = 10 * base + (str[i++] - '0');
        }
        return base * sign;
    }
};
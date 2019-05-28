class Solution {
public:
    /// 马拉车算法
    string longestPalindrome(string s) {
        if (s.size() < 2)
            return s;
        
        /// 给字符串插入"#"
        /// 字符串的开头固定为"$#"
        string t = "$#";
        for (int i = 0; i < s.size(); ++i)
        {
            t += s[i];
            t += "#";
        }
        
        /// 处理字符串t
        vector<int> p(t.size(), 0);
        int mx = 0, id = 0, resLen = 0, resMx = 0;
        for(int i = 1; i < t.size(); ++i)
        {
            p[i] = mx > i ? min(p[2 * id - i], mx - i) : 1;
            while (t[i + p[i]] == t[i - p[i]])
                ++p[i];
            if(mx < i + p[i])
            {
                mx = i + p[i];
                id = i;
            }
            if(resMx < p[i])
            {
                resMx = p[i];
                resLen = i;
            }
        }
        return s.substr((resLen - resMx) / 2, resMx - 1);
    }
};
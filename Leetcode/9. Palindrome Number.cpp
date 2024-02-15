class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        int num = x;
        long reversed = 0;
        while (num > 0){
            int lastDigit = num % 10;
            reversed = reversed * 10 + lastDigit;
            num /= 10;
        }
        if (x == reversed){
           return true;
        }
        else {
            return false;
        }
    }

};
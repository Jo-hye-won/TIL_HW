# 기초 수식
 - 연습문제들: 다음 재귀식들을 O() notation 수준으로 풀어라
- 문제 1 : T(n) = T(n-1) + 1, T(0) = 1
                = T(n-2) + 1 + 1
                = T(n-3) + 1 + 1 + 1
                = T(n-k) + k
                = T(0) + n
                = 1 + n
                > O(n)
      
  T(n) = T(n-1) + n,
  

T(n) = T(n/2) + 1, T(1) = 1
     = T(1/2 * n/2) + 1 + 1
     = T(1/2 * n/4) + 1 + 1 + 1
     = T(n/2ⁿ) + n

# 재귀
int abc(int x)
{
 return abc(x)
}

int sum(int x)
{
 if(x <=0) return 0
 return x + sum(x-1);

}

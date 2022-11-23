#include <cstdio>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
using namespace std;

// stack, queue 예제
// int main() {
//     stack<int> s;
//     queue<int> q;
//     for(int i = 0; i < 10; i++) {
//         int t;
//         scanf("%d", &t);
//         s.push(t);
//         q.push(t);
//     }

//     while(!s.empty()) {
//         printf("%d", s.top());
//         s.pop();
//     }

//     printf("\n");
//     while(!q.empty()) {
//         printf("%d", q.front());
//         q.pop();
//     }
//     return 0;
// }

// 1. 화물 배송
// int main() {
//     int n;
//     scanf("%d", &n);
//     stack<int> s;
//     queue<string> q;
//     for(int i = 0; i < n; i++) {
//         int m;
//         string a;
//         scanf("%d", &m);
//         cin >> a;
//         s.push(m);
//         q.push(a);
//     }

//     while(!s.empty()) {
//         printf("%d ", s.top());
//         s.pop();
//     }
//     printf("\n");
//     while(!q.empty()) {
//         cout << q.front();
//         printf(" ");
//         q.pop();
//     }
//     return 0;
// }

// 2. 요세푸스 순열
// int main() {
//     int n, k;
//     scanf("%d %d", &n, &k);
//     queue<int> q;
//     for(int i = 1; i <= n; i++) {
//         q.push(i);
//     }
//     while(!q.empty()) {
//         for(int i = 0; i < k - 1; i++) {
//             q.push(q.front());
//             q.pop();
//         }
//         printf("%d", q.front());
//         q.pop();
//     }
//     return 0;
// }

// 3. 종이컵 마술
// int main() {
//     int n;
//     scanf("%d", &n);
//     stack<int> s;
//     for(int i = 0; i < n; i++) {
//         int size;
//         scanf("%d", &size);
//         while(!s.empty() && s.top() < size) {
//             s.pop();
//         }
//         s.push(size);
//     }
//     printf("%d", s.size());
//     return 0;
// }

// 4. 괄호 검사기
// int main() {
//     char str[100001];
//     stack<char> s;
//     scanf("%s", str);
//     for(int i = 0; str[i]; i++) {
//         if(str[i] == '(' || str[i] == '{' || str[i] == '[')
//             s.push(str[i]);
//         else {
//             if(s.empty()) {
//                 printf("0");
//                 return 0;
//             } else if (s.top() != '(' && str[i] == ')') {
//                 printf("0");
//                 return 0;
//             } else if (s.top() != '{' && str[i] == '}') {
//                 printf("0");
//                 return 0;
//             } else if (s.top() != '[' && str[i] == ']') {
//                 printf("0");
//                 return 0;
//             }
//             s.pop();
//         }
//     }
//     if(s.empty())
//         printf("1");
//     else
//         printf("0");
//     return 0;
// }

// 5. 숫자 만들기 1
// int main() {
//     int a, b;
//     scanf("%d %d", &a, &b);
//     queue<int> q;
//     q.push(a);
//     while(!q.empty()) {
//         int num = q.front();
//         q.pop();
//         if (num == b) {
//             printf("1");
//             return 0;
//         }
//         if (num * 2 <= b) {
//             q.push(num * 2);
//         }
//         if (num * 10 + 1 <= b) {
//             q.push(num * 1- + 1);
//         }
//     }
//     printf("%d", -1);
//     return 0;
// }

// 6. 후위 표기법
// int main() {
//     char str[101];
//     scanf("%s", str);
//     stack<int> s;
//     for(int i = 0; str[i]; i++) {
//         if('0' <= str[i] && str[i] <= '9')
//             s.push(str[i] - '0');
//         else {
//             int a = s.top();
//             s.pop();
//             int b = s.top();
//             s.pop();
//             if(str[i] == '+') {
//                 s.push(b + a);
//             } else {
//                 s.push(b - a);
//             }
//         }
//     }
//     printf("%d", s.top());
//     return 0;
// }
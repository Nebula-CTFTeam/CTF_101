# RE

比赛结束之后网站就关闭了，不知道后来放新题没有，题目名字也可能不准确

## Lucy_Number
看一下 `main` 函数里的 `doSomething` 函数：
```C
unsigned __int64 __fastcall doSomething(unsigned __int64 a1)
{
  unsigned __int64 v3; // [rsp+10h] [rbp-8h]

  v3 = 0LL;
  while ( a1 )
  {
    v3 = 10 * v3 + a1 % 0xA;
    a1 /= 0xAuLL;
  }
  return v3;
}
```
逻辑很简单，就是把输入的数字按十进制倒过来，比如 123 变成 321

之后是 `luckyNumberGen`：
```C
void __fastcall luckyNumberGen(_QWORD *a1)
{
  __int64 v1; // [rsp+8h] [rbp-20h]
  __int64 v2; // [rsp+10h] [rbp-18h]
  unsigned __int64 i; // [rsp+18h] [rbp-10h]
  __int64 v4; // [rsp+20h] [rbp-8h]

  v1 = 0LL;
  v2 = 1LL;
  *a1 = 0LL;
  for ( i = 0LL; i <= 49; ++i )
  {
    *a1 += v1;
    v4 = v1 + v2;
    v1 = v2;
    v2 = v4;
  }
}
```

可以复现或者复制这段得到幸运数字，然后倒过来：
```python
a = 0
b = 1
c = 0
for i in range(50):
    c += a
    d = a + b
    a = b
    b = d

print(f'BDSEC{{{str(c)[::-1]}}}')

# BDSEC{37011056302}
```

# Not_That_Easy
意义不大的题目，flag 藏在 `banner` 函数里：
```C
/* ... */
flag[17] = flag[10];
flag[1] = toupper(*(char *)(a2 + 9));
flag[0] = toupper(*(char *)(a2 + 9));
puts((const char *)a4);
flag[1] = toupper(*(char *)(a2 + 5));
flag[2] = toupper(*(char *)(a4 + 13));
flag[3] = toupper(*(char *)(a2 + 7));
flag[4] = toupper(*(char *)(a6 + 11));
puts(a5);
flag[5] = toupper(*(char *)(a6 + 18));
flag[6] = toupper(*(char *)(a4 + 3));
flag[7] = *(_BYTE *)(a2 + 4);
flag[15] = flag[3];
flag[8] = *(_BYTE *)(a4 + 4);
flag[19] = toupper(*(char *)(a6 + 22));
flag[9] = *(_BYTE *)(a2 + 18);
flag[10] = *(_BYTE *)(a6 + 20);
flag[11] = *(_BYTE *)a2;
flag[17] = flag[9];
flag[12] = *(_BYTE *)(a4 + 8);
flag[16] = *(_BYTE *)(a3 + 4);
flag[13] = *(_BYTE *)(a4 + 13);
flag[14] = flag[10];
flag[1] = toupper(*(char *)(a2 + 13));
flag[18] = *(_BYTE *)(a6 + 6);
/* ... */
```
这里的变量 `flag` 是对 20 个局部变量重新定义得到的，因为它们并没有被使用，所以比较可疑，用调试器跟一下就得到了 flag：`BDSEC{Oops-1tS-EAsy}`，或者根据传参复现这个过程也能得到，`toupper` 函数可以将小写字母转为大写字母，这里的 `a2`~`a6` 传入的是 menu 文本的内容
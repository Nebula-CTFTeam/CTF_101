## 飞机大战

程序生成了 16 bits 的随机种子和 16 位的随机掩码，通过二者乘模确定接下来的随机序列，通过信息知识可以知道，每架飞机每次可以飞四个方向，自信息量为2bits，8架飞机飞一次就可以得到 16 bits 信息，再飞一次就可得到改变后的种子，反解出掩码，之后即可预测飞机所有的走向

预测之后要打还存在一些编程困难，题解提供了手摇版（exp.py, game_patched.py）和自动交互版（solve.py）

## Nebulang

题目看似复杂，其实有明显的循环节，看出逻辑需要一些时间，逻辑大致如下：

```cpp
#include <stdio.h>

unsigned char cipher[] = {
    11, 52, 20, 17, 16, 48, 26, 39, 86, 59, 44, 103, 49, 85, 108, 77, 11, 13, 3, 87, 64, 67, 85, 111, 79, 79, 100, 55, 86, 77, 42, 14, 63, 65, 31, 85, 39, 15, 74, 49, 126, 23, 87, 33, 81, 66, 71, 41, 42, 106, 126, 64, 43
};

unsigned char enc[53] = {0};
char data[53] = {0};

char fake[] = "flag{you are smart but this is not the flag you want}";

void encrypt(char* plaintext, unsigned char* cipher)
{
    for (int i = 0; i < 53; i++)
    {
        cipher[i] = plaintext[i] ^ plaintext[(i+1)%53] ^ plaintext[(i+2)%53] ^ plaintext[(i+3)%53] ^ plaintext[(i+4)%53] ^ plaintext[(i+5)%53] ^ plaintext[(i+6)%53];
        cipher[i] ^= fake[i];
    }
}

int main()
{
    scanf("%s", data);
    encrypt(data, enc);
    for (int i = 0; i < 53; i++)
    {
        if (enc[i] != cipher[i])
        {
            puts("Wrong...\n");
            return 0;
        }
    }
    puts("Right!\n");
    return 0;
}
```

解法上我这里取巧了，已知最后一位一定是反花括号（ASCII 125），所以根据它来推：

```python
cipher = [11, 52, 20, 17, 16, 48, 26, 39, 86, 59, 44, 103, 49, 85, 108, 77, 11, 13, 3, 87, 64, 67, 85, 111, 79, 79, 100, 55, 86, 77, 42, 14, 63, 65, 31, 85, 39, 15, 74, 49, 126, 23, 87, 33, 81, 66, 71, 41, 42, 106, 126, 64, 43]
fake = b"flag{you are smart but this is not the flag you want}"

for i in range(53): cipher[i] ^= fake[i]

flag = [0] * 53
flag[52] = 125

i = 6
while 1:
    flag[i % 53] = flag[(i - 7) % 53] ^ cipher[(i - 7) % 53] ^ cipher[(i - 6) % 53]
    i += 7
    if not 0 in flag:
        flag = [chr(i) for i in flag]
        print(''.join(flag))
        break

# NebuCTF{Hahaha_de4r_Fr1end_D0_YoU_l1k3_0Ur_N3bu14ng6}
```

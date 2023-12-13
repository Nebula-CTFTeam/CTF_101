## White Hat

本题出题的核心思路为白盒 AES 的破解。

### level 0

了解分组密码的 CTR 模式即可，或者直接读代码也可以发现，用加密函数再加密一遍密文就得到明文了：

```cpp
#include <stdio.h>

#include "encryptor.h"

const uint8_t nonce[16] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

uint8_t input[48] = {
    16, 78, 21, 160, 73, 95, 86, 0, 231, 78, 7, 57, 42, 191, 65, 192, 51, 176, 162, 229, 69, 203, 184, 239, 3, 228, 211, 213, 197, 4, 62, 228, 234, 121, 233, 149, 31, 147, 200, 160, 39, 176, 122, 44, 180, 27, 212, 155
};
uint8_t cipher[48] = {0};

int main() {
    // scanf("%48s", input);
    // encrypt_ctr(nonce, input, 48, cipher);
    // for (int i = 0; i < 48; i++)
    //     printf("%d, ", cipher[i]);
    encrypt_ctr(nonce, input, 48, cipher);
    for (int i = 0; i < 48; i++)
        printf("%c", cipher[i]);
    return 0;
}

//output: 104e15a0495f5600e74e07392abf41c033b0a2e545cbb8ef03e4d3d5c5043ee4ea79e9951f93c8a027b07a2cb41bd49b

//flag: NebuCTF{1111_AES_1s_an_imp0rt4nt_3ncrypt_m3th0d}
```

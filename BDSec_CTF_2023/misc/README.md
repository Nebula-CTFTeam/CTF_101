# Misc

都是入门题，感觉非常友好（分值也都不高），Forensics 和 Osint 比较烦，所以没看（逃

## Think Like a Hacker

一个视频看完一遍没什么异样，用 010editor 打开，拉到最下面发现文件尾后面有可疑信息。

```
"Hacking is not about breaking into something; it's about bending reality." - Frank Abagnale.OQFRP{.OQFrp_.PGS_.2023_.Ce0z0_.I1Q30_.sY4T}."The best way to predict the future is to create it." - Peter Drucker."Hacking involves a different way of looking at problems that no one's thought of." - Walter O'Brien.
```

中间的 `OQFRP{.OQFrp_.PGS_.2023_.Ce0z0_.I1Q30_.sY4T}` 看起来就像是 `flag` 经过某种变换来的 (注：这里的 `.` 并非句号而是不可打印字符，16 进制字符为 `0A` ，实际复制粘贴得到的应该是换行符号) ，看格式以及数字没有改变猜测是 `ROT13` 一类的代换，一试还真是，得到 `flag` 为 `BDSEC{BDSec_CTF_2023_Pr0m0_V1D30_fL4G}` 

## What is this ?

解压后打开文件夹里有大量文件，用 010editor 打开 `flag_aa` 看一眼会发现标准的 `PNG` 文件头

```
.PNG........IHDR.......8.....g.V.....sRGB...,.....pHYs...a...a..?.i....IDATx(后面略)
```

合理猜测题目将一个 `PNG` 文件拆成了字母序命名的若干文件，写脚本恢复即可，恢复后 `flag` 直接写在了图片里，得到 `flag` 为 `BDSEC{1tS_@_PnG_f1LE_}`

*脚本与图片均在 `misc_wp` 文件夹中
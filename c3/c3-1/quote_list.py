# Created by RitsukiShuto on 2019/03/20.
# Python TextBook Chapter c3-1 "list-kakugen.py"
#
import random

# 格言をリストに格納
quotes = [
    "能ある鷹は爪を隠す",
    "豚に真珠",
    "二兎を追う者は一兎をも得ず",
    "叩き続けなさい。そうすれば開かれます。"
]

# ランダムにひとつ選ぶ
i = random.randint(0, len(quotes)-1)
# 選んだ格言を表示
print(quotes[i])

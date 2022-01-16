# 解説（書きかけ）
ここら辺から章末問題に骨のある問題が登場してきます。
詳しい説明は[著者本人によるもの](https://github.com/hiro-mori999/Drken_book_Python/blob/master/solutions/chap04.md)に任せて、
ここでは実装上のテクニックについて補足します。

## 4.5
関数SFTのコードは次の通りです。
```python:code1
def SFT(N,cur,use):
    if cur>N: return 
    
    if use==7:
        Answer.add(cur)
    sft=[3,5,7]
    for i in range(3):
        SFT(N,cur*10+sft[i],use|(1<<i))

    return 
```
ここでの処理は、
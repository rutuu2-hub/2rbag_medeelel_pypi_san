# 2-r bagiin san

Pandas хүснэгт дээр статистик тооцоолж, өгөгдлийн чанарыг
шалгаж, сонгосон дүрмээр цэвэрлэх Python сан.

## Функцууд

- `medeelel(df)`-үндсэн статистик гаргана.
- `sus(df)`=missing, давхардал, IQR outlier, корреляцыг шалгана.
- `tseverleh(df, davhardal=False, nuhuh=None, hasah=None)` —
  эх өгөгдлийн хуулбарыг сонгосон дүрмээр цэвэрлэж буцаана.

## Ашиглах жишээ

```python
import pandas as pd
import medeelel_tools as mt

df = pd.DataFrame({"nas": [20, 25, 30]})
print(mt.medeelel(df))
```
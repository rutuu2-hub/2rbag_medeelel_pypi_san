# 2-р багийн EDA сан

Өгөгдлийн статистик гаргах, чанарыг шалгах, цэвэрлэх Python сан.

## Суулгах

```bash
pip install 2r-bag-medeelel-tools
```

## Ашиглах

```python
import pandas as pd
import medeelel_tools as mt

df = pd.DataFrame({
    "nas": [20, 20, 30, None],
    "tsalin": [1000000, 1000000, None, 2000000]
})
```

### 1. medeelel(df)

Count, mean, std, min, max, квартиль болон median (`50%`) гаргана.

```python
print(mt.medeelel(df))
```

### 2. sus(df)

Missing утгын тоо/хувь, давхардсан мөрийн тоо, IQR outlier-ийн тоо болон корреляцыг гаргана.

```python
hariu = mt.sus(df)

print(hariu["missing"])
print(hariu["davhardsan"])
print(hariu["outlier"])
print(hariu["correlation"])
```

### 3. tseverleh(df, ...)

Эх өгөгдлийг өөрчлөхгүйгээр хуулбар дээр цэвэрлэгээ хийнэ.

```python
clean_df = mt.tseverleh(
    df,
    davhardal=True,
    nuhuh={"tsalin": 1500000},
    hasah=["nas"]
)

print(clean_df)
```

Энэ жишээнд давхардлыг арилгаж, дутуу цалинг 1500000-аар нөхөж,
нас нь хоосон мөрийг хасна. Outlier-ийг автоматаар устгахгүй.

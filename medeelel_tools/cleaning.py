import pandas as pd

def sus(df):
    missing = pd.DataFrame({
        "too": df.isna().sum(),
        "huvi": df.isna().mean() * 100
    })

    davhardsan = df.duplicated().sum()

    toon_baganuud = df.select_dtypes(include="number")

    q1 = toon_baganuud.quantile(0.25)
    q3 = toon_baganuud.quantile(0.75)
    iqr = q3 - q1

    dood = q1 - 1.5 * iqr
    deed = q3 + 1.5 * iqr

    outlier_mask = (toon_baganuud < dood) | (toon_baganuud > deed)
    outlier_too = outlier_mask.sum()

    correlation = toon_baganuud.corr()

    return{
        "missing": missing,
        "davhardsan": davhardsan,
        "outlier": outlier_too,
        "correlation": correlation

    }

def tseverleh(df, davhardal=False, nuhuh=None, hasah=None):
    clean = df.copy()

    if davhardal:
        clean = clean.drop_duplicates()
    
    if nuhuh is not None:
        clean =clean.fillna(nuhuh)
    
    if hasah is not None:
        clean = clean.dropna(subset=hasah)

    return clean
    
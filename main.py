import pandas as pd
import medeelel_tools as mt

#df = pd.DataFrame({
#    "nas": [20, 25, 30, 35, 40],
#    "tsalin": [1000000, 1500000, 2000000, 2500000, 3000000]
#})

#print(mt.medeelel(df))
#print(mt.sus(df))

#hariu = mt.sus(df)

#print("Missing utga:")
#print(hariu["missing"])

#print("\nduplicated mur:")
#print(hariu["davhardsan"])

#print("\nOutlier:")
#print(hariu["outlier"])

#print("\ncorrelation")
#print(hariu["correlation"])


test_df = pd.DataFrame({
    "nas": [20, 20, 30, None],
    "tsalin": [1000000, 1000000, None, 2000000]
})

clean_df = mt.tseverleh(
    test_df,
    davhardal=True,
    nuhuh={"tsalin": 1500000},
    hasah=["nas"]
)

print("Эх өгөгдөл:")
print(test_df)

print("\nЦэвэрлэсэн өгөгдөл:")
print(clean_df)
sales_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# بيانات مبيعات وهمية بسيطة
data = {
    'الشهر': ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو'],
    'المبيعات': [200, 350, 400, 300, 550],
    'المنتج': ['أ', 'ب', 'أ', 'ج', 'ب']
}

df = pd.DataFrame(data)

print("أول 5 صفوف من البيانات:")
print(df.head())

# رسم بياني بسيط
df.groupby('المنتج')['المبيعات'].sum().plot(kind='bar', title='المبيعات حسب المنتج')
plt.xlabel('المنتج')
plt.ylabel('إجمالي المبيعات')
plt.show()

# رؤية بسيطة
top_product = df.groupby('المنتج')['المبيعات'].sum().idxmax()
print(f"المنتج الأكثر مبيعًا: {top_product}")

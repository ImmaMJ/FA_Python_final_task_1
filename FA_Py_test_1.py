import pandas as pd

# Загрузка данных
df = pd.read_csv('movies_stats.csv')

# Создание списка годов с 1950 по 2010
years = list(range(1950, 2011))

# Функция для определения года выпуска из названия
def production_year(title):
    for year in years:
        if str(year) in title:
            return year
    return 1900

# Добавление нового столбца с годом выпуска
df['year'] = df['title'].apply(production_year)

# Расчет среднего рейтинга по годам и сортировка
average_ratings = df.groupby('year')['rating'].mean().sort_values(ascending=False)

print(average_ratings)
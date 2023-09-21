### Python 3.10.11

_load data_

```sqlite

.headers ON -- turn on column headers when displaying SELECT results
.mode csv

.import ../foodstats-analysis/data/cleaned_food_category.csv foodstats_api_foodcategory
select * from foodstats_api_foodcategory;
.schema foodstats_api_foodcategory -- verify columns match data (NOTE: no semicolon)

.import ../foodstats-analysis/data/cleaned_foundation_food.csv foodstats_api_food
select count(*) from foodstats_api_food;
.schema foodstats_api_food -- verify columns match data (NOTE: no semicolon)

.tables -- verify no tables were mistakenly created
```

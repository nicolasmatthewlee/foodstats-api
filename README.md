### Python 3.10.11

### deployment instructions

1. clone repository on virtual machine
2. in `settings.py` set `DEBUG=FALSE`
3. kill gunicorn process

```shell
pkill gunicorn
```

3. start virtual environment

```shell
source env/bin/activate
```

4. navigate to project root directory

5. restart gunicorn process

```shell
gunicorn -D foodstats_api.wsgi:application
```

---

```sql
/* commands for loading database */

.headers ON -- turn on column headers when displaying SELECT results
.mode csv

/* food categories */
.import ../foodstats-analysis/data/cleaned_food_category.csv foodstats_api_foodcategory
select * from foodstats_api_foodcategory;
.schema foodstats_api_foodcategory -- verify columns match data (NOTE: no semicolon)

/* nutrient categories */
.import ../foodstats-analysis/data/nutrient_category.csv foodstats_api_nutrientcategory
select * from foodstats_api_nutrientcategory;
.schema foodstats_api_nutrientcategory  -- verify columns match data (NOTE: no semicolon)

/* foods */
.import ../foodstats-analysis/data/cleaned_foundation_food.csv foodstats_api_food
select count(*) from foodstats_api_food;
.schema foodstats_api_food -- verify columns match data (NOTE: no semicolon)

/* nutrients */
.import ../foodstats-analysis/data/cleaned_nutrient_with_category.csv foodstats_api_nutrient
select * from foodstats_api_nutrient;

/* food nutrients (instances that correspond to the value of a nutrient for a specific food) */
.import ../foodstats-analysis/data/cleaned_food_nutrient.csv temp_foodnutrient -- import into temp table
/* .csv files only contain text values, must convert to NULL once imported */
update temp_foodnutrient set min=NULL where min="";
update temp_foodnutrient set max=NULL where max="";
update temp_foodnutrient set median=NULL where median="";
update temp_foodnutrient set min_year_acqured=NULL where min_year_acqured="";

/* .csv files only contain text values, must manually cast all fields */
insert into foodstats_api_foodnutrient (id,food_id,nutrient_id,amount,data_points,derivation_id,min,max,median,footnote,min_year_acquired)
select
    id,
    fdc_id,
    nutrient_id,
    cast(amount as real),
    cast(data_points as int),
    cast(derivation_id as int),
    coalesce(cast(min as real),null),
    coalesce(cast(max as real),null),
    coalesce(cast(median as real),null),
    footnote,
    coalesce(cast(min_year_acqured as int),null)
from temp_foodnutrient; -- move into actual table with column names

drop table temp_foodnutrient; -- drop temp table

.tables -- verify no tables were mistakenly created
```

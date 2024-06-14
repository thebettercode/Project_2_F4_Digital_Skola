# learn_dbt



## How to run it?

create a virtual env of python first :
```
python3 -m venv <your directory>, exp : /Users/farhanpratama/venv_dskola
source <your directory>, exp : /Users/farhanpratama/venv_dskola/bin/activate
```
1. build the python image
```
docker build -t {postgres_image_name} -f Dockerfile.postgres .
docker build -t python_script -f Dockerfile.python .
```
2. run python container
if you want to check the result on local (uncomment first the EXPOSE command on dockerfile postgres)
```
docker run --name {postgres_container_name} {postgres_image_name}
docker run --name python python_script
```
3. export file csv to sql
```
docker cp python:/usr/src/insertData.sql .
```
4. build the postgres image
```
docker build -t {postgres_image_name} -f Dockerfile.postgres .
docker build -t postgres_script -f Dockerfile.postgres .
```
5. run postgres container
if you want to check the result on local (uncomment first the EXPOSE command on dockerfile postgres)
```
docker run -d -p 5432:5432 --name {postgres_container_name} {postgres_image_name}
docker run -d -p 5432:5432 --name postgres postgres_script
```
6. debug your dbt connection
```
dbt debug --profiles-dir ./ --project-dir dbt_dskola_project
```
7. run dbt model
```
dbt run --profiles-dir ./ --project-dir dbt_dskola_project
```
8. generate dbt docs
```
dbt docs generate --profiles-dir ./ --project-dir dbt_dskola_project
```
9. serve dbt docs
```
dbt docs serve --profiles-dir ./ --project-dir dbt_dskola_project
```
   











# Django Template

*2020.07, Yeong-Jo, Pak*



## 0. Usage

- setup
  - gitignore file
  - Requiremenst file
  - flake8
  - pre-commit
  - docker-compose (*progresQL*)
  - settings for multie environments (*base, local, dev, prod*)
  - django-debug-toolbar
  - aws secret manager
  - CommonModelFieldMixIn
  - django extensions
  - django-passwords
  - setup.cfg
  - purest





## 1. For local enviroment

### 1. Setup virtualenv

```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements/local.txt
pre-commit install (***OPTIONAL***)
```



### 2. Create Database

1. install Docker and Container build

   1. install docker

      https://www.docker.com/

   2. run `docker-compose up -d`

2. create database

   ```
   psql -U postgres
   create database {DATABASE_NAME}
   ```

   > postgres 기본 명령어
   >
   > \l database 보기
   >
   > \c database 선택
   >
   > \q postgres 종료



## 99. References

https://docs.djangoproject.com/en/3.0/

https://pre-commit.com/

https://pypi.org/project/flake8/

https://pypi.org/project/psycopg2/

https://pypi.org/project/django-debug-toolbar/

https://pypi.org/project/django-extensions/

https://pypi.org/project/django-passwords/

https://pypi.org/project/boto3/

https://pypi.org/project/pytest/

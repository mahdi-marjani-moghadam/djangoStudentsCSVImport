# djangoStudentsCSVImport
پروژه ساده برای موارد زیر در فریم ورک جنگو

۱- آپلود گروهی اطلاعات دانش آموزان

۲- درست کردن api

۳- گزارش تعداد دانش آموزانی که سن پردشان بالای ۶۰ سال باشد

۴- گزارش دانش آموزانی که سن پدرشان بالای ۵۰ باشد. (توسط api)


## ویژگی های پروژه
۱- استفاده از generic

۲- اتصال به دیتابیس mysql

۳- جداسازی اپ students از parent

۴- جدا سازی قسمت api داخل هر اپ

۵- نوشتن تست ساده برای مدل parents

۶- اضافه کردن url در serialize

۷- اپلود اطلاعات دانش اموزان از طریق فایل csv

# طریقه اجرا
ابتدا کدها را گرفته

۱- virtual env خود را ایجاد کرده

۲- دستور 

``` pip install -r requirements.txt ```

۳- دیتابیس به نام django ساخته

۴- 

``` python3 manage.py makemigrations ```

``` python3 manage.py migrate ```


۶- ساخت کاربر سوپر ادمین

۷- 

``` python3 manage.py runserver 127.0.0.1:8000```

# مسیر های پروژه بعد از اجرا
## Front
- ```127.0.0.1:8000/```
- ```127.0.0.1:8000/students```

## Admin
- ```127.0.0.1:8000/admin```

## Api
### students
- ```127.0.0.1:8000/api/v1/students``` -> Student list
- ```127.0.0.1:8000/api/v1/students/1``` -> detail students
- ```127.0.0.1:8000/api/v1/students/report/50``` -> Json list of students where parent age grreate than 50
### parents
- ```127.0.0.1:8000/api/v1/parents```
- ```127.0.0.1:8000/api/v1/parents/1```


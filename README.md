# FootballClubManager

Tạo môi trường ảo
```bash
# window and linux
python3 -m venv myvenv
```

Active môi trường ảo
```bash
# windowm
.venv\Scripts\activate
# linux, macosvenv\Scripts\activate
source myvenv/bin/activate
``` 

Cài đặt các package cần thiết:
```bash
pip install -r requirements.txt
```

Migrate database
```bash
python manage.py migrate
```

Tạo superuser
```bash
python manage.py createsuperuser
```

Chạy server
```bash
python manage.py runserver
```
Kết nối database sqlite với PyCharm Pro
Mở cửa sổ Database(góc phải trên) -> Add -> Data Source -> SQLite -> Chọn file tới file db.sqlite3 của project

Tương tác với database

Thêm, sửa models trong các file models.py: https://docs.djangoproject.com/en/5.1/topics/db/models/
```python
from django.db import models

class DoiBong(models.Model):
    ma_doi_bong = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    san_van_dong = models.CharField(max_length=100)
    nam_thanh_lap = models.IntegerField()

    class Meta:
        db_table = 'DoiBong'
```

Sau khi thêm sửa models thì tạo file migrations
```bash
python manage.py makemigrations
```

Sau đó apply thay đổi vào database
```bash
python manage.py migrate
```

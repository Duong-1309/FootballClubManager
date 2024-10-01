# FootballClubManager

Tạo môi trường ảo
```bash
# window and linux
python3 -m venv myvenv
```

Active môi trường ảo
```bash
# window
myvenv\Scripts\activate
# linux, macos
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
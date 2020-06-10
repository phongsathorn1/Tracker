# Tracker
## set Up
  1) ลง lib ใน requiments.txt
  2) run `python manage.py makemigrations`
  3) run `python manage.py migrate`
  4) run `python manage.py createsuperuser` แล้วก็สร้าง user
  5) run `python manage.py runserver`
  6) เข้าไปที่ sheet จะมีให้ import csv หรือ excel บลาๆ เข้าไปได้
  
## การใช้
  ยิง api get ใช้ param เป็น query เช่น http://127.0.0.1:8000/sheet/?query=สวัสดี

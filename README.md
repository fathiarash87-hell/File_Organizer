# مرتب‌کننده خودکار فایل‌ها

یک اسکریپت ساده پایتون که فایل‌های یک پوشه (مثل Downloads) را بر اساس نوع، در پوشه‌های جدا مرتب می‌کند.

## دسته‌ها

- **Images**: jpg، jpeg، png، gif
- **Documents**: pdf، docx، txt
- **Excel**: xlsx، xls، csv
- **Videos**: mp4، mkv
- **Others**: هر پسوند دیگر

اگر فایلی با اسم تکراری وجود داشته باشد، اسم فایل جدید با شماره ادامه پیدا می‌کند (مثلاً `photo_1.jpg`) و چیزی بازنویسی نمی‌شود.

## نیازمندی‌ها

- Python 3.8 یا بالاتر
- نیازی به نصب کتابخانه‌ی اضافه نیست

## نحوه اجرا

اول با حالت تست اجرا کنید (فقط نشان می‌دهد چه می‌شود، چیزی جابه‌جا نمی‌شود):

```
python organizer.py "C:\Users\YourName\Downloads" --dry-run
```

اگر خروجی درست بود، اجرای واقعی:

```
python organizer.py "C:\Users\YourName\Downloads"
```

## مثال

قبل از اجرا:

```
Downloads/
├── photo.jpg
├── report.pdf
└── data.xlsx
```

بعد از اجرا:

```
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
└── Excel/
    └── data.xlsx
```

## نکته

فایل `organizer.py` را داخل پوشه‌ای که می‌خواهید مرتب شود نگذارید، وگرنه خودش هم جابه‌جا می‌شود.
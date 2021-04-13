from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = [
    ('トヨタ','TOYOTA'),
    ('レクサス','LEXUS'),
    ('日産','NISSAN'),
    ('ホンダ','HONDA'),
    ('スバル','SUBARU'),
    ('三菱','MITSUBISHI'),
    ('マツダ','MAZDA'),
    ('スズキ','SUZUKI'),
    ('ダイハツ','DAIHATSU'),
    ('光岡','MITSUOKA'),
    ('いすゞ','ISUZU'),
    ]
    name = models.CharField(max_length=100,primary_key=True,choices=name,)

    class Meta:
        db_table="manufacturer"

    pass
    def __str__(self):
        return (self.name)

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE,)
    #car_name = models.CharField(max_length=30, primary_key=True)

    # ...

    #画像を扱う
    picture = models.ImageField(upload_to='images/')
    vehicle_model = models.CharField('車両型式',max_length=200)

    def __str__(self):
        return self.title

    car_name = models.CharField('車名',max_length=60,)

    car_menu = [
        ('SP', 'Sports'),
        ('SUV', 'SUV'),
        ('SD', "Sedan"),
        ('TR', "Trucks"),
        ('SW', "StationWagon"),
    ]
    car_menu = models.CharField('タイプ',max_length=3, choices=car_menu,)

    drive_system = [
        ('オートマ','AT・CVT'),
        ('マニュアル','MT'),
    ]
    drive_system = models.CharField('タイプ',max_length=6, choices=drive_system,)

    car_drive = [
        ('前輪駆動','FF'),
        ('後輪駆動','FR'),
        ('4輪駆動','4WD'),
        ('ミッドシップ','MR'),
        ]
    car_drive = models.CharField('駆動方式',max_length=6, choices=car_drive,)

    odometer1 = models.CharField('走行距離',max_length=7,)

    odometer2 = [
    ('50,000_or_less','5万キロ未満'),
    ('over_50,000','5万キロ以上'),
    ('over_100,000','10万キロ以上'),
    ]
    odometer2 = models.CharField('走行距離',max_length=14, choices=odometer2,)

    car_repaired = [
        ('yes','修復歴有り'),
        ('no','修復歴無し'),
    ]
    car_repaired = models.CharField('修復歴',max_length=5, choices=car_repaired,)

    color = [
    ('Red','レッド'),
    ('Bleu','ブルー'),
    ('White','ホワイト'),
    ('Black','ブラック'),
    ('Yellow','イエロー'),
    ('Green','グリーン'),
    ('Decorated car','痛車'),
    ]
    color = models.CharField('車の色',max_length=15, choices=color,)


    kanto = [
    ('Kanagawa','神奈川県'),
    ('Tokyo','東京都'),
    ('Saitama','埼玉県'),
    ('Chiba','千葉県'),
    ('Gunma','群馬県'),
    ('Ibaraki','茨城県'),
    ]
    kanto = models.CharField('関東地方',max_length=10, choices=kanto,)
    city = models.CharField('市',max_length=60,)
    area = models.CharField('区・町・村',max_length=60,)


    def __str__(self):
        return self.car_name

class Register(models.Model):



    shop1 = models.CharField(max_length=30, primary_key=True)




INSTALLED_APPS = [

    'myapp',

    ]

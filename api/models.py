from django.db import models

# Create your models here.
class TranSum(models.Model):
    TYPE=(
        ('Shares','Shares'),
        ('Mutual Funds','Mutual Funds'),
        ('Futures & Options','Futures & Options'),
        ('Day Trading','Day Trading'),
        ('Trading','Trading')
    )
    FY=(
        ('2010-2011','2010-2011'),
        ('2011-2012','2011-2012'),
        ('2012-2013','2012-2013'),
        ('2013-2014','2013-2014'),
        ('2014-2015','2014-2015'),
        ('2015-2016','2015-2016'),
        ('2016-2017','2016-2017'),
        ('2017-2018','2017-2018'),
        ('2018-2019','2018-2019'),
        ('2019-2020','2019-2020'),
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'),
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),
        ('2025-2026','2025-2026'),
        ('2026-2027','2026-2027'),
        ('2027-2028','2027-2028'),
        ('2028-2029','2028-2029')
    )
    OPTION=(
        ('O','O'),
        ('A','A'),
        ('S','S')
    )
    customerId=models.IntegerField('CustomerId')
    memberId=models.IntegerField('Member_Id')
    fy=models.CharField('FY',max_length=50,choices=FY)
    type=models.CharField('Type',max_length=30,choices=TYPE)
    option=models.CharField(max_length=20,choices=OPTION)
    scriptId=models.CharField(max_length=200)
    script=models.CharField(max_length=300)
    purchaseDate=models.DateField('PurchaseDate')
    quantity=models.IntegerField('Quantity')
    rate=models.DecimalField('Rate',max_digits=300,decimal_places=2)
    value=models.DecimalField('Value',max_digits=1000,decimal_places=2)
    stt=models.DecimalField('STT',max_digits=1000,decimal_places=2,blank=True,null=True)
    other=models.DecimalField('Oth',max_digits=1000,decimal_places=2,blank=True,null=True)
    note=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return str(self.customerId)

     


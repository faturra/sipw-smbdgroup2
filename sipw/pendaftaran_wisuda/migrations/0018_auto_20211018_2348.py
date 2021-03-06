# Generated by Django 3.2.8 on 2021-10-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran_wisuda', '0017_auto_20211018_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akademik',
            name='jenis_kelamin',
            field=models.CharField(blank=True, choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='jadwal_wisuda',
            name='gelombang',
            field=models.CharField(choices=[('Pertama', 'Pertama'), ('Kedua', 'Kedua')], default='Pertama', max_length=150),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='kelas',
            field=models.CharField(choices=[('B', 'B'), ('A', 'A')], default='A', max_length=10),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='ukuran_toga',
            field=models.CharField(choices=[('S', 'S'), ('XL', 'XL'), ('M', 'M'), ('XXL', 'XXL'), ('L', 'L')], default='L', max_length=150),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='yn',
            field=models.CharField(blank=True, choices=[('Yakin, lanjutkan', 'Yakin, lanjutkan')], max_length=100, null=True),
        ),
    ]

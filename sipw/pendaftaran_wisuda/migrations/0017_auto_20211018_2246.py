# Generated by Django 3.2.8 on 2021-10-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran_wisuda', '0016_auto_20211018_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendaftaran_wisuda',
            name='yn',
            field=models.CharField(blank=True, choices=[('Yakin, Lanjutkan', 'Yakin, Lanjutkan')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jadwal_wisuda',
            name='gelombang',
            field=models.CharField(choices=[('Kedua', 'Kedua'), ('Pertama', 'Pertama')], default='Pertama', max_length=150),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='kelas',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A', max_length=10),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='status_approval',
            field=models.CharField(choices=[('Tidak Disetujui', 'Tidak Disetujui'), ('Disetujui', 'Disetujui'), ('Belum Disetujui', 'Belum Disetujui')], default='Belum Disetujui', max_length=150),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='ukuran_toga',
            field=models.CharField(choices=[('S', 'S'), ('L', 'L'), ('M', 'M'), ('XL', 'XL'), ('XXL', 'XXL')], default='L', max_length=150),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran_wisuda', '0018_auto_20211018_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jadwal_wisuda',
            name='gelombang',
        ),
        migrations.AddField(
            model_name='jadwal_wisuda',
            name='pelaksanaan',
            field=models.CharField(choices=[('Utama', 'Utama'), ('Geladi Bersih', 'Geladi Bersih')], default='Geladi Bersih', max_length=150),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='status_keaktifan',
            field=models.CharField(choices=[('Aktif', 'Aktif'), ('Non-Aktif', 'Non-Aktif')], default='Aktif', max_length=150),
        ),
        migrations.AlterField(
            model_name='informasi_publik',
            name='visibilitas',
            field=models.CharField(choices=[('Hanya Staf', 'Hanya Staf'), ('Publik', 'Publik')], default='Hanya Staf', max_length=150),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='status_keaktifan',
            field=models.CharField(choices=[('Aktif', 'Aktif'), ('Non-Aktif', 'Non-Aktif')], default='Aktif', max_length=150),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='status_approval',
            field=models.CharField(choices=[('Belum Disetujui', 'Belum Disetujui'), ('Tidak Disetujui', 'Tidak Disetujui'), ('Disetujui', 'Disetujui')], default='Belum Disetujui', max_length=150),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='ukuran_toga',
            field=models.CharField(choices=[('XL', 'XL'), ('M', 'M'), ('S', 'S'), ('XXL', 'XXL'), ('L', 'L')], default='L', max_length=150),
        ),
    ]

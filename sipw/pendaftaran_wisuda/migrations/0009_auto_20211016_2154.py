# Generated by Django 3.2.8 on 2021-10-16 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran_wisuda', '0008_auto_20211016_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akademik',
            name='status_keaktifan',
            field=models.CharField(choices=[('Non-Aktif', 'Non-Aktif'), ('Aktif', 'Aktif')], default='Aktif', max_length=150),
        ),
        migrations.AlterField(
            model_name='informasi_publik',
            name='visibilitas',
            field=models.CharField(choices=[('Publik', 'Publik'), ('Hanya Staf', 'Hanya Staf')], default='Hanya Staf', max_length=150),
        ),
        migrations.AlterField(
            model_name='jadwal_wisuda',
            name='gelombang',
            field=models.CharField(choices=[('Pertama', 'Pertama'), ('Kedua', 'Kedua')], default='Pertama', max_length=150),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='jenis_kelamin',
            field=models.CharField(blank=True, choices=[('Laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='status_keaktifan',
            field=models.CharField(choices=[('Non-Aktif', 'Non-Aktif'), ('Aktif', 'Aktif')], default='Aktif', max_length=150),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='id_mahasiswa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pendaftaran_wisuda.mahasiswa'),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='ukuran_toga',
            field=models.CharField(choices=[('S', 'S'), ('L', 'L'), ('XXL', 'XXL'), ('M', 'M'), ('XL', 'XL')], default='L', max_length=150),
        ),
    ]

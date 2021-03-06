# Generated by Django 3.2.8 on 2021-10-20 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran_wisuda', '0020_auto_20211020_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='jenis_kelamin',
            field=models.CharField(blank=True, choices=[('Laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='id_jadwal_wisuda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pendaftaran_wisuda.jadwal_wisuda'),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='status_approval',
            field=models.CharField(choices=[('Belum Disetujui', 'Belum Disetujui'), ('Disetujui', 'Disetujui'), ('Tidak Disetujui', 'Tidak Disetujui')], default='Belum Disetujui', max_length=150),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='ukuran_toga',
            field=models.CharField(choices=[('L', 'L'), ('XXL', 'XXL'), ('S', 'S'), ('M', 'M'), ('XL', 'XL')], default='L', max_length=150),
        ),
    ]

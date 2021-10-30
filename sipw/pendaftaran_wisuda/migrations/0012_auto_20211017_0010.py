# Generated by Django 3.2.8 on 2021-10-16 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran_wisuda', '0011_auto_20211016_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fakultas',
            fields=[
                ('id_fakultas', models.AutoField(primary_key=True, serialize=False)),
                ('nama_fakultas', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='informasi_publik',
            name='visibilitas',
            field=models.CharField(choices=[('Publik', 'Publik'), ('Hanya Staf', 'Hanya Staf')], default='Hanya Staf', max_length=150),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='jenis_kelamin',
            field=models.CharField(blank=True, choices=[('Laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='id_mahasiswa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pendaftaran_wisuda.mahasiswa'),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='status_approval',
            field=models.CharField(choices=[('Disetujui', 'Disetujui'), ('Tidak Disetujui', 'Tidak Disetujui'), ('Belum Disetujui', 'Belum Disetujui')], default='Belum Disetujui', max_length=150),
        ),
        migrations.AlterField(
            model_name='pendaftaran_wisuda',
            name='ukuran_toga',
            field=models.CharField(choices=[('S', 'S'), ('L', 'L'), ('M', 'M'), ('XXL', 'XXL'), ('XL', 'XL')], default='L', max_length=150),
        ),
    ]

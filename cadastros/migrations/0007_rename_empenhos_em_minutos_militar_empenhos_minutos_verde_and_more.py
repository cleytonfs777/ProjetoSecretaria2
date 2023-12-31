# Generated by Django 4.2.4 on 2023-09-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_remove_empenho_duracao_empenho_duracao_em_minutos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='militar',
            old_name='empenhos_em_minutos',
            new_name='empenhos_minutos_verde',
        ),
        migrations.RenameField(
            model_name='militar',
            old_name='qtd_empenhos',
            new_name='empenhos_minutos_vermelha',
        ),
        migrations.AddField(
            model_name='empenho',
            name='classe',
            field=models.CharField(blank=True, choices=[('verde', 'Verde'), ('vermelha', 'Vermelha')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='militar',
            name='qtd_empenhos_verde',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='militar',
            name='qtd_empenhos_vermelha',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='militar',
            name='empenhos',
            field=models.ManyToManyField(blank=True, null=True, related_name='militares', to='cadastros.empenho'),
        ),
        migrations.AlterField(
            model_name='militar',
            name='local',
            field=models.CharField(blank=True, choices=[('acf', 'ACF'), ('acf1', 'ACF-1'), ('acf2', 'ACF-2'), ('acf3', 'ACF-3'), ('sdts1', 'SDTS-1'), ('sdts2', 'SDTS-2'), ('sdts3', 'SDTS-3'), ('nts', 'NTS'), ('gol', 'GOL'), ('sdal', 'SDAL'), ('sdal1', 'SDAL-1'), ('sdal2', 'SDAL-2'), ('sdal3', 'SDAL-3'), ('sdal4', 'SDAL-4'), ('secretaria', 'Secretaria')], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Obs_emp',
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-06 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_gladiator_melee_damage_gladiator_spell_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gladiator',
            old_name='melee_damage',
            new_name='melee_damage_bonus',
        ),
    ]

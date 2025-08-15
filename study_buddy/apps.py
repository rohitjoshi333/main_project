from django.db import migrations

def create_interests(apps, schema_editor):
    Interest = apps.get_model('study_buddy', 'Interest')
    courses = [
        "Web Development",
        "Mobile App Development",
        "Data Analysis",
        "Machine Learning / AI",
        "Data Science",
        "Cybersecurity",
        "Cloud Computing / DevOps",
        "Game Development",
        "Embedded Systems / IoT",
        "Blockchain Development",
        "Software Engineering",
        "UI/UX Design",
    ]
    for name in courses:
        Interest.objects.get_or_create(name=name)

class Migration(migrations.Migration):

    dependencies = [
        ('study_buddy', '0001_initial'),  # your last migration
    ]

    operations = [
        migrations.RunPython(create_interests),
    ]

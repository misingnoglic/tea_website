import csv
import progressbar
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tea_website.settings")
django.setup()
from tea.models import Tea

def import_pics():
    teas = csv.DictReader(open('teas.csv', encoding='utf8'))
    bar = progressbar.ProgressBar(max_value=500)
    for line in teas:
        if line["Picture"]:
            try:
                tea_obj = Tea.objects.get(name=line['Name'].strip().title(), brand__name=line['Brand'].strip())
            except:
                import pdb;pdb.set_trace()
            tea_obj.main_picture = line["Picture"]
            tea_obj.save()

if __name__ == "__main__":
    import_pics()

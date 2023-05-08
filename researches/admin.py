from django.contrib import admin
import researches.models as models

admin.site.register((
    models.Supervisor, models.Student, models.Department, models.Research, models.ResearchAchievement
))

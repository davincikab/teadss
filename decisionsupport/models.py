from django.contrib.gis.db import models

# Create your models here.
class NoticeBoard(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.TextField("Description")
    date_from = models.DateField("From Date")
    date_to = models.DateField("To Date")
    location = models.CharField("Location", max_length=50, blank=True)
    created_on = models.DateTimeField("Created On", auto_now=True)

    class Meta:
        verbose_name = "NoticeBoard"
        verbose_name_plural = "NoticeBoards"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("NoticeBoard_detail", kwargs={"pk": self.pk})

class FarmerIssue(models.Model):
    ISSUE_CHOICES = (
        ('Pest', 'Pest'),
        ('Disease', 'Disease'),
        ('Pest and Diseases', 'Pest and Diseases'),
        ('Others', 'Others')
    )

    title = models.CharField("Title", max_length=50)
    issues = models.CharField("Issue", max_length=50, choices=ISSUE_CHOICES)
    description = models.TextField()
    geom = models.PointField(srid=4326)
    location_name = models.CharField("Location Name", max_length=50)
    reported_on = models.DateTimeField("Reported On", auto_now=True)

    class Meta:
        verbose_name = "Farmer Issue"
        verbose_name_plural = "Farmer Issues"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("FarmerIssue_detail", kwargs={"pk": self.pk})

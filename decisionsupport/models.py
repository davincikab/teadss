from django.db import models

# Create your models here.
class NoticeBoard(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.TextField("Description")
    date_from = models.DateField("From Date")
    date_to = models.DateField("To Date")
    location = models.CharField("Location", max_length=50, blank=True)

    class Meta:
        verbose_name = "NoticeBoard"
        verbose_name_plural = "NoticeBoards"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("NoticeBoard_detail", kwargs={"pk": self.pk})

from django.db import models

class Review(models.Model):
    SECTION_CHOICES = [
        ('trustpilot', 'Trustpilot'),
        ('traders_union', 'Traders Union'),
        ('review_io', 'Review.io'),
        ('brokersview', 'Brokersview'),
        ('forex_peace_army', 'Forex Peace Army'),
    ]

    name = models.CharField(max_length=100)
    stars = models.PositiveSmallIntegerField()  # 1 to 5 stars
    location = models.CharField(max_length=100, blank=True)
    review_content = models.TextField()
    date = models.DateField()
    badge_text = models.CharField(max_length=100, blank=True)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.section}) - {self.stars} Stars"


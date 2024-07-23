from core.models import TimeStampedModel
from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    Model,
    TextChoices,
    TextField,
)


class ContactInfo(Model):
    class ContactType(TextChoices):
        PHONE = "phone"
        EMAIL = "email"
        LINKEDIN = "linkedin"
        PERSONAL_WEBSITE = "personal_website"
        OTHER = "other"

    value = CharField(max_length=100)
    contact_type = CharField(max_length=40, choices=ContactType.choices)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"
        db_table = "contact_infos"
        unique_together = ("value", "contact_type")

    def __str__(self):
        return f"{self.contact_type} - {self.value}"


class Skill(Model):
    name = CharField(max_length=50, primary_key=True, null=False, blank=False)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        db_table = "skills"

    def __str__(self):
        return self.name


class SectionItem(Model):
    section = ForeignKey(
        "Section", related_name="items", on_delete=CASCADE, null=False, blank=False
    )

    title = CharField(max_length=100, null=False, blank=False)
    description = TextField(null=True, blank=True)
    order = IntegerField(default=1)

    start_date = DateField(null=False, blank=False)
    end_date = DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Section Item"
        verbose_name_plural = "Section Items"
        db_table = "section_items"
        ordering = ["order", "pk"]

    def __str__(self):
        return f"Section № {self.order}: {self.title}, {self.start_date} — {self.end_date if self.end_date else 'current'}"


class Section(Model):
    title = CharField(max_length=150, primary_key=True)
    order = IntegerField(default=1)

    resume = ForeignKey(
        "Resume", related_name="sections", on_delete=CASCADE, null=False, blank=False
    )

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Section"
        db_table = "sections"
        ordering = ["order", "pk"]

    def __str__(self):
        return f"Section '{self.title}' of resume '{self.resume.title}'"


class Resume(TimeStampedModel):
    title = CharField(max_length=100, db_index=True, null=False, blank=False)
    subtitle = CharField(max_length=200, db_index=True, null=False, blank=False)
    version = CharField(max_length=5, null=False, blank=False)

    skills = ManyToManyField(Skill, related_name="+")
    contact_information = ManyToManyField(ContactInfo, related_name="+")

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"
        db_table = "resumes"

    def __str__(self):
        return self.title

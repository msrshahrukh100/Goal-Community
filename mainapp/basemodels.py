from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.


def upload_to(instance, filename):
	return "group_banners/%s/%s/%s" % (instance.__class__.__name__, instance.name, filename)


class Group(models.Model):
	name = models.CharField(max_length=255, help_text="The name of the individual group formed within a community")
	slug = AutoSlugField(populate_from='name')
	description = models.TextField(help_text="The description for the group in the community")
	image = models.ImageField(
		upload_to=upload_to,
		null=True,
		blank=True,
		width_field="width_field",
		height_field="height_field", help_text="A image representing the Community")
	height_field = models.IntegerField(default=0, blank=True, null=True)
	width_field = models.IntegerField(default=0, blank=True, null=True)
	target_statement = models.TextField(help_text="What the user wants to achieve while forming this group")
	users = models.ManyToManyField(User, related_name="%(app_label)s_groupusers", help_text="The users who are part of this group")
	unit_name = models.CharField(max_length=255, help_text="Unit of work, eg. chapters when reading a book")
	total_units = models.IntegerField(help_text="The total number of units in the task")
	start_date = models.DateTimeField(help_text="The start date for the task")
	end_date = models.DateTimeField(help_text="The end date for the task")
	is_inactive = models.BooleanField(default=False, help_text="Whether the group is still active, set to false when user deletes it")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, related_name="%(app_label)s_groupcreateduser", on_delete=models.CASCADE)
	updated_by = models.ForeignKey(User, related_name="%(app_label)s_groupupdateduser", on_delete=models.CASCADE)

	class Meta:
		abstract = True


class UnitDescription(models.Model):
	unit = models.IntegerField(default=0)
	unit_title = models.CharField(max_length=300)

	class Meta:
		abstract = True


class UserProgress(models.Model):
	user = models.ForeignKey(User, related_name="%(app_label)s_userprogressuser", help_text="The user who makes the progress in the group", on_delete=models.CASCADE)  # community - userprogress
	progress = models.FloatField(default=0, help_text="The progress of the user") # remove
	at_unit = models.IntegerField(default=0, help_text="The current state of the user, eg. at chapter 2")
	last_progress_made = models.DateTimeField(auto_now=True, help_text="The last date the user made progress")

	class Meta:
		abstract = True


class UserMilestones(models.Model):
	user = models.ForeignKey(User, related_name="%(app_label)s_usermilestones", on_delete=models.CASCADE)

	class Meta:
		abstract = True

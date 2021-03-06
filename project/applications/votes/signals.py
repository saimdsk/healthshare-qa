#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models.signals import pre_save
from django.dispatch import receiver
from project.applications.votes.models import Vote


@receiver(pre_save, sender='votes.Vote', dispatch_uid='votes.pre_save')
def user_post_save(sender, instance=None, created=False, **kwargs):
    instance.value = -1 if instance.type == Vote.DOWNVOTE else 1

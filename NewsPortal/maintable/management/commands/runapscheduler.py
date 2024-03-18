import datetime
import logging
from django.core.mail import EmailMultiAlternatives

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.template.loader import render_to_string

from maintable.models import Post, Category

logger = logging.getLogger(__name__)


def my_job():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'week_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Недельная сводка статей из любимой категории',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = 'Runs apscheduler.'

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), 'default')

        scheduler.add_job(
            my_job(),
            trigger=CronTrigger(day_of_week='wed', hour='19', minute='30'),
            id='my_job',
            max_instances=1,
            replace_existing=True,
        )
        logger.info('Added job "my_job" .')

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(day_of_week='mon', hour='23', minute='00'),
            id='delete_old_dob_executions',
            max_instance=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info('Starting scheduler _ _ _')
            scheduler.start()
        except KeyboardInterrupt:
            logger.info('Stopping scheduler _ _ _')
            scheduler.shutdown()
            logger.info('Scheduler shut down successfully!')

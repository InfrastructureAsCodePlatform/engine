import logging

from celery import current_app

logger = logging.getLogger(__name__)


class register:
    """Decorator for class tasks to name and register them."""

    def __call__(self, cls):
        cls.name = f"{cls.__module__}.{cls.__name__}"
        try:
            current_app.register_task(cls())
        except Exception as e:
            logger.error(e, f"unable to register celery task {cls.name}")
        return cls

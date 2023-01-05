In order to load some test data we should use [django fixtures](https://docs.djangoproject.com/en/4.1/howto/initial-data/) built-in mechanism.

If you want to load already created fixtures for modules & boilerplates you should use these commands:
```shell
docker compose exec harakiri-backend bash -c "django-admin loaddata modules_for_testing"
docker compose exec harakiri-backend bash -c "django-admin loaddata boilerplates_for_testing"
```

If you want to create/update fixtures for modules & boilerplates you should use these commands:
```shell
docker compose exec harakiri-backend bash -c "django-admin dumpdata modules > harakiri/modules/fixtures/modules_for_testing.json"
docker compose exec harakiri-backend bash -c "django-admin dumpdata boilerplates > harakiri/boilerplates/fixtures/boilerplates_for_testing.json"
```

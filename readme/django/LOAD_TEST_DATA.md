In order to load some test data we should use [django fixtures](https://docs.djangoproject.com/en/4.1/howto/initial-data/) built-in mechanism.

If you want to create fixtures for boilerplates you should use this command:
```shell
docker compose exec harakiri-backend bash -c "django-admin dumpdata boilerplates > harakiri/boilerplates/fixtures/boilerplates_for_testing.json"
```

If you want to load already created fixtures for boilerplates you should use this command:
```shell
docker compose exec harakiri-backend bash -c "django-admin loaddata boilerplates_for_testing"
```

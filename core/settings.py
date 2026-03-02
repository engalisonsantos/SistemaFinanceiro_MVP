Starting Container
Traceback (most recent call last):
  File "/app/manage.py", line 11, in <module>
    main()
  File "/app/manage.py", line 8, in main
    execute_from_command_line(sys.argv)
  File "/usr/local/lib/python3.12/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "/usr/local/lib/python3.12/site-packages/django/core/management/__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/usr/local/lib/python3.12/site-packages/django/core/management/base.py", line 412, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/usr/local/lib/python3.12/site-packages/django/core/management/base.py", line 458, in execute
    output = self.handle(*args, **options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^
  File "/usr/local/lib/python3.12/site-packages/django/core/management/base.py", line 106, in wrapper
    res = handle_func(*args, **kwargs)
  File "/usr/local/lib/python3.12/site-packages/django/db/migrations/executor.py", line 18, in __init__
    self.loader = MigrationLoader(self.connection)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/migrations/loader.py", line 58, in __init__
          ^^^^^^^^^^^^^^^^^^^^^^^^^
^^^
  File "/usr/local/lib/python3.12/site-packages/django/core/management/commands/migrate.py", line 117, in handle
    executor = MigrationExecutor(connection, self.migration_progress_callback)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    self.build_graph()
  File "/usr/local/lib/python3.12/site-packages/django/db/migrations/loader.py", line 235, in build_graph
    self.applied_migrations = recorder.applied_migrations()
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/migrations/recorder.py", line 81, in applied_migrations
    if self.has_table():
       ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/migrations/recorder.py", line 57, in has_table
    with self.connection.cursor() as cursor:
         ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 330, in cursor
    return self._cursor()
           ^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 306, in _cursor
    self.ensure_connection()
  File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 289, in ensure_connection
    self.connect()
  File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 269, in connect
    conn_params = self.get_connection_params()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/postgresql/base.py", line 201, in get_connection_params
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: The database name 'railwaypostgresql://postgres:GvFOxCQgHxnGfziBgFjQmRyGrGSrWgiS@postgres.railway.internal:5432/railway' (100 characters) is longer than PostgreSQL's limit of 63 characters. Supply a shorter NAME in settings.DATABASES.
Traceback (most recent call last):
  File "/app/manage.py", line 11, in <module>
    main()
  File "/app/manage.py", line 8, in main
    execute_from_command_line(sys.argv)
  File "/usr/local/lib/python3.12/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "/usr/local/lib/python3.12/site-packages/django/core/management/__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/usr/local/lib/python3.12/site-packages/django/core/management/base.py", line 412, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/usr/local/lib/python3.12/site-packages/django/core/management/base.py", line 458, in execute
    output = self.handle(*args, **options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/core/management/base.py", line 106, in wrapper
    res = handle_func(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/core/management/commands/migrate.py", line 117, in handle
    executor = MigrationExecutor(connection, self.migration_progress_callback)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/migrations/executor.py", line 18, in __init__
    self.loader = MigrationLoader(self.connection)
  File "/usr/local/lib/python3.12/site-packages/django/db/migrations/recorder.py", line 57, in has_table
    with self.connection.cursor() as cursor:
         ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 330, in cursor
    return self._cursor()
           ^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 306, in _cursor
    self.ensure_connection()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/migrations/loader.py", line 58, in __init__
    self.build_graph()
  File "/usr/local/lib/python3.12/site-packages/django/db/migrations/loader.py", line 235, in build_graph
    self.applied_migrations = recorder.applied_migrations()
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/migrations/recorder.py", line 81, in applied_migrations
    if self.has_table():
       ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 289, in ensure_connection
    self.connect()
  File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)

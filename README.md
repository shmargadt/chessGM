# chessGM
# Openshift quickstart: Django

This is a [Django](http://www.djangoproject.com) project that you can use as the starting point to develop your own.

**NOTE:** This version contains obsolete Django 1.11.x LTS which works with RHEL/Centos 7 and Python 2. Consider switching to RHEL/Centos 8 and Python 3 with Django 2.2.x LTS in [branch 2.2.x](https://github.com/sclorg/django-ex/tree/2.2.x) or 3.2.x LTS in [branch 3.2.x](https://github.com/sclorg/django-ex/tree/3.2.x).


```
src/         - 
├──         - 
└──       - 

```

## Warnings

### Database configuration


### Automatic test execution

## Local development
  - macOS:
3. Fork this repo and clone your fork:

4. Install dependencies:


5. Create a development database?

6. If everything is alright, you should be able to start the Django development server.

7. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.
## Logs

By default your Django application is served with gunicorn and configured to output its access log to stderr.
You can look at the combined stdout and stderr of a given pod with this command:

    oc get pods         # list all pods in your project
    oc logs <pod-name>

This can be useful to observe the correct functioning of your application.

## Special environment variables
### APP_CONFIG
### DJANGO_SECRET_KEY
## One-off command execution
## Data persistence
## Looking for help
## License


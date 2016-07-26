========
Mistypes
========

Mistypes is a Django app to let users report about mistypes on your site.

Quick start
-----------

1. Add "mistypes" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'mistypes',
    )

2. Include the mistypes URLconf in your project urls.py like this::

    url(r'^mistypes/', include('mistypes.urls'), namespace="mistypes"),

3. Run `python manage.py migrate` to create the mistypes models.

4. Load mistypes_extras template tags to your template::

    {% load mistypes_extras %}

5. Add jQuery (https://jquery.com/) on your site.

6. Add {% mistype_form %} tag on page, where you want to see reporting form.

7. Start the development server and visit page from step 6. Press CTRL+Enter

8. Now your users can report about mistypes!

9. Visit http://127.0.0.1:8000/admin/ to manage mistypes reported.

10. Add ADMINS setting if you want to be reported by email.

11. Set MISTYPES_CSRF_EXEMPT to True if you doesn't need in csrf protection (ex. using this form on static pages)

Special README for designers/skinners/those mainly concerned with page layout and look-and-feel.

Static files:

All static files live in commons_project/static/. CSS files in /css/, JavaScript files in /js/, etcetera.

Right now, CSS styling for the entire website is going in style.css. We can decide later if we want to divide up styles among different stylesheets. If you find yourself writing special cases / style information that will only apply to one small part of the site, it's a good idea to put those rules in their own section, with comments marking the beginning and end of that section and explaining where those rules apply.


Templates:

First, go read https://docs.djangoproject.com/en/dev/topics/templates/. Especially the section on blocks, extends, and template inheritance -- that's the most awesome and powerful part of Django's templating engine.

Our templates live in multiple places:
	* The base, "apply-to-every-page-on-the-site" templates are in commons_project/templates/.
	* The default templates that come with some other Django apps that we're reusing (e.g. userena, which creates users and their profiles for us) live in commons_project/src/<name_of_app>/<name_of_app>/templates/, if applicable. Do *not* edit these. Instead...
	* Go to commons_project/templates/, click on folder <app_name>, and either edit the template files there or create your own with the same name as the default template file that you want to customize. These template files will override the default ones hidden away with the app.
	* Finally, all the template files for the rest of the site (the most-used stuff, minus the base templates themselves) are in commons_project/commons_core/templates/. These templates correspond to the commons_core models and site organization/presentation pretty closely.

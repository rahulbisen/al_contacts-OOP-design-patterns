from distutils.core import setup

files = ["resources/*"]

setup(
    name = "al_contacts",
    version = "1.0",
    description = "contacts info example with multiple data formats and reader/writer handling",
    author = "Rhul Singh",
    author_email = "rahulbisen@gmail.com",
    packages = ['al_contacts'],
    package_data = {'al_contacts' : files },
    scripts = ["scripts/al_contacts"],
)
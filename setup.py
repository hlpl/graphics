#! /usr/bin/python 
from setuptools  import setup
import os
import sys
import platform
import configparser

from io import open
# to install type:
# python setup.py install --root=/
LONG_DESCRIPTION=open('README.md','r',encoding='utf8').read()        
        
if sys.version_info[0] < 3:
    raise Exception(
        'You are tying to install hlpl_graphics on Python version {}.\n'
        'Please install hlpl_graphics in Python 3 instead.'.format(
            platform.python_version()
        )
    )
    
config = configparser.ConfigParser()
current_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_directory, 'hlpl_graphics/setup.cfg')
config.read(config_file_path)

VERSION = config['hlpl_graphics']['version']
AUTHOR = config['hlpl_graphics']['author']
AUTHOR_EMAIL = config['hlpl_graphics']['email']
URL = config['hlpl_graphics']['url']


projects_urls={}
for i in range(4,len(list(config['hlpl_graphics'].keys()))):
    x=list(config['hlpl_graphics'].keys())[i]
    y=x
    if i>3:
       y=y[0:len(y)-4]
    projects_urls[y]=config['hlpl_graphics'][x]
    

setup (name='hlpl_graphics', version=VERSION,
      description='hlpl_graphics is a software makes graphics (games, movies, animes...)',
      long_description_content_type='text/markdown',  
      long_description = LONG_DESCRIPTION,       
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=URL+'/download/',
      project_urls=projects_urls,      
      python_requires='>=3, <=3.9',
      license='MIT',
      platform="OS independent",
      keywords=['hlpl_graphics', 'hlpl graphics', 'hlpl-graphics', 'NLP', 'hlpl', 'games maker', 'movies maker', 'animes maker'],
      package_dir={'hlpl_graphics': 'hlpl_graphics',},
      packages=['hlpl_graphics',],
      install_requires=[],         
      include_package_data=True,
      entry_points ={
        'console_scripts': [
                'hlpl_graphics = hlpl_graphics.__main__:main',
            ]},   
      classifiers=[
          'Topic :: Games/Entertainment',
          'Topic :: Multimedia :: Graphics',
          ],
                  
    );

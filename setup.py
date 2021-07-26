from distutils.core import setup
setup(
  name = 'uwu',
  packages = ['uwu'],
  version = '1.0.0',
  license='MIT',
  description = 'uwu text generator ٩(◕‿◕｡)۶',
  author = 'Philip Jones',
  author_email = 'philipjonesma@gmail.com',
  url = 'https://github.com/philinphiladelphia/uwuize',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['uwu', "( ‾́ ◡ ‾́ )"], 
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
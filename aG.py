# standard
import os
import hashlib


# project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# settings file
SETTINGS_FILE = os.path.join(BASE_DIR, 'settings.txt')


# license file
LICENSE_FILE = os.path.join(BASE_DIR, 'license.txt')


# salt
SALT = 'bury me aG'



# read settings.txt file and prepare contents
with open(SETTINGS_FILE, 'rt', encoding='utf-8') as f:
    content = ''
    for line in f.readlines()[1:]:
        content += line.strip()
# append salt to settings contents
content += SALT


# write created license into license.txt file
with open(LICENSE_FILE, 'wt') as f:
    f.write(hashlib.md5(content.encode()).hexdigest())

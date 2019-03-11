#!/bin/bash
if [[ -f ../release.py ]]; then
	rm -rf ../release.py
fi

cp release.py ../release.py

cd ..
if [[ -d ./monit_backup ]]; then
	rm -rf ./monit_backup
fi

cp -rf monit monit_backup
python3 release.py

find ./monit_backup -name '*.pyc' -exec rename 's/.cpython-35//' {} \;
find ./monit_backup -name '*.pyc' -execdir mv {} .. \;
find ./monit_backup -name '*.py' -print -exec rm {} \;
find ./monit_backup -name '__pycache__' -exec rmdir {} \;

echo "release done!"
exit 0

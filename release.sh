#!/bin/bash
if [[ -f ../release.py ]]; then
	rm -rf ../release.py
fi

cp release.py ../release.py

cd ..
if [[ -d ./monit_release ]]; then
	rm -rf ./monit_release
fi

cp -rf monit monit_release
python3 release.py

find ./monit_release -name '*.pyc' -exec rename 's/.cpython-35//' {} \;
find ./monit_release -name '*.pyc' -execdir mv {} .. \;
find ./monit_release -name '*.py' -print -exec rm {} \;
find ./monit_release -name '__pycache__' -exec rmdir {} \;

rm release.py
echo "release done!"
exit 0

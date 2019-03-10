#!/bin/bash
if [[ -f ../release.py ]]; then
	rm -rf ../release.py
fi
cp release.py ../release.py
cd ..
python3 release.pyc

#find -name '*.pyc' -exec rename 's/.cpython-35//' {} \;
#find -name '*.pyc' -execdir mv {} .. \;
find -name '*.py' -type f -print -exec rm {} \;
#find -name '__pycache__' -exec rmdir {} \;

echo "release done!"
exit 0

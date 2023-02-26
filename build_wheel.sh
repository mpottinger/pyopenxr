rm -rf build
rm -rf dist

python setup.py bdist_wheel
cp dist/pyopenxr-1.0.2601-py3-none-any.whl /Users/matthewpottinger/StudioProjects/chaquopy-console/app/src/main


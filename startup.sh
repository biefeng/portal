

source /home/BieFeNg/program/miniconda2/bin/activate test

python -V


cd /home/BieFeNg/workspace/portal
echo $(pwd)
nohup  waitress-serve  --port=80 --call app:create_app > portal.log 2>&1 &

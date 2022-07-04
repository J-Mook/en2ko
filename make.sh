# PYTHON_VER=$(python --version)
# PYINSTLL_VER=$(pyinstaller --version)
# if [ ${PYINSTLL_VER:0:1} -ge 3 -a ${PYTHON_VER:7:1} -ge 3 ];then
# echo $PYINSTLL_VER
# echo $PYTHON_VER
# fi
CURDIR=$(pwd)
pyinstaller -w --onefile --icon=/$CURDIR/src/en2ko_icon.ico /$CURDIR/en2ko.py -y
rm -f $CURDIR/dist/en2ko
cp -r $CURDIR/dist/$(ls $CURDIR/dist/) $CURDIR/
rm -r -f build dist en2ko.spec
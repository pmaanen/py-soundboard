CC = gcc
PYINC=-I /opt/local/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7
PYLIB=-L /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages -lPython
CFLAGS=-fPIC
default: soundboard

soundboard.c: soundboard.py
	cython soundboard.py --embed

soundboard: soundboard.c
	gcc soundboard.c $(CFLAGS) $(PYINC) $(PYLIB) -o soundboard
clean:
	$(RM) *~
	$(RM) *.pyc
	$(RM) *.c

distclean: clean
	$(RM) soundboard
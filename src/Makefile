# @author: Tereza Lapčíková (xlapci03)

make: all

all: setup

pack: clean
	mkdir ../../xmager00_xlapci03_xspankt00/
	mkdir ../../xmager00_xlapci03_xspankt00/repo
	mkdir ../../xmager00_xlapci03_xspankt00/doc
	mkdir ../../xmager00_xlapci03_xspankt00/install
	cd ../.. && cp -rf IVS_projekt2/* xmager00_xlapci03_xspankt00/repo
	cd ../.. && cp -rf IVS_projekt2/.[^.]* xmager00_xlapci03_xspankt00/repo
	cp ../dokumentace.pdf ../../xmager00_xlapci03_xspankt00/doc
	cd ../../xmager00_xlapci03_xspankt00 && zip -r ../xmager00_xlapci03_xspankt00.zip .

clean: 
	rm -rf ../latex ../html __pycache__ ../../xmager00_xlapci03_xspankt00 ../../xmager00_xlapci03_xspankt00.zip

test:
	python3 math_test.py
	python3 eval_test.py


doc: 
	doxygen Doxyfile
	sed -i '2s/^/\\usepackage[utf8]{inputenc}\n\\DeclareUnicodeCharacter{221A}{\\sqrt}\n/' ../latex/refman.tex
	-cd ../latex && pdflatex -interaction=nonstopmode refman || true
	-cd ../latex && makeindex refman.idx
	-cd ../latex && pdflatex -interaction=nonstopmode refman || true
	-cd ../latex && latex_count=8 ; \
	-cd ../latex && while egrep -s 'Rerun (LaTeX|to get cross-references right)' refman.log && [ $$latex_count -gt 0 ] ;\
	    do \
	      echo "Rerunning latex...." ;\
	      -pdflatex -interaction=nonstopmode refman || true ;\
	      latex_count=`expr $$latex_count - 1` ;\
	    done
	-cd ../latex && makeindex refman.idx || true
	-cd ../latex && pdflatex -interaction=nonstopmode refman || true
	mv ../latex/refman.pdf ../dokumentace.pdf

run: 
	python3 window.py

profile: setup

setup: requirements.txt
	pip install -r requirements.txt
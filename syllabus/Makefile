TITLE="syllabus"
CAL="cal"

all:
	pdflatex $(TITLE).tex
#	bibtex $(TITLE)
#	pdflatex $(TITLE).tex
	pdflatex $(TITLE).tex

cal:
	pdflatex $(CAL).tex
#	bibtex $(TITLE)
#	pdflatex $(CAL).tex
	pdflatex $(CAL).tex

clean:
	rm -f *.{aux,log,bbl,lof,lot,blg,out}
	rm -f */*.{aux,log,bbl,lof,lot,blg,out}


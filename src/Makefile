all: clean test

transform: kasi.py fact.kasi
	@echo "BEFORE TRANSFORM"
	@echo "***************************"
	@cat fact.kasi
	@echo "***************************"
	@./kasi.py -k ../kw_maps/kw_map_kannada.txt fact.kasi

compile: transform
	@echo 
	@echo "AFTER TRANSFORM"
	@echo "***************************"
	@cat fact.kasi.C
	@echo "***************************"
	@echo 
	@echo "COMPILE"
	@echo "***************************"
	gcc -c -Wall fact.kasi.C
	@echo "***************************"

link: compile
	@echo 
	@echo "LINK"
	@echo "***************************"
	gcc fact.kasi.o -o fact
	@echo "***************************"

test: link
	@echo 
	echo 3 | ./fact
	@echo 
	@echo "***************************"
	@echo "*****BUILD SUCCESSFULL*****"
	@echo "***************************"

clean:
	rm -f fact.kasi.C fact.kasi.o fact

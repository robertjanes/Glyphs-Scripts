Glyphs3ScriptsPath = ~/Library/Application\ Support/Glyphs\ 3/Scripts
Glyphs3ScriptsPathExists = $(shell [ -d $(Glyphs3ScriptsPath) ] && echo 1 || echo 0)

install:
ifeq ($(Glyphs3ScriptsPathExists) , 1)
	@mkdir -p $(Glyphs3ScriptsPath)/Rob’s\ Scripts
	@rsync -a --delete ./ $(Glyphs3ScriptsPath)/Rob’s\ Scripts --exclude=.git --exclude=.gitignore --exclude=Makefile
	@echo "\033[0;32m✔ \033[0;34mInstalled scripts to Glyphs 3 scripts folder\033[0m"
endif

dev:
	fswatch -0 Lib | xargs -0 -n 1 -I {} make install
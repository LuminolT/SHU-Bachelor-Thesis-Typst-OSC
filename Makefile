PROJECT_ROOT := $(abspath .)
FONTS_PATH   := $(abspath ./template/fonts)
OUTPUT_NAME  := thesis


# Build the thesis PDF from the Typst template
default build:
	typst --font-path $(FONTS_PATH) --root=$(PROJECT_ROOT) compile ./thesis.typ $(OUTPUT_NAME).pdf

# Watch for changes to the Typst template and rebuild the thesis automatically
watch:
	typst --font-path $(FONTS_PATH) --root=$(PROJECT_ROOT) --watch ./thesis.typ $(OUTPUT_NAME).pdf

# Convert the thesis PDF to a JPG image (ImageMagick should be installed)
image: build 
	convert -density 500 $(OUTPUT_NAME).pdf $(OUTPUT_NAME).jpg

# Clean up the generated files
clean:
	rm -r *.pdf

# Personal Share of Codes

This is a collection of codes that are not complicated enough to become a standalone project.

## docs

Some HTML pages, view through links:

- [Hyperbolic group presentation](https://jingmatrix.github.io/Code/HyperbolicGroup/index.html)
- [A snake game in genus 2 surface](https://jingmatrix.github.io/Code/h2snake/index.html)

## Shell

This is the interesting part.

### Mathpix for OCR math equation

`Mathpix` is a bash\zsh script that perform OCR for image in the clipboard that contains math equation, and then copy result Latex code to the clipboard.

You need first get a developper API key from [Mathpix](https://accounts.mathpix.com/login?return_to=%2Focr-api), which allows you to use perform OCR 1k times each month.

To run this script, you need set envirment variables `app_id` and `app_key`, and install `jq` for pleasant output in the terminal.

### Add outline to PDF and DJVU ebooks

I refer to the folder `Shell/toc`.

This will be my everlasting small project. It happens that we download PDF or DJVU ebooks from websites like `libegen` without embedded table of contents, also named as bookmarks and outlines. I then start to add bookmarks for them, finished books are shared by [Google Drive](https://drive.google.com/drive/folders/1O279emuW9Z1LGmQ94fbRYfjZoxT8bpwU?usp=sharing).

There are much more details to discuss, if interested please go to [Shell/toc](Shell/toc).

### Backup plugin install state

`Shell/*.plugin` files are directory structure output by `tree` command, they indicates what kind of plugins I installed on my computer. To update state, use:

```bash
cd Shell
./updatePluginState.sh
```

## Mathematica

I sometimes do mathematical experiments and presentations with Wolfram Mathematica.

## Latex

They are my latex drafts. Some pictures locate at [Latex/resource](Latex/resource) are made by `lpe`, `inkscape` and `Mathematica`.

## Python

This folder contains my Python codes for probability modelisation course of M1 course in UPS.

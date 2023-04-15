'''
Author: LuminolT luminol.chen@gmail.com
Date: 2023-03-28 21:44:42
LastEditors: LuminolT luminol.chen@gmail.com
LastEditTime: 2023-04-15 11:10:36
FilePath: /SHU-Bachelor-Thesis-Typst-OSC/tools/bib2gb.py
Description: a script to convert bib to gb

Copyright (c) 2023 by LuminolT, All Rights Reserved.
'''

import bibtexparser

from bibtexparser.bparser import BibTexParser

parser = BibTexParser()
parser.ignore_nonstandard_types = False

with open('test.bib', 'r', encoding='utf-8') as f:
    bib_data = bibtexparser.load(f, parser=parser)


def get_gb_entry_code(entry_type: str) -> str:
    if entry_type == 'article' or entry_type == 'incollection':
        return 'M'
    elif entry_type == 'proceedings' or entry_type == 'inproceedings' or entry_type == 'conference':
        return 'C'
    elif entry_type == 'article':
        return 'J'
    elif entry_type == 'mastersthesis' or entry_type == 'phdthesis':
        return 'D'
    elif entry_type == 'techreport':
        return 'R'
    elif entry_type == 'online':
        return 'EB'
    elif entry_type == 'misc':
        return 'Z'


def bib2gb(bib_item: map) -> str:
    entry_code = get_gb_entry_code(bib_item['ENTRYTYPE'])
    if entry_code == 'M':
        # 普通图书
        author = ', '.join(bib_item['author'].split(' and '))
        title = bib_item['title']
        journal = bib_item['journal']
        year = bib_item['year']
        volume = bib_item['volume']
        number = bib_item['number']
        pages = bib_item['pages']
        return f'{author}. {title}[{entry_code}]. {journal}, {volume}({number}), {pages} ({year}).'

    elif entry_code == 'C':
        # 会议文集
        author = ', '.join(bib_item['author'].split(' and '))
        title = bib_item['title']
        booktitle = bib_item['booktitle']
        year = bib_item['year']
        pages = bib_item['pages']
        return f'{author}. {title}[{entry_code}]. {booktitle}, {pages} ({year}).'

    elif entry_code == 'J':
        # 期刊
        author = ', '.join(bib_item['author'].split(' and '))
        title = bib_item['title']
        journal = bib_item['journal']
        year = bib_item['year']
        volume = bib_item['volume']
        number = bib_item['number']
        pages = bib_item['pages']
        return f'{author}. {title}[{entry_code}]. {journal}, {volume}({number}), {pages} ({year}).'

    elif entry_code == 'D':
        # 学位论文
        author = ', '.join(bib_item['author'].split(' and '))
        title = bib_item['title']
        school = bib_item['school']
        year = bib_item['year']
        return f'{author}. {title}[{entry_code}]. {school}, {year}.'

    elif entry_code == 'R':
        # 技术报告
        author = ', '.join(bib_item['author'].split(' and '))
        title = bib_item['title']
        institution = bib_item['institution']
        year = bib_item['year']
        return f'{author}. {title}[{entry_code}]. {institution}, {year}.'

    elif entry_code == 'EB':
        # 电子文献
        author = ', '.join(bib_item['author'].split(' and '))
        title = bib_item['title']
        year = bib_item['year']
        url = bib_item['url']
        return f'{author}. {title}[{entry_code}]. ({year}). {url} .'

    elif entry_code == 'Z':
        # 其他
        author = ', '.join(bib_item['author'].split(' and '))
        title = bib_item['title']
        year = bib_item['year']
        return f'{author}. {title}[{entry_code}]. {year}.'

    else:
        raise Exception(f'Unknown entry type: {bib_item["ENTRYTYPE"]}')


for bib_item in bib_data.entries:
    print(bib2gb(bib_item))

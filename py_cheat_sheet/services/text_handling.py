import os
import sys
from loguru import logger


CHEAT_SHEET_PATH = 'cheat_sheet/cheat_sheet.txt'
PAGE_SIZE = 1050

cheat_sheet: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    ch = {',', '.', '!', ':', ';', '?'}
    ssize = size
    if len(text) <= size + start:
        ssize = len(text) - start
    else:
        for i in range(size + start - 1, start, -1):
            if text[i] in ch and text[i + 1] not in ch:
                break
            ssize -= 1
    return text[start: start + ssize], ssize


def prepare_cheat_sheet(path: str) -> None:
    with open(path, mode='r', encoding='UTF-8') as file:
        page_num = 1
        start = 0
        text = file.read()
        while text:
            page, page_len = _get_part_text(text, start, PAGE_SIZE)
            text = text[page_len:]
            cheat_sheet[page_num] = page.lstrip()
            page_num += 1
        logger.info("Cheat sheet prepared.")


prepare_cheat_sheet(
    os.path.join(sys.path[0], os.path.normpath(CHEAT_SHEET_PATH))
)

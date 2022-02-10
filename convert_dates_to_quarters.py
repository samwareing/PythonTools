from datetime import datetime
from typing import List


def convert_to_datetime(date, date_format='%d/%m/%Y') -> datetime:
    '''Converts the string to datetime using the English format.'''
    return datetime.strptime(date, date_format)


def convert_to_quarter_text(datet: datetime) -> str:
    '''Converts the datetime to the correct quarter and year format we needed.'''
    year = datet.year
    month = datet.month
    if month in (1, 2, 3):
        quarter = 'Q4'
    elif month in (4, 5, 6):
        quarter = 'Q1'
    elif month in (7, 8, 9):
        quarter = 'Q2'
    elif month in (10, 11, 12):
        quarter = 'Q3'
    else:
        return (f'Something went wrong: {datet}')
    return (f'{quarter} / {year}')


def main():
    '''Main script to convert a list of dates into QQ / YY format.'''
    dates = ['04/01/2022', '04/01/2023', '', '04/01/2024']

    quarter_year_texts = []
    for date in dates:
        if date:
            date = convert_to_datetime(date)
            quarter_year_texts.append(convert_to_quarter_text(date))
        else:
            quarter_year_texts.append('')

    for quarter_year_text in quarter_year_texts:
        print(quarter_year_text)


if __name__ == '__main__':
    main()
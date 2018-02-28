import pytest
import os
import datetime
import pandas as pd


from dpic.compare import SiteData, WbInfoException

country = "TestCountry"


def get_file(name):
    return os.path.join('tests', 'files', name)


def test_valid_wb_info():
    sd = SiteData(country, 'site', 'normal', get_file('valid.json'))
    assert sd.info['wb_path'] == '/vagrant/disagg_tools/TestCountryCOP18DisaggToolv2018.02.26_HTSSELF fixed.xlsx'
    assert isinstance(datetime.datetime.strptime(sd.info.get('timestamp'), '%Y-%m-%d %H:%M:%S'), datetime.datetime)
    assert sd.info['wb_type'] == 'NORMAL'
    assert sd.info['ou_name'] == 'TestCountry'
    assert sd.info['ou_uid'] == 'V0qMZH29CtN'
    assert sd.info['is_clustered'] is False
    assert sd.info['distribution_method'] == 2017
    assert sd.info['support_files_path'] == '/vagrant/support_files/'


def test_invalid_wb_info():
    with pytest.raises(WbInfoException):
        SiteData(country, 'site', 'normal', get_file('invalid.json'))


def test_valid_sitedata_obj():
    sd = SiteData(country, 'site', 'normal', get_file('valid.json'))
    assert isinstance(sd.info, dict)
    assert sd.country == 'TestCountry'
    assert sd.level == 'site'
    assert sd.identifier == 'files/valid.json'
    assert sd.path == get_file('valid.json')
    assert sd.typ == 'normal'
    assert sd.validate_info() is None
    assert isinstance(sd.df, pd.DataFrame)


def test_df_equal():
    sd1 = SiteData(country, 'site', 'normal', get_file('valid.json'))
    sd2 = SiteData(country, 'site', 'normal', get_file('valid.json'))
    assert sd1 == sd2
    assert pd.DataFrame.equals(sd1.df, sd2.df)


def test_df_equal_reordered():
    sd1 = SiteData(country, 'site', 'normal', get_file('valid.json'))
    sd2 = SiteData(country, 'site', 'normal', get_file('valid_equal.json'))
    assert sd1 == sd2
    assert pd.DataFrame.equals(sd1.df, sd2.df)

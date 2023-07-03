from secgpt.schema.base import BaseFiling, FilingType
from secgpt.schema.constants import FILING_10_K_SECTIONS, \
    FILING_10_Q_SECTIONS, FILING_8_K_SECTIONS

from edgar import CompanyFiling

class Filing10K(BaseFiling):
    """ 10k Filing """
    def __init__(self):
        self.data.fromkeys(FILING_10_K_SECTIONS)
    
    @classmethod
    def get_type(cls):
        return FilingType.TenK


class Filing10Q(BaseFiling):
    """ 10-Q Filing """
    def __init__(self):
        self.data.fromkeys(FILING_10_Q_SECTIONS)

    @classmethod
    def get_type(cls):
        return FilingType.TenQ

class Filing8K(BaseFiling):
    """ 8-K Filing """
    def __init__(self):
        self.data.fromkeys(FILING_10_Q_SECTIONS)

    @classmethod
    def get_type(cls):
        return FilingType.EightK
    


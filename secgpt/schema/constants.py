
# For section items, refer to https://sec-api.io/docs/sec-filings-item-extraction-api
FILING_10_K_SECTIONS = [
    '1' , # Business
    '1A', # Risk Factors
    '1B', # Unresolved Staff Comments
    '2' , # Properties
    '3' , # Legal Proceedings
    '4' , # Mine Safety Disclosures
    '5' , # Market for Registrant’s Common Equity, Related Stockholder Matters and Issuer 'Pu'rchases of Equity Securities
    '6' , # Selected Financial Data 
    '7' , # Management’s Discussion and Analysis of Financial Condition and Results of 'Op'erations
    '7A', # Quantitative and Qualitative Disclosures about Market Risk
    '8' , # Financial Statements and Supplementary Data
    '9' , # Changes in and Disagreements with Accountants on Accounting and Financial 'Di'sclosure
    '9A', # Controls and Procedures
    '9B', # Other Information
    '10', # Directors, Executive Officers and Corporate Governance
    '11', # Executive Compensation
    '12', # Security Ownership of Certain Beneficial Owners and Management and Related 'St'ockholder Matters
    '13', # Certain Relationships and Related Transactions, and Director Independence
    '14', # Principal Accountant Fees and Services
]

FILING_10_Q_SECTIONS = [
    'part1item1' , # Financial Statements
    'part1item2' , # Management’s Discussion and Analysis of Financial Condition and Results of Operations
    'part1item3' , # Quantitative and Qualitative Disclosures About Market Risk
    'part1item4' , # Controls and Procedures
    'part2item1' , # Legal Proceedings
    'part2item1a', # Risk Factors
    'part2item2' , # Unregistered Sales of Equity Securities and Use of Proceeds
    'part2item3' , # Defaults Upon Senior Securities
    'part2item4' , # Mine Safety Disclosures
    'part2item5' , # Other Information
    'part2item6' , # Exhibits
]

FILING_8_K_SECTIONS = [
    '1-1', # Entry into a Material Definitive Agreement
    '1-2', # Termination of a Material Definitive Agreement
    '1-3', # Bankruptcy or Receivership
    '1-4', # Mine Safety - Reporting of Shutdowns and Patterns of Violations
    '2-1', # Completion of Acquisition or Disposition of Assets
    '2-2', # Results of Operations and Financial Condition
    '2-3', # Creation of a Direct Financial Obligation or an Obligation under an Off-Balance Sheet Arrangement of a Registrant
    '2-4', # Triggering Events That Accelerate or Increase a Direct Financial Obligation or an Obligation under an Off-Balance Sheet Arrangement
    '2-5', # Cost Associated with Exit or Disposal Activities
    '2-6', # Material Impairments
    '3-1', # Notice of Delisting or Failure to Satisfy a Continued Listing Rule or Standard; Transfer of Listing
    '3-2', # Unregistered Sales of Equity Securities
    '3-3', # Material Modifications to Rights of Security Holders
    '4-1', # Changes in Registrant's Certifying Accountant
    '4-2', # Non-Reliance on Previously Issued Financial Statements or a Related Audit Report or Completed Interim Review
    '5-1', # Changes in Control of Registrant
    '5-2', # Departure of Directors or Certain Officers; Election of Directors; Appointment of Certain Officers: Compensatory Arrangements of Certain Officers
    '5-3', # Amendments to Articles of Incorporation or Bylaws; Change in Fiscal Year
    '5-4', # Temporary Suspension of Trading Under Registrant's Employee Benefit Plans
    '5-5', # Amendments to the Registrant's Code of Ethics, or Waiver of a Provision of the Code of Ethics
    '5-6', # Change in Shell Company Status
    '5-7', # Submission of Matters to a Vote of Security Holders
    '5-8', # Shareholder Nominations Pursuant to Exchange Act Rule 14a-11
    '6-1', # ABS Informational and Computational Material
    '6-2', # Change of Servicer or Trustee
    '6-3', # Change in Credit Enhancement or Other External Support
    '6-4', # Failure to Make a Required Distribution
    '6-5', # Securities Act Updating Disclosure
    '6-6', # Static Pool
    '6-10', # Alternative Filings of Asset-Backed Issuers
    '7-1', # Regulation FD Disclosure
    '8-1', # Other Events
    '9-1', # Financial Statements and Exhibits
    'signature', # Signature
]

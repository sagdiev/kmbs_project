
def compare_ticker_lists(list_1, list_2):
    # анализ расхождений между нашим списком sp500 2020/05 и акциями из списка sp500 за 2020 - перепроверка актуальности

    list_1_minus_list_2 = [item for item in list_1 if item not in list_2]
    list_1_common_list_2 = [item for item in list_1 if item in list_2]
    list_2_minus_list_1 = [item for item in list_2 if item not in list_1]

    print('list_1 = ', list_1)
    print('list_1 = ', len(list_1))
    print('list_2 = ', list_2)
    print('list_2 = ', len(list_2))

    print('list_1_minus_list_2 = ', list_1_minus_list_2)
    print('list_1_minus_list_2 = ', len(list_1_minus_list_2))

    print('list_1_common_list_2 = ', list_1_common_list_2)
    print('list_1_common_list_2 = ', len(list_1_common_list_2))

    print('list_2_minus_list_1 = ', list_2_minus_list_1)
    print('list_2_minus_list_1 = ', len(list_2_minus_list_1))

    return list_1_minus_list_2, list_1_common_list_2, list_2_minus_list_1


sp500_2020_05_01_part_1 = [
    'AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'AMGN', 'AMZN', 'AVGO', 'AXP', 'BA', 'BAC', 'BKNG', 'BLK', 'BMY', 'BRK.B',
    'C', 'CAT', 'CB', 'CELG', 'CHTR', 'CMCSA', 'COP', 'COST', 'CRM', 'CSCO', 'CVS', 'CVX', 'DIS', 'FB', 'GE', 'GILD',
    'GOOG', 'GOOGL', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ',
    'MDT', 'MMM', 'MO', 'MRK', 'MS', 'MSFT', 'MU', 'NEE', 'NFLX', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PFE', 'PG', 'PM',
    'PNC', 'PYPL', 'QCOM', 'SBUX', 'SCHW', 'SLB', 'T', 'TMO', 'TWX', 'TXN', 'UNH', 'UNP', 'UPS', 'USB', 'V', 'VZ',
    'WFC', 'WMT', 'XOM']

sp500_2020_05_01_part_2 = [
    'ADP', 'AGN', 'AIG', 'AMAT', 'AMT', 'ANTM', 'AON', 'APD', 'ATVI', 'BDX', 'BIIB', 'BK', 'BSX', 'CCI', 'CI', 'CL',
    'CME', 'COF', 'CSX', 'CTSH', 'D', 'DAL', 'DE', 'DHR', 'DUK', 'EA', 'EBAY', 'EMR', 'EOG', 'ESRX', 'ETN', 'EXC', 'F',
    'FDX', 'FOXA', 'GD', 'GM', 'HAL', 'HPQ', 'HUM', 'ICE', 'ILMN', 'INTU', 'ISRG', 'ITW', 'JCI', 'KHC', 'KMB', 'LRCX',
    'MAR', 'MET', 'MMC', 'NOC', 'NSC', 'OXY', 'PRU', 'PSX', 'SO', 'SPG', 'SPGI', 'STT', 'STZ', 'SYK', 'TEL', 'TGT',
    'TJX', 'TRV', 'VLO', 'VRTX', 'WBA', 'ZTS']

sp500_2020_05_01_part_3 = [
    'A', 'AAL', 'AAP', 'ABC', 'ABMD', 'ADI', 'ADM', 'ADS', 'ADSK', 'AEE', 'AEP', 'AFL', 'AIV', 'AIZ', 'AJG', 'AKAM',
    'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'ALXN', 'AMCR', 'AMD', 'AME', 'AMP', 'ANET', 'ANSS', 'AOS', 'APA', 'APH',
    'APTV', 'ARE', 'ATO', 'AVB', 'AVY', 'AWK', 'AZO', 'BAX', 'BBY', 'BF.B', 'BLL', 'BR', 'BWA', 'BXP', 'CDNS', 'CHRW',
    'COG', 'CPB', 'ECL', 'LNT', 'LYB', 'PGR', 'SHW', 'WM']

sp500_2020_05_01_part_4 = [
    'BEN', 'ES', 'EXPD', 'EXPE', 'EXR', 'FAST', 'FBHS', 'FCX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLIR', 'FLS',
    'FLT', 'FMC', 'FRC', 'FRT', 'FTNT', 'FTV', 'GIS', 'GL', 'GPC', 'GPN', 'GPS', 'GRMN', 'GWW', 'HAS', 'HBAN', 'HBI',
    'HCA', 'HES', 'HFC', 'HIG', 'HII', 'HLT', 'HOG', 'HOLX', 'HP', 'HPE', 'HRB', 'HRL', 'HSIC', 'HST', 'HSY', 'HWM',
    'IDXX', 'IEX', 'INCY', 'INFO', 'IP', 'IPG', 'IPGP', 'IQV', 'IR', 'IRM', 'IT', 'IVZ', 'J', 'JBHT', 'JNPR', 'K',
    'KEY', 'KEYS', 'KIM', 'KLAC', 'KMI', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LDOS', 'LEG', 'LEN', 'LH', 'LHX', 'LIN', 'LKQ',
    'LNC', 'LVS', 'LYV', 'MAS', 'MCK', 'MKC', 'MKTX', 'MLM', 'MPC', 'MRO', 'MTB', 'MXIM', 'PEAK', 'RE', 'SJM', 'LW']

sp500_2020_05_01_part_5 = [
    'LUV', 'DGX', 'FTI', 'JWN', 'MAA', 'MCHP', 'MCO', 'MGM', 'MHK', 'MNST', 'MOS', 'MSCI', 'MSI', 'MTD', 'MYL', 'NBL',
    'NCLH', 'NDAQ', 'NEM', 'NI', 'NLOK', 'NLSN', 'NOV', 'NOW', 'NRG', 'NTAP', 'NTRS', 'NUE', 'NVR', 'NWL', 'NWS',
    'NWSA', 'O', 'ODFL', 'OKE', 'OMC', 'ORLY', 'OTIS', 'PAYC', 'PAYX', 'PBCT', 'PCAR', 'PEG', 'PFG', 'PH', 'PHM', 'PKG',
    'PKI', 'PLD', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PSA', 'PVH', 'PWR', 'PXD', 'QRVO', 'RCL', 'REG', 'REGN', 'RF',
    'RHI', 'RJF', 'RL', 'RMD', 'ROK', 'ROL', 'ROP', 'ROST', 'RSG', 'RTX', 'SBAC', 'SEE', 'SIVB', 'SLG', 'SNA', 'SNPS',
    'SRE', 'STE', 'STX', 'SWK', 'SWKS', 'SYF', 'SYY', 'TAP', 'TDG', 'TFC', 'TFX', 'TIF', 'TMUS', 'TPR', 'TROW', 'TSCO',
    'TT', 'TTWO', 'TWTR', 'TXT']
#
sp500_2020_05_01_part_6 = [
    'UAA', 'DPZ', 'DXCM', 'TSN', 'UA', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNM', 'URI', 'VAR', 'VFC', 'VIAC', 'VMC', 'VNO',
    'VRSK', 'VRSN', 'VTR', 'WAB', 'WAT', 'WDC', 'WEC', 'WELL', 'WHR', 'WLTW', 'WMB', 'WRB', 'WRK', 'WU', 'WY', 'WYNN',
    'XEL', 'XLNX', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZBRA', 'ZION']

sp500_2020_05_01 = sp500_2020_05_01_part_1 +\
                   sp500_2020_05_01_part_2 +\
                   sp500_2020_05_01_part_3 +\
                   sp500_2020_05_01_part_4 +\
                   sp500_2020_05_01_part_5 +\
                   sp500_2020_05_01_part_6

currency_history = [
    '^USDZAR', '^USDAUD', '^USDCAD', '^USDCHF', '^USDDKK', '^USDEUR',
    '^USDGBP', '^USDJPY', '^USDNOK', '^USDSEK', '^USDSGD']

crypto_history = [
    '^XRPUSD', '^xmrusd', '^xlmusd', '^USDTUSD', '^LTCUSD', '^ETHUSD',
    '^EOSUSD', '^etcusd', '^dashusd', '^BTCUSD', '^BCHUSD', '^adausd']

losers_2000 = [
    'AABA', 'ABX', 'ACV', 'ADCT', 'AES', 'AET', 'AGC', 'AL', 'AM', 'APC', 'ARC', 'ARNC', 'ASH', 'AT', 'ATI', 'AVP',
    'BBBY', 'BBT', 'BC', 'BCR', 'BEAM', 'BFO', 'BGG', 'BHGE', 'BIG', 'BMS', 'BUD', 'CA', 'CAR', 'CBS', 'CCE', 'CCK',
    'CCU', 'CEN', 'CG', 'CHA', 'COMS', 'CPWR', 'CR', 'CTB', 'CTX', 'DDS', 'DELL', 'DLX', 'EC', 'EFU', 'EHC', 'EMC',
    'FDC', 'FMCC', 'FNMA', 'G', 'GAS', 'GRA', 'GT', 'GTE', 'H', 'HCR', 'HI', 'IFF', 'ITT', 'JCP', 'JP', 'KATE', 'KBH',
    'KMG', 'LPX', 'LSI', 'LXK', 'M', 'MAT', 'MBI', 'MDP', 'MDR', 'MIL', 'MTG', 'NAV', 'NC', 'NSM', 'NYT', 'ODP', 'OI',
    'ONE', 'PBI', 'PBY', 'PCG', 'PCH', 'PD', 'PLL', 'PSFT', 'PTC', 'PX', 'R', 'RAD', 'RDC']

sp500_2000_01_03 = [
    'AABA', 'AAMRQ', 'AAPL', 'ABI', 'ABS', 'ABT', 'ABX', 'ACKH', 'ACV', 'ADBE', 'ADCT', 'ADI', 'ADM', 'ADP', 'ADSK',
    'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AFS.A', 'AGC', 'AGN', 'AIG', 'AL', 'ALL', 'AM', 'AMAT', 'AMD', 'AMGN', 'ANDW',
    'AON', 'APA', 'APC', 'APD', 'ARC', 'ARNC', 'ASH', 'ASO', 'AT', 'ATI', 'AVP', 'AVY', 'AW', 'AXP', 'AZA.A', 'AZO',
    'BA', 'BAC', 'BAX', 'BBBY', 'BBT', 'BBY', 'BC', 'BCR', 'BDK', 'BDX', 'BEAM', 'BEN', 'BF.B', 'BFO', 'BGG', 'BHGE',
    'BHMSQ', 'BIG', 'BK', 'BLL', 'BLS', 'BMC', 'BMET', 'BMS', 'BMY', 'BNI', 'BOL', 'BR', 'BSC', 'BSX', 'BUD', 'C', 'CA',
    'CAG', 'CAH', 'CAR', 'CAT', 'CB', 'CBE', 'CBS', 'CCE', 'CCK', 'CCL', 'CCTYQ', 'CCU', 'CEG', 'CEN', 'CFC', 'CG',
    'CGP', 'CHA', 'CI', 'CIN', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CMI', 'CMS', 'CMVT', 'CNC', 'CNG', 'CNP', 'COC.B',
    'COF', 'COMS', 'COP', 'COST', 'CPB', 'CPQ', 'CPWR', 'CR', 'CSCO', 'CSR', 'CSX', 'CTB', 'CTL', 'CTX', 'CTXS', 'CVS',
    'CVX', 'D', 'DALRQ', 'DCNAQ', 'DD', 'DDS', 'DE', 'DELL', 'DG', 'DHR', 'DIS', 'DJ', 'DLX', 'DOV', 'DOW', 'DPHIQ',
    'DRI', 'DTE', 'DUK', 'DXC', 'EC', 'ECL', 'ED', 'EDS', 'EFU', 'EFX', 'EHC', 'EIX', 'EKDKQ', 'EMC', 'EMN', 'EMR',
    'ENRNQ', 'EP', 'ETN', 'ETR', 'ETS', 'EXC', 'F', 'FBF', 'FCX', 'FDC', 'FDX', 'FE', 'FITB', 'FJ', 'FLTWQ', 'FMC',
    'FMCC', 'FNMA', 'FPC', 'FWLT', 'G', 'GAPTQ', 'GAS', 'GD', 'GDT', 'GDW', 'GE', 'GIS', 'GLK', 'GLW', 'GP', 'GPC',
    'GPS', 'GPU', 'GR', 'GRA', 'GT', 'GTE', 'GTW', 'GWW', 'GX', 'H', 'HAL', 'HAS', 'HBAN', 'HCA', 'HCR', 'HD', 'HES',
    'HET', 'HI', 'HIG', 'HLT', 'HM', 'HNZ', 'HON', 'HPC', 'HPQ', 'HRB', 'HSH', 'HSY', 'HUM', 'IBM', 'IFF', 'IKN',
    'INCLF', 'INTC', 'IP', 'IPG', 'IR', 'ITT', 'ITW', 'JAVA', 'JCI', 'JCP', 'JNJ', 'JOS', 'JP', 'JPM', 'JWN', 'K',
    'KATE', 'KBH', 'KEY', 'KLAC', 'KM', 'KMB', 'KMG', 'KO', 'KR', 'KRB', 'KRI', 'KSS', 'KSU', 'L', 'LB', 'LDG', 'LEG',
    'LEHMQ', 'LLY', 'LMT', 'LNC', 'LOW', 'LPX', 'LSI', 'LU', 'LUV', 'LXK', 'M', 'MAR', 'MAS', 'MAT', 'MAY', 'MBI',
    'MCD', 'MCK', 'MCO', 'MDP', 'MDR', 'MDT', 'MEA', 'MEE', 'MEL', 'MER', 'MIL', 'MIR', 'MKG', 'MMC', 'MMM', 'MO',
    'MOLX', 'MRK', 'MRO', 'MS', 'MSFT', 'MSI', 'MTG', 'MTLQQ', 'MU', 'MWV', 'MYG', 'MZIAQ', 'NAV', 'NC', 'NCC', 'NCE',
    'NEE', 'NEM', 'NGH', 'NKE', 'NLV', 'NMK', 'NOC', 'NOVL', 'NRTLQ', 'NSC', 'NSI', 'NSM', 'NTAP', 'NTRS', 'NUE', 'NWL',
    'NXTL', 'NYT', 'OAT', 'ODP', 'OI', 'OK', 'OKE', 'OMC', 'OMX', 'ONE', 'ORCL', 'OWENQ', 'OXY', 'PAYX', 'PBI', 'PBY',
    'PCAR', 'PCG', 'PCH', 'PCS', 'PD', 'PDG', 'PEG', 'PEP', 'PFE', 'PG', 'PGL', 'PGN', 'PGR', 'PH', 'PHA', 'PHM', 'PKI',
    'PLL', 'PNC', 'PNU', 'PNW', 'PPG', 'PPL', 'PRD', 'PSFT', 'PTC', 'PTV', 'PVN', 'PWJ', 'PX', 'QCOM', 'QTRN', 'R',
    'RAD', 'RAL', 'RBK', 'RDC', 'RDS.A', 'RF', 'RIG', 'RLM', 'RML', 'ROH', 'ROK', 'RRD', 'RSHCQ', 'RTN', 'RX', 'S',
    'SAF', 'SCHW', 'SCI', 'SEE', 'SEG', 'SFA', 'SGID', 'SGP', 'SHW', 'SIAL', 'SLB', 'SLM', 'SLR', 'SMI', 'SMS', 'SNA',
    'SNV', 'SO', 'SOTR', 'SPGI', 'SPLS', 'SRE', 'STI', 'STJ', 'STT', 'SUB', 'SUN', 'SVU', 'SWK', 'SWY', 'SXCL', 'SYY',
    'T', 'TAP', 'TEK', 'TER', 'TGNA', 'TGT', 'THC', 'TIN', 'TJX', 'TKR', 'TLAB', 'TMC', 'TMC.A', 'TMK', 'TMO', 'TNB',
    'TOS', 'TOY', 'TRB', 'TROW', 'TRV', 'TRW', 'TUP', 'TWX', 'TX', 'TXN', 'TXT', 'TXU', 'UAWGQ', 'UCL', 'UCM', 'UIS',
    'UK', 'UMG', 'UN', 'UNH', 'UNM', 'UNP', 'UPC', 'UPR', 'USB', 'UST', 'USW', 'UTX', 'VFC', 'VMC', 'VO', 'VZ', 'WAMUQ',
    'WB', 'WBA', 'WCOEQ', 'WEN', 'WFC', 'WHR', 'WLA', 'WLL', 'WLP', 'WM', 'WMB', 'WMT', 'WNDXQ', 'WOR', 'WWY', 'WY',
    'WYE', 'X', 'XEL', 'XLNX', 'XOM', 'XRX', 'YUM']


sp500_2020_01_28 = [
    'A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABMD', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'AEE',
    'AEP', 'AES', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'ALXN', 'AMAT',
    'AMCR', 'AMD', 'AME', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'APD', 'APH',
    'APTV', 'ARE', 'ARNC', 'ATO', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BAC', 'BAX', 'BBY', 'BDX',
    'BEN', 'BF.B', 'BIIB', 'BK', 'BKNG', 'BKR', 'BLK', 'BLL', 'BMY', 'BR', 'BRK.B', 'BSX', 'BWA', 'BXP', 'C', 'CAG',
    'CAH', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CCL', 'CDNS', 'CDW', 'CE', 'CERN', 'CF', 'CFG', 'CHD', 'CHRW', 'CHTR',
    'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COG', 'COO', 'COP',
    'COST', 'COTY', 'CPB', 'CPRI', 'CPRT', 'CRM', 'CSCO', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTVA', 'CTXS', 'CVS', 'CVX',
    'CXO', 'D', 'DAL', 'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DLR', 'DLTR',
    'DOV', 'DOW', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DXC', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN',
    'EMR', 'EOG', 'EQIX', 'EQR', 'ES', 'ESS', 'ETFC', 'ETN', 'ETR', 'EVRG', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F',
    'FANG', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLIR', 'FLS', 'FLT', 'FMC', 'FOX',
    'FOXA', 'FRC', 'FRT', 'FTI', 'FTNT', 'FTV', 'GD', 'GE', 'GILD', 'GIS', 'GL', 'GLW', 'GM', 'GOOG', 'GOOGL', 'GPC',
    'GPN', 'GPS', 'GRMN', 'GS', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA', 'HD', 'HES', 'HFC', 'HIG', 'HII', 'HLT',
    'HOG', 'HOLX', 'HON', 'HP', 'HPE', 'HPQ', 'HRB', 'HRL', 'HSIC', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IDXX', 'IEX',
    'IFF', 'ILMN', 'INCY', 'INFO', 'INTC', 'INTU', 'IP', 'IPG', 'IPGP', 'IQV', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ',
    'J', 'JBHT', 'JCI', 'JKHY', 'JNJ', 'JNPR', 'JPM', 'JWN', 'K', 'KEY', 'KEYS', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI',
    'KMX', 'KO', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LDOS', 'LEG', 'LEN', 'LH', 'LHX', 'LIN', 'LKQ', 'LLY', 'LMT', 'LNC',
    'LNT', 'LOW', 'LRCX', 'LUV', 'LVS', 'LW', 'LYB', 'LYV', 'M', 'MA', 'MAA', 'MAR', 'MAS', 'MCD', 'MCHP', 'MCK', 'MCO',
    'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MKTX', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOS', 'MPC', 'MRK', 'MRO',
    'MS', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'MXIM', 'MYL', 'NBL', 'NCLH', 'NDAQ', 'NEE', 'NEM', 'NFLX', 'NI',
    'NKE', 'NLOK', 'NLSN', 'NOC', 'NOV', 'NOW', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NWL', 'NWS',
    'NWSA', 'O', 'ODFL', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYC', 'PAYX', 'PBCT', 'PCAR', 'PEAK', 'PEG', 'PEP',
    'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU',
    'PSA', 'PSX', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RJF', 'RL',
    'RMD', 'ROK', 'ROL', 'ROP', 'ROST', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCHW', 'SEE', 'SHW', 'SIVB', 'SJM', 'SLB', 'SLG',
    'SNA', 'SNPS', 'SO', 'SPG', 'SPGI', 'SRE', 'STE', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYY', 'T',
    'TAP', 'TDG', 'TEL', 'TFC', 'TFX', 'TGT', 'TIF', 'TJX', 'TMO', 'TMUS', 'TPR', 'TROW', 'TRV', 'TSCO', 'TSN', 'TTWO',
    'TWTR', 'TXN', 'TXT', 'UA', 'UAA', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'UTX',
    'V', 'VAR', 'VFC', 'VIAC', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAB', 'WAT', 'WBA', 'WDC',
    'WEC', 'WELL', 'WFC', 'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRB', 'WRK', 'WU', 'WY', 'WYNN', 'XEC', 'XEL', 'XLNX',
    'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZBRA', 'ZION', 'ZTS']

# # анализ расхождений между нашим списком sp500 2020/05 и акциями из списка sp500 за 2000
# compare_ticker_lists(sp500_2000_01_03, sp500_2020_05_01)
#
# # анализ расхождений между нашим списком sp500 2020/05 и акциями из списка sp500 за 2020 - перепроверка актуальности
# compare_ticker_lists(sp500_2020_01_28, sp500_2020_05_01)
#
# # анализ расхождений между
# compare_ticker_lists(losers_2000, sp500_2020_01_28)
#
# # анализ расхождений между
# compare_ticker_lists(losers_2000, sp500_2000_01_03)
#
# # анализ расхождений между
# compare_ticker_lists(sp500_2020_01_28, sp500_2020_05_01 + losers_2000)
